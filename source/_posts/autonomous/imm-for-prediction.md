---
title: Using Interacting Multiple Model(IMM) algorithm to predict pedestrian and vehicle's trajectroy
mathjax: true
date: 2020-10-29 19:37:24
---

For self-driving vehicle, it's important to reliably predict the movement of traffic agents around ego car, such as vehicles, cyclists and pedestrians.

We have many neural networks to predict obstacle on lane, but for obstacles which are not on lane, we now have poor method to predict them.

<!-- more -->

# Current predictor for obstacles not on lane
If an obstacle(vehicle/bicycle/pedestrian) is not on lane, we use a `FreeMovePredictor` to predict its trajectory. `FreeMovePredictor` assumes that the obstacle always moves with constant acceleration, the state is:
$$
\begin{bmatrix}
x \\\\
y \\\\
x^\prime \\\\
y^\prime \\\\
x^{\prime\prime} \\\\
y^{\prime\prime}
\end{bmatrix}
$$
and the transition matrix is:
$$
\begin{bmatrix}
1 & 0 & t & 0 & 0.5 * t^2 & 0 \\\\
0 & 1 & 0 & t & 0 & 0.5 * t^2 \\\\
0 & 0 & 1 & 0 & t & 0 \\\\
0 & 0 & 0 & 1 & 0 & t \\\\
0 & 0 & 0 & 0 & 1 & 0 \\\\
0 & 0 & 0 & 0 & 0 & 1
\end{bmatrix}
$$
The disadvantages are:
1. We use the newest position and velocity from perception module, but the result is not so accurate.
2. It performs not so good especially for vehicles.

To solve these problems and imporve the prediction accuracy off lane, we use
- constant velocity kalman filter to predict pedestrian;
- interacting multiple model of constant velocity(cv), constant acceleration(ca) and constant turn rate(ct) to predict vehicle and bicycle.

# Kalman filter
In 1960, R.E. Kalman published his famous paper describing a recursive solution to the discent-data linear filtering problem. Since that time, due in large part to advances in digital computing, the Kalman filter has been the subject of extensive research and application, particularly in the area of autonomous or assisted navigation.

The Kalman filter is a set of mathematical equations that provides an efficient computational (recursive) means to estimate the state of a process, in a way that minimizes the mean of the squared error. The filter is very powerful in several aspects: it supports estimations of past, present, and even future states, and it can do so even when the precise nature of the modeled system is unknown.

## The process to be estimated
The Kalman filter addresses the general problem of trying to estimate the state $x \in \Re^n$ of a discrete-time controlled process that is governed by the linear stochastic difference equation:
$$
x_k = Ax_{k-1} + Bu_{k-1} + w_{k-1} \tag1
$$
with a measurement $z \in \Re^m$ that is:
$$
z_k = Hx_k + v_k \tag2
$$
- The $n * n$ matrix $A$ is `transition matrix` which relates the state at the previous time step $k - 1$ to the state at the current step $k$, in the absence of either a driving function or process noise. Note that in practice A might change with each time step, but here we assume it is constant.
- The $n * l$ matrix $B$ is `control matrix` which relates the optional control input $u \in \Re^l$ to the state $x$.
- The $m * n$ matrix $H$ is `measurement matrix` which relates the state to the measurement $z_k$. In practice $H$ might change with each time step ore measurement, but we assume it is constant.

The random variable $w_k$ and $v_k$ represent the process and measurement noise. They are assumed to be independent(of each other), white and with normal probability distributions:
$$
p(w) \sim N(0, Q) \tag3
$$
$$
p(v) \sim N(0, R) \tag4
$$
where the $Q$ is `process noise covariance` and R is `measurement noise convariance`, they might change with each time step or measurement, but we assume that they are constant.

## The computational origin of the filter
We define $\hat{x}\_k^- \in \Re^n$ to be our `priori state` estimate at step $k$ given knowledge of the process prior to step $k$ and $\hat{x}\_k \in \Re^n$ to be our `posteriori state` estimate at step $k$ given measurement $z_k$. We can then define a `priori` and a `posteriori` estimate errors as:
$$
e\_k^- \equiv x\_k - \hat{x}\_k^- \tag5
$$

$$
e\_k \equiv x\_k - \hat{x}\_k \tag6
$$

The `priori` estimate error covariance is then:
$$
P\_k^- = E[e\_k^-(e\_k^-)^T] \tag7
$$
and the `posteriori` estimate error covariance is:
$$
P\_k = E[e\_ke\_k^T] \tag8
$$

In deriving the equation for the Kalman filter, we begin with the goal of finding an equation that compute an `posteriori` state estimate $\hat{x}\_k$ as a linear combination of the `priori` estimate $\hat{x}\_k^-$ and a weighted difference between an actual measurement $z\_k$ and a measurement prediction $H\hat{x}\_k^-$ as shown below:
$$
\hat{x}\_k = \hat{x}\_k^- + K(z\_k - H\hat{x}\_k^-) \tag9
$$
The difference $(z_k - H\hat{x}_k^-)$ is called the measurement `innovation` or `residual`. The residual reflects the discrepancy between the predicted measurement $H\hat{x}_k^-$ and the actual measurement $z_k$. A residual of zero means that the two are in complete agreement.

The $n*m$ matrix $K$ is chosen to be the `gain` or `blending factor` that minimizes the `posteriori` error covariance in (8). 

This minimization can be accomplished by 
1. substituting (9) into the (6) and substituting that into (8);
2. performing the indicated expectations;
3. taking the derivative of the trace of the result with respcet to $K$,
4. setting the result equal to $0$ and then solving for $K$.

One form of the resulting $K$ that minimizeds (8) is:
$$
\begin{align}
K_k &= P_k^-H^T(HP_k^-H^T + R)^{-1} \\\\
    &= \frac{P_k^-H^T}{HP_k^-HT + R}
\end{align} \tag{10}
$$

Looking at (10) we see that as the measurement error covariance $R \to 0$, the gain $K$ weights the residual more heavily. Specifically,
$$
\lim_{R_k \to 0}K_k = H^-1 \tag{11}
$$
On the other hand, as the `priori` estimate error convariance $P_k^- \to 0$, the gain $K$ weights the residual less heavily. Specially,
$$
\lim_{P_0^- \to 0} K_k = 0 \tag{12}
$$

Another way of thinking about the weighting by $K$ is that as the measurement error covariance $R \to 0$, the actual measurement $z_k$ is `trusted` more and more, while the predicted measurement $H\hat{x}_k^-$ is trusted less and less. On the other hand, as the `priori` estimate error covariance $P_k^- \to 0$ the actual measurement $z_k$ is trusted less and less, while the predicted measurement $H\hat{x}_k^-$ is trusted more and more.

## The discrete kalman filter algorithm
The Kalman filter estimate a process by using a form of feedback control: the filter estimates the process state at some time and then obtains feedback in the form of (noisy) measurement. As such, the equations for the Kalman filter falls into two groups:
- `time update`(predict) equations;
- `measurement update`(correct) equations.

The `time update` equations are responsible for projecting forward(in time) the current state and error covariance estimates to obtain the `priori` estimates for the next time step.

The `measurement update` equations are responsible for the feedback, incorporating a new measurement into the `priori` estimate to obtain an improved `posteriori` estimate.

The final estimation algorithm resembles that of a `predictor-corrector` algorithm for solving numerical problems:
```
           Time Update -----> Measurement Update
            (Predict)             (Correct)
                ^                     |
                |                     |
                -----------------------
```

The specific equations for the `time update` are:

$$
\hat{x}\_k^- = A \hat{X}\_{k-1} + B u\_{k-1} \tag{13}
$$

$$
P_k^- = AP_{k-1}A^T + Q \tag{14}
$$

where:
- $\hat{X}_{k-1}$ is the `posteriori` state from time step $k-1$;
- $u_{k-1}$ is the control from time step $k-1$;
- $\hat{x}_k^-$ is the `priori` state from time step $k$;
- $P_{k-1}$ is the `posteriori` estimate error covariance from time step $k-1$;
- $P_k^-$ is the `priori` estimate error covariance from time step $k$.

The specific equations for the `measurement update` are:

$$
K_k = P_k^-H^T(HP_k^-H^T + R)^{-1} \tag{15}
$$

$$
\hat{x}_k = \hat{x}_k^- + K_k(z_k - H\hat{x}_k^-) \tag{16}
$$

$$
P_k = (I - K_kH)P_k^- \tag{17}
$$
where:
- $K_k$ is the `gain` from time step $k$;
- $z_k$ is the measurement variable from time step $k$;
- $\hat{x}_k$ is the `posteriori` state from time step $k$;
- $P_k$ is the `posteriori` estimate error covariance from time step $k$.

## Filter prameters and tunning
In the actual implementation of the filter, the measurement noise covariance $R$ is usually measured prior to operation of the filter. Measuring the measurement error covariance $R$ is generally practical (possible) because we need to be able to measure the process anyway (while operating the filter) so we should generally be able to take some off-line sample measurements in order to determine the variance of the measurement noise.

The determination of the process noise covariance $Q$ is generally more difficult as we typically do not have the ability to directly observe the process we are estimating. Sometimes a relatively simple (poor) process model can produce acceptable results if one “injects” enough uncertainty into the process via the selection of $Q$. Certainly in this case one would hope that the process measurements are reliable.

In either case, whether or not we have a rational basis for choosing the parameters, often times superior filter performance (statistically speaking) can be obtained by `tuning` the filter parameters $Q$ and $R$. The tuning is usually performed off-line, frequently with the help of another (distinct) Kalman filter in a process generally referred to as `system identification`.

# Dynamic model
The motion of a target object(pedestrian or vehicle) can be modeled as:
- Moving with constant speed(CV) in straight;
- Moving with constant acceleration(CA) in straight;
- Moving with constant turn(CT).

## CV model
For this model, the states under consideration are:
$$
X = \begin{bmatrix} x \\\\ \dot{x} \\\\ y \\\\ \dot{y} \end{bmatrix}
$$

where:
- $x$ is the position in longitudinal component;
- $y$ is the position in lateral component;
- $\dot{x}$ is the velocity in x-direction;
- $\dot{y}$ is the velocity in y-direction;

For this model, state transition matrix is:
$$
A_{CV} = 
\begin{bmatrix} 
1 & dt & 0 & 0 \\\\
0 & 1 & 0 & 0 \\\\
0 & 0 & 1 & dt \\\\
0 & 0 & 0 & 1
\end{bmatrix}
$$

## CA model
For this model, the states under consideration are:
$$
X = \begin{bmatrix} 
x \\\\
\dot{x} \\\\
\ddot{x} \\\\
y \\\\
\dot{y} \\\\
\ddot{y} 
\end{bmatrix}
$$

where:
- $x$ is the position in longitudinal component;
- $y$ is the position in lateral component;
- $\dot{x}$ is the velocity in x-direction;
- $\dot{y}$ is the velocity in y-direction;
- $\ddot{x}$ is the acceleration in x-direction;
- $\ddot{y}$ is the acceleration in y-direction;

For this model, state transition matrix is:
$$
A_{CA} = 
\begin{bmatrix} 
1 & dt & \frac{dt^2}{2} & 0 & 0 & 0 \\\\
0 & 1 & dt & 0 & 0 & 0 \\\\
0 & 0 & 1 & 0 & 0 & 0 \\\\
0 & 0 & 0 & 1 & dt & \frac{dt^2}{2} \\\\
0 & 0 & 0 & 0 & 1 & dt \\\\
0 & 0 & 0 & 0 & 0 & 1
\end{bmatrix}
$$

## CT model
For this model, the states under consideration are:
$$
X = \begin{bmatrix} 
x \\\\
\dot{x} \\\\
y \\\\
\dot{y} \\\\
\dot{\theta} \\\\
\end{bmatrix}
$$

where:
- $x$ is the position in longitudinal component;
- $y$ is the position in lateral component;
- $\dot{x}$ is the velocity in x-direction;
- $\dot{y}$ is the velocity in y-direction;
- $\dot{\theta}$ is the yawrate of obstacle;

For this model, state transition matrix is:
$$
A_{CT} = 
\begin{bmatrix} 
1 & \frac{sin(\dot{\theta} * dt)}{\dot{\theta}}& 0 & -\frac{1-cos(\dot{\theta} * dt)}{\dot{\theta}}& 0 \\\\
0 & cos(\dot{\theta} * dt)& 0 & -sin(\dot{\theta} * dt)& 0 \\\\
0 & \frac{1-cos(\dot{\theta} * dt)}{\dot{\theta}} & 1 & \frac{sin(\dot{\theta} * dt)}{\dot{\theta}}& 0 \\\\
0 & sin(\dot{\theta} * dt)& 0 & cos(\dot{\theta} * dt)& 0 \\\\
0 & 0 & 0 & 0 & 1
\end{bmatrix}
$$

## Simulation for kalman filter
To check if the algorithm is correct, we build the equation of kalman in python.

### Kalman filter
```python
class kalman_filter:
    def __init__(self, A, B, H, Q, R):
        self.A = A
        self.B = B
        self.H = H
        self.Q = Q
        self.R = R

        self.U = np.zeros((B.shape[0], 1))
        self.X = np.zeros((A.shape[0], 1))
        self.X_pre = self.X
        self.P = np.zeros(A.shape)
        self.P_pre = self.P

    def filt(self, Z):
        self.__predict()
        self.__update(Z)
        return self.X

    def __predict(self):
        self.X_pre = np.dot(self.A, self.X) + np.dot(self.B, self.U)
        self.P_pre = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q

    def __update(self, Z):
        K = np.dot(np.dot(self.P_pre, self.H.T),
                   np.linalg.inv(np.dot(np.dot(self.H, self.P_pre), self.H.T) +\
                                 self.R))
        self.X = self.X_pre + np.dot(K, Z - np.dot(self.H, self.X_pre))
        self.P = self.P_pre - np.dot(np.dot(K, self.H), self.P_pre)
```

### Constant velocity model
```python
def kf_cv():
    A = np.array([
            [1., dt, 0., 0.],
            [0., 1., 0., 0.],
            [0., 0., 1., dt],
            [0., 0., 0., 1.]
            ])
    B = np.eye(A.shape[0])
    H = np.array([
        [1., 0., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 1., 0.],
        [0., 0., 0., 1.]
        ])
    Q = np.eye(A.shape[0])
    R = np.eye(4) * 10. ** 2

    kf = kalman_filter(A, B, H, Q, R)
    return kf
```
The simulation result:
![cv](/images/2020/imm/cv.png)

### Constant acceleration model
```python
def kf_ca():
    A = np.array([
            [1., dt, 0.5 * dt**2, 0., 0., 0.],
            [0., 1., dt, 0., 0., 0.],
            [0., 0., 1., 0., 0., 0.],
            [0., 0., 0., 1., dt, 0.5 * dt**2],
            [0., 0., 0., 0., 1., dt],
            [0., 0., 1., 0., 0., 1.]
            ])
    B = np.eye(A.shape[0])
    H = np.array([
        [1., 0., 0., 0., 0., 0.],
        [0., 1., 0., 0., 0., 0.],
        [0., 0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 1., 0.]
        ])
    Q = np.eye(A.shape[0])
    R = np.eye(4) * 150

    kf = kalman_filter(A, B, H, Q, R)
    return kf
```
The simulation result:
![ca](/images/2020/imm/ca.png)

# Interacting multiple model
The IMM estimator was originally proposed by Bloom in [An efficient filter for abruptly changing systems](https://ieeexplore.ieee.org/document/4047965). It is one of the most cost-effective class of estimators for a single maneuvering target. The IMM has been receiving special attention in the last few years, due to its capability of being combined with other algorithms to resolve the multiple target tracking problem.

The main idea of imm is the identification and transition between different models: at every tracking moment, by setting weight-coefficient and probability for each filter, and finally weighting calculation, we obtain the current optimal estimation state.

![pic]()

Assume that we have $r$ models, each model's state equation:
$$
X_{k+1} = A^jX_{k} + w^j_{k}
$$
where
- $j \in [1, r]$, $X$ is state vector,
- $A_j$ is transition matrix,
- $w$ is noise with the variance of $Q$.

The measurement equation is:
$$
Z_{k} = H^jX_{k} + v^j_k
$$
where 
- $Z$ is measurement vector,
- $H$ is measurement matrix,
- $v$ is the noise with the variance of $R$.

The transition matrix between models can be:
P = 
\begin{bmatrix} 
p_{11} & \cdots & p_{1r} \\\\
\rdots & \cdots & \rdots \\\\
p_{r1} & \cdots & p_{rr}
\end{bmatrix}
$$

and probability vector of each model is:
$$
U = \begin{bmatrix} u_1 & \cdots & u_{r} \end{bmatrix}
$$

## Step1: Input mix
$$
X^{0j}\_{k-1|k-1} = \sum_{i=1}^{r}{X^j_{k-1|k-1}u^{ij}\_{k-1|k-1}}
$$
$$
P^{0j}\_{k-1|k-1} = \sum_{i=1}^{r}{u^ij_{k-1|k-1}\[P^j_{k-1|k-1} + (X^j_{k-1|k-1}) - X^{0j}\_{k-1|k-1}\]\[P^j_{k-1|k-1} + (X^j_{k-1|k-1}) - X^{0j}\_{k-1|k-1}\]^T}
$$

where
- $X^j_{k-1|k-1}$ is the optimal state estimate,
- $P^j_{k-1|k-1}$ is the optimal state estimate;

$$
u^{ij}\_{k-1|k-1} = \frac{p_{ij}U^j_{k-1}}{C^j}
$$ 
and
$$
C^j = \sum_{i=1}^r{p_ijU^j_{k-1}}
$$

## Step2: Model estimate
It's the same as normal kalman filter.

## Step3: Probability update

## Simulation for imm

# Cpp class diagram
