import numpy as np
from numpy import sqrt, abs, cos, sin

def T_matrix(lam, d, eps):
    """Calculate a single matrix"""
    n = sqrt((abs(eps) + eps.real)/2) + 1j*sqrt((abs(eps) - eps.real)/2)
    k = 2*np.pi / lam * n

    T = np.array([
        [cos(k*d), 1j/n*sin(k*d)],
        [1j*n*sin(k*d), cos(k*d)],
    ])
    return T

def total_matrix(lam, layers):
    T = np.identity(2)
    
    for layer in layers:
        d = layer[0]
        eps = layer[1]
        T = np.matmul(T_matrix(lam, d, eps), T)
    
    return T

def r(T):
    T11, T12, T21, T22 = T[0,0], T[0,1], T[1,0], T[1,1]
    r = (T12 + (T11-T22) - T21) / (T12 - (T11+T22) + T21)
    return r

def t(T):
    T11, T12, T21, T22 = T[0,0], T[0,1], T[1,0], T[1,1]
    t = -2 / (T12 - (T11+T22) + T21)
    return t