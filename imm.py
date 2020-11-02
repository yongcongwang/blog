#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# By yongcong.wang @ 13/10/2020

import math
import numpy as np

import matplotlib.pyplot as plt

np.seterr(divide='ignore',invalid='ignore')

# step
dt = 0.1

def add_noise(Z, gain):
    noise_z = []
    for z in Z:
        copy_z = np.copy(z)
        for ele in copy_z:
            ele += gain * np.random.randn(1)[0]
        noise_z.append(copy_z)

    return noise_z

def get_xdx_ydy(std_z, noise_z):
    std = [[], [], [], []]
    for z in std_z:
        std[0].append(z[0, 0])
        std[1].append(z[1, 0])
        std[2].append(z[2, 0])
        std[3].append(z[3, 0])
    noise = [[], [], [], []]
    for z in noise_z:
        noise[0].append(z[0, 0])
        noise[1].append(z[1, 0])
        noise[2].append(z[2, 0])
        noise[3].append(z[3, 0])
    return std, noise

def get_error_pos_spd(std, noise, filt):
    error_pos = [[], []]
    error_spd = [[], []]
    for i in range(len(std[0])):
        error_pos[0].append(math.hypot(std[0][i] - noise[0][i],
                                       std[2][i] - noise[2][i]))
        error_pos[1].append(math.hypot(std[0][i] - filt[0][i],
                                       std[2][i] - filt[2][i]))
        error_spd[0].append(math.hypot(std[1][i] - noise[1][i],
                                       std[3][i] - noise[3][i]))
        error_spd[1].append(math.hypot(std[1][i] - filt[1][i],
                                       std[3][i] - filt[3][i]))

    return error_pos, error_spd

def plot_cx(std, noise, filt):
    # error
    error_pos, error_spd = get_error_pos_spd(std, noise, filt)

    # plot
    fig = plt.figure(1)

    pos_plt = fig.add_subplot(221)
    pos_plt.plot(std[0], std[2], color='r', label='standard')
    pos_plt.plot(noise[0], noise[2], color='b', label='noised')
    pos_plt.plot(filt[0], filt[2], color='g', label='filted')
    pos_plt.legend()
    pos_plt.title.set_text("position")

    spd_plt = fig.add_subplot(222)
    spd_plt.plot(std[1], std[3], color='r', label='standard')
    spd_plt.plot(noise[1], noise[3], color='b', label='noised')
    spd_plt.plot(filt[1], filt[3], color='g', label='filted')
    spd_plt.legend()
    spd_plt.title.set_text("speed")

    error_pos_plt = fig.add_subplot(223)
    t = np.arange(0, len(error_pos[0]))
    error_pos_plt.plot(t, error_pos[0], color='r', label='noise')
    error_pos_plt.plot(t, error_pos[1], color='b', label='filted')
    error_pos_plt.legend()
    error_pos_plt.title.set_text("position error")

    error_spd_plt = fig.add_subplot(224)
    t = np.arange(0, len(error_spd[0]))
    error_spd_plt.plot(t, error_spd[0], color='r', label='noise')
    error_spd_plt.plot(t, error_spd[1], color='b', label='filted')
    error_spd_plt.legend()
    error_spd_plt.title.set_text("speed error")

    plt.show()
    plt.close()

class kalman_filter:
    def __init__(self, A, B, H, Q, R):
        self.A = A
        self.B = B
        self.H = H
        self.Q = Q
        self.R = R

        self.U = np.zeros((B.shape[1], 1))
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

def get_cv_z(x0, dx, y0, dy, pt_cnt):
    Z = [np.array([[x0], [dx], [y0], [dy]])]
    for i in np.arange(1, pt_cnt):
        x0 = Z[i-1][0, 0]
        dx = Z[i-1][1, 0]
        y0 = Z[i-1][2, 0]
        dy = Z[i-1][3, 0]
        Z.append(np.array([[x0 + dx * dt],
                           [dx],
                           [y0 + dy * dt],
                           [dy]
                           ]))
    return Z

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

def test_cv():
    # start up
    std_z = get_cv_z(5., 1., 5., 1.5, 1500)
    noise_z = add_noise(std_z, 0.1)
    kf = kf_cv()
    kf.X = noise_z[0]

    # filt
    filt_x = []
    for z in noise_z:
        x = kf.filt(z)
        filt_x.append(x)

    # extract
    std, noise = get_xdx_ydy(std_z, noise_z)

    filt = [[], [], [], []]
    for x in filt_x:
        filt[0].append(x[0, 0])
        filt[1].append(x[1, 0])
        filt[2].append(x[2, 0])
        filt[3].append(x[3, 0])

    plot_cx(std, noise, filt)
#test_cv()

def get_ca_z(x0, dx, ddx, y0, dy, ddy, pt_cnt):
    Z = [np.array([[x0], [dx], [y0], [dy]])]
    for i in np.arange(1, pt_cnt):
        x0 = Z[i-1][0, 0]
        dx = Z[i-1][1, 0]
        y0 = Z[i-1][2, 0]
        dy = Z[i-1][3, 0]
        Z.append(np.array([[x0 + dx * dt + 0.5 * ddx * dt**2],
                           [dx + ddx * dt],
                           [y0 + dy * dt + 0.5 * ddy * dt**2],
                           [dy + ddy * dt]
                           ]))
    return Z

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

def test_ca():
    # start up
    std_z = get_ca_z(0., 1., 0.5, 0., 2, 1.5, 1500)
    noise_z = add_noise(std_z, 1.)
    kf = kf_ca()
    z0 = noise_z[0]
    kf.X = np.array([
        [z0[0, 0]],
        [z0[1, 0]],
        [0.],
        [z0[2, 0]],
        [z0[3, 0]],
        [0.]
        ])

    # filt
    filt_x = []
    for z in noise_z:
        x = kf.filt(z)
        filt_x.append(x)

    # extract
    std, noise = get_xdx_ydy(std_z, noise_z)

    filt = [[], [], [], []]
    for x in filt_x:
        filt[0].append(x[0, 0])
        filt[1].append(x[1, 0])
        filt[2].append(x[3, 0])
        filt[3].append(x[4, 0])

    plot_cx(std, noise, filt)
test_ca();

#class imm:
#    def __init__(self, modes, P_trans, U_prob):
#        self.modes = modes
#        self.P_trans = P_trans # 3 * 3
#        self.U_prob = U_prob # 1 * 3
#
#        self.mode_cnt = len(modes)
#        self.dim = modes[0].A.shape[0]
#
#    def filt(self, Z):
#        # setp1: input mix
#        U = np.array([self.U_prob, self.U_prob, self.U_prob])
#        tr = np.dot(U, self.P_trans) # 3 * 3
#        mu = tr / np.sum(tr)
#
#        X_mix = [np.zeros(x.X.shape) for x in self.modes]
#
#        for j in range(self.mode_cnt):
#            for i in range(self.mode_cnt):
#                X_mix[j] += self.modes[j].X * mu[i, j]
#
#        P_mix = [np.zeros(self.modes[0].P.shape)] * 3
#        for j in range(self.mode_cnt):
#            for i in range(self.mode_cnt):
#                P_mix[j] += mu[i, j] * (self.modes[j].P + np.dot(
#                      self.modes[j].X - X_mix[j], (self.modes[j].X - X_mix[j]).T))
#
#        ## step2: filt
#        for j in range(self.mode_cnt):
#            self.modes[j].X = X_mix[j]
#            self.modes[j].P = P_mix[j]
#            self.modes[j].filt(Z)
#
#        ### step3: update probability
#        for j in range(self.mode_cnt):
#            mode = self.modes[j]
#            S = np.dot(np.dot(mode.H, mode.P_pre), mode.H.T) + mode.R
#            D = Z - np.dot(mode.H, mode.X_pre)
#
#            Lambda = (2 * math.pi * abs(np.linalg.det(S))) ** (-0.5) * \
#                     np.exp(-0.5 * np.dot(np.dot(D.T, np.linalg.inv(S)), D))
#            self.U_prob[j] *= Lambda
#        self.U_prob = self.U_prob / np.sum(self.U_prob)
#
#        ### step4: merge
#        X = np.zeros(self.modes[j].X.shape)
#        for j in range(self.mode_cnt):
#            X += self.modes[j].X * self.U_prob[j]
#        return X
#
#def add_noise(Z, gain):
#    noise_z = []
#    for z in Z:
#        copy_z = np.copy(z)
#        for ele in copy_z:
#            ele += gain * np.random.randn(1)[0]
#        noise_z.append(copy_z)
#
#    return noise_z
#
#def ca_z(x0, y0, v, a, theta):
#    Z = [np.array([[x0], [y0]])]
#    k_x = math.cos(theta)
#    k_y = math.sin(theta)
#    for i in np.arange(1, iter_cnt):
#        last = Z[i - 1]
#        Z.append(np.array(
#            [[last[0, 0] + v * dt * k_x + 0.5 * a * dt**2 * k_x],
#             [last[1, 0] + v * dt * k_y + 0.5 * a * dt**2 * k_y]]))
#    return Z
#
#def ct_z(x0, y0, v, theta, dtheta):
#    Z = [np.array([[x0], [y0]])]
#    for i in np.arange(1, iter_cnt):
#        last = Z[i - 1]
#        theta += dtheta
#        Z.append(np.array([[last[0, 0] + v * dt * math.cos(theta)],
#                           [last[1, 0] + v * dt * math.sin(theta)]]))
#    return Z
#
#def plot_result(std_z, noise_z, filt_z, probs):
#    std_xy = [[], []]
#    for z in std_z:
#        std_xy[0].append(z[0, 0])
#        std_xy[1].append(z[1, 0])
#    noise_xy = [[], []]
#    for z in noise_z:
#        noise_xy[0].append(z[0, 0])
#        noise_xy[1].append(z[1, 0])
#    filt_xy = [[], []]
#    for z in filt_z:
#        filt_xy[0].append(z[0, 0])
#        filt_xy[1].append(z[1, 0])
#    #print(filt_xy)
#
#    prob_cx = [[], [], []]
#    for p in probs:
#        prob_cx[0].append(p[0])
#        prob_cx[1].append(p[1])
#        prob_cx[2].append(p[2])
#
#    plt.figure(1)
#
#    plt.subplot(211)
#    plt.plot(std_xy[0], std_xy[1], color='r', label='standard')
#    plt.plot(noise_xy[0], noise_xy[1], color='b', label='noised')
#    plt.plot(filt_xy[0], filt_xy[1], color='g', label='filted')
#    plt.legend()
#
#    plt.subplot(212)
#    t = np.arange(0, len(probs))
#    plt.plot(t, prob_cx[0], color='r', label='cv')
#    plt.plot(t, prob_cx[1], color='b', label='ca')
#    plt.plot(t, prob_cx[2], color='g', label='ct')
#    plt.legend()
#
#    plt.show()
#    plt.close()
#
#
#
#def kf_cv(X, Z):
#    A = np.array(
#        [[1, 0, dt, 0, 0, 0],
#         [0, 1, 0, dt, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0]])
#    B = np.eye(X.shape[0])
#    U = np.zeros((X.shape[0], 1))
#    H = np.array([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]])
#    Q = np.eye(X.shape[0]) * 1
#    R = np.eye(Z.shape[0]) * 10000
#
#    P = np.eye(X.shape[0]) 
#
#    return A, B, U, H, Q, R, P
#
#def conf_cv():
#    std_z = curve_cv(0., 0., 1., 45. / 180. * 3.14)
#    noise_z = add_noise(std_z, 0.1)
#    Z0 = noise_z[0]
#    X0 = np.array([[Z0[0, 0]],
#                   [Z0[1, 0]],
#                   [0.1],
#                   [0.1],
#                   [0.],
#                   [0.]])
#
#    A, B, U, H, Q, R, P = kf_cv(X0, Z0)
#    kf = kalman_filter(A, B, U, H, Q, R, X0, P)
#    filted_z = [X0]
#
#    return std_z, noise_z, filted_z, kf
#
#def test_cv():
#    std_z, noise_z, filted_z, ft = conf_cv()
#    for z in noise_z:
#        x = ft.filt(z)
#        filted_z.append(x)
#    plot_cx(std_z, noise_z, filted_z)
#    print(ft.P)
#
#test_cv()
#
#def ct_kf(X, Z):
#    omega = 10
#    theta = omega * dt
#    A = np.array(
#        [[1, 0, math.sin(theta) / omega, -(1 - math.cos(theta)) / omega, 0, 0],
#         [0, 1, (1 - math.cos(theta)) / omega, math.sin(theta) / omega, 0, 0],
#         [0, 0, math.cos(theta), -math.sin(theta), 0, 0],
#         [0, 0, math.sin(theta), math.cos(theta), 0, 0],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 0, 0, 0, 1]])
#    B = np.eye(X.shape[0])
#    U = np.zeros((X.shape[0], 1))
#    H = np.array([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]])
#    Q = np.eye(X.shape[0])
#    R = np.eye(Z.shape[0])
#
#    P = np.diag((0.01, 0.01, 0.01, 0.01, 0.01, 0.01))
#    return A, B, U, H, Q, R, P
#
#def ca_kf(X, Z):
#    A = np.array(
#        [[1, 0, dt, 0, 0.5 * dt ** 2, 0], 
#         [0, 1, 0, dt, 0, 0.5 * dt ** 2],
#         [0, 0, 1, 0, dt, 0],
#         [0, 0, 0, 1, 0, dt],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 0, 0, 0, 1]])
#    B = np.eye(X.shape[0])
#    U = np.zeros((X.shape[0], 1))
#    H = np.array([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]])
#    Q = np.eye(X.shape[0])
#    R = np.eye(Z.shape[0])
#
#    P = np.diag((0.01, 0.01, 0.01, 0.01, 0.01, 0.01))
#    return A, B, U, H, Q, R, P
#
#def test_ca():
#    std_z = ca_z(0., 0., 1., 0.5, 45. / 180. * 3.14)
#    noise_z = add_noise(std_z, 0.2 * dt)
#    Z0 = noise_z[0]
#    X0 = np.array([[Z0[0, 0]],
#                   [Z0[1, 0]],
#                   [0.1],
#                   [0.1],
#                   [0.],
#                   [0.]])
#
#    A, B, U, H, Q, R, P = ca_kf(X0, Z0)
#    kf = kalman_filter(A, B, U, H, Q, R, X0, P)
#    filted_z = [X0]
#
#    return std_z, noise_z, filted_z, kf
#
#def test_ct():
#    std_z = ct_z(0., 0., 1., 45. / 180. * 3.14, 0.1)
#    noise_z = add_noise(std_z, 0.2 * dt)
#    Z0 = noise_z[0]
#    X0 = np.array([[Z0[0, 0]],
#                   [Z0[1, 0]],
#                   [0.1],
#                   [0.1],
#                   [0.0],
#                   [0.0]])
#
#    A, B, U, H, Q, R, P = ct_kf(X0, Z0)
#    kf = kalman_filter(A, B, U, H, Q, R, X0, P)
#    filted_z = [X0]
#
#    return std_z, noise_z, filted_z, kf
#
#def z_cv_ca_ct(x0, y0, theta, v, a, dtheta):
#    Z = [np.array([[x0], [y0]])]
#
#    Z_last = Z[-1]
#    del Z[-1]
#    Z += cv_z(x0, y0, v, theta)
#
#    Z_last = Z[-1]
#    del Z[-1]
#    Z += ca_z(x0, y0, v, a, theta)
#
#    Z_last = Z[-1]
#    del Z[-1]
#    Z += ct_z(Z[-1][0, 0], Z[-1][1, 0], v, theta, dtheta)
#
#    return Z
#
#def conf_imm():
#    std_z = z_cv_ca_ct(0., 0., 45. / 180. * math.pi, 1., 0.5, 0.1)
#    noise_z = add_noise(std_z, 0.1 * dt)
#    Z0 = noise_z[0]
#    X0 = np.array([[Z0[0, 0]],
#                   [Z0[1, 0]],
#                   [0.1],
#                   [0.1],
#                   [0.0],
#                   [0.0]])
#
#    _, _, _, cv_kf = test_cv()
#    _, _, _, ca_kf = test_ca()
#    _, _, _, ct_kf = test_ct()
#    modes = [cv_kf, ca_kf, ct_kf]
#
#    P_trans = np.array([
#        [0.33, 0.33, 0.33],
#        [0.33, 0.33, 0.33],
#        [0.33, 0.33, 0.33]
#    ])
#    U_prob = np.array([0.33, 0.33, 0.33])
#
#
#    ft = imm(modes, P_trans, U_prob)
#    filted_z = [X0]
#
#    return std_z, noise_z, filted_z, ft
#
#def test_imm():
#    std_z, noise_z, filted_z, ft = conf_imm()
#    probs = [np.copy(ft.U_prob)]
#    for z in noise_z:
#        z = ft.filt(z)
#        filted_z.append(z)
#        probs.append(np.copy(ft.U_prob))
#
#    plot_result(std_z, noise_z, filted_z, probs)
