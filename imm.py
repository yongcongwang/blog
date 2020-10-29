#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# By yongcong.wang @ 29/10/2020
import math
import numpy as np

import matplotlib.pyplot as plt

dt = 0.1

class kalman_filter:
    def __init__(self, A, B, U, H, Q, R):
        self.A = A
        self.B = B
        self.U = U
        self.H = H
        self.Q = Q
        self.R = R

        self.X = np.zeros((A.shape[0], 1))
        self.X_pre = self.X
        self.P = np.eye(A.shape[0]) * 0.01
        self.P_pre = self.P

    def filt(self, Z):
        self.__predict()
        self.__update(Z)
        return self.X

    def __predict(self):
        self.X_pre = np.dot(self.A, self.X) + np.dot(self.B, self.U)
        self.P_pre = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q

    def __update(self, Z):
        K = np.dot(np.dot(self.P_pre, self.H.T), np.linalg.inv(np.dot(np.dot(self.H, self.P_pre), self.H.T) + self.R))
        self.X = self.X_pre + np.dot(K, Z - np.dot(self.H, self.X_pre))
        self.P = self.P_pre - np.dot(np.dot(K, self.H), self.P_pre)
        
def plot_imm(std_z, noise_z, filt_z, probs):
    std_xy = [[], []]
    for z in std_z:
        std_xy[0].append(z[0, 0])
        std_xy[1].append(z[1, 0])
    noise_xy = [[], []]
    for z in noise_z:
        noise_xy[0].append(z[0, 0])
        noise_xy[1].append(z[1, 0])
        
    error = []
    for i in range(len(std_z)):
        std_x = std_z[i][0, 0]
        std_y = std_z[i][1, 0]
        filt_x = filt_z[0][i]
        filt_y = filt_z[1][i]
        error.append(math.hypot(std_x - filt_x, std_y - filt_y))

    prob_cx = [[], [], []]
    for p in probs:
        prob_cx[0].append(p[0])
        prob_cx[1].append(p[1])
        prob_cx[2].append(p[2])
        
    plt.rcParams['figure.figsize'] = (20.0, 20.0)
    plt.figure(1)

    plt.subplot(221)
    plt.plot(std_xy[0], std_xy[1], color='r', label='standard')
    plt.plot(noise_xy[0], noise_xy[1], color='b', label='noised')
    plt.plot(filt_z[0], filt_z[1], color='g', label='filted')
    plt.legend()

    plt.subplot(223)
    t = np.arange(0, len(error))
    plt.plot(t, error, color='r', label='error')
    plt.legend()
    
    plt.subplot(222)
    t = np.arange(0, len(probs))
    plt.plot(t, prob_cx[0], color='r', label='prob_cv')
    plt.plot(t, prob_cx[1], color='b', label='prob_ca')
    plt.plot(t, prob_cx[2], color='g', label='prob_ct')
    plt.legend()

    plt.show()
    plt.close()

def plot_cx(std_z, noise_z, filt_z):
    std_xy = [[], []]
    for z in std_z:
        std_xy[0].append(z[0, 0])
        std_xy[1].append(z[1, 0])
    noise_xy = [[], []]
    for z in noise_z:
        noise_xy[0].append(z[0, 0])
        noise_xy[1].append(z[1, 0])
        
    error = []
    for i in range(len(std_z)):
        std_x = std_z[i][0, 0]
        std_y = std_z[i][1, 0]
        filt_x = filt_z[0][i]
        filt_y = filt_z[1][i]
        error.append(math.hypot(std_x - filt_x, std_y - filt_y))

    plt.rcParams['figure.figsize'] = (20.0, 20.0)
    plt.figure(1)

    plt.subplot(121)
    plt.plot(std_xy[0], std_xy[1], color='r', label='standard')
    plt.plot(noise_xy[0], noise_xy[1], color='b', label='noised')
    plt.plot(filt_z[0], filt_z[1], color='g', label='filted')
    plt.legend()

    plt.subplot(122)
    t = np.arange(0, len(error))
    plt.plot(t, error, color='r', label='error')
    plt.legend()
    
    plt.show()
    plt.close()

def generate_ca_curve(x0, y0, v_x, v_y, a_x, a_y, size):
    Z = [np.array([[x0], [y0], [v_x], [v_y], [a_x], [a_y]])]
    for i in np.arange(1, size):
        v_x = a_x * dt
        v_y = a_y * dt
        Z.append(np.array([[Z[i - 1][0, 0] + v_x * dt + 0.5 * a_x * dt**2],
                           [Z[i - 1][1, 0] + v_y * dt + 0.5 * a_x * dt**2],
                           [v_x],
                           [v_y],
                           [a_x],
                           [a_y]
                           ]))
        
    return Z

def generate_ct_curve(x0, y0, v_x, v_y, omega, size):
    Z = [np.array([[x0], [y0], [v_x], [v_y], [0.], [0.]])]
    theta = math.tan(v_y/v_x)
    v = math.hypot(v_x, v_y)
    for i in np.arange(1, size):
        theta += omega * dt
        Z.append(np.array([[Z[i - 1][0, 0] + v * dt * math.cos(theta)],
                           [Z[i - 1][1, 0] + v * dt * math.sin(theta)],
                           [v * math.cos(theta)],
                           [v * math.sin(theta)],
                           [0.],
                           [0.]
                           ]))
    return Z

def add_noise(Z, gain):
    noise_z = []
    for z in Z:
        copy_z = np.copy(z)
        for ele in copy_z:
            ele += gain * np.random.randn(1)[0]
        noise_z.append(copy_z)

    return noise_z

def generate_cv_curve(x0, y0, v_x, v_y, size):
    Z = [np.array([[x0], [y0], [v_x], [v_y], [0.], [0.]])]
    for i in np.arange(1, size):
        Z.append(np.array([[Z[i - 1][0, 0] + v_x *  dt],
                           [Z[i - 1][1, 0] + v_y * dt],
                           [v_x],
                           [v_y],
                           [0.],
                           [0.]]))
    return Z

def cv_conf():
    A = np.array([[1., dt, 0., 0.],
                  [0., 1., 0., 0.],
                  [0., 0., 1., dt],
                  [0., 0., 0., 0.]])
    B = np.eye(A.shape[0])
    U = np.zeros((A.shape[0], 1))
    H = np.array([[1., 0., 0., 0.],
                  [0., 1., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 1., 0.],
                  [0., 0., 0., 1.],
                  [0., 0., 0., 0.]])
    R = np.eye(H.shape[0])
    Q = np.eye(A.shape[0])

    return A, B, U, H, Q, R

def test_cv():
    std_z = generate_cv_curve(0., 0., 5, 3, 100)
    noise_z = add_noise(std_z, 0.5*dt)
    A, B, U, H, Q, R = cv_conf()
    cv_kf = kalman_filter(A, B, U, H, Q, R)

    filt_z = [[],[]]
    for z in noise_z:
        x = cv_kf.filt(z)
        filt_z[0].append(x[0, 0])
        filt_z[1].append(x[2, 0])
        
    plot_cx(std_z, noise_z, filt_z)

test_cv()
