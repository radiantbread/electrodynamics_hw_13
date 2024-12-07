import lib
import numpy as np
from matplotlib import pyplot as plt

eps1 = 4 + 0.05j
eps2 = 16 + 0.1j
d1 = 100
d2 = 50

wavelengths = np.linspace(150, 500, 1000)

layers = [(d1, eps1), (d2, eps2)]
left_matrices = [lib.total_matrix(lam, layers) for lam in wavelengths]
right_matrices = [lib.total_matrix(lam, reversed(layers)) for lam in wavelengths]

# Left coefficients.
r_l = np.array([lib.r(matrix) for matrix in left_matrices])
t_l = np.array([lib.t(matrix) for matrix in left_matrices])
R_l = abs(r_l)**2
T_l = abs(t_l)**2

# Right coefficients.
r_r = np.array([lib.r(matrix) for matrix in right_matrices])
t_r = np.array([lib.t(matrix) for matrix in right_matrices])
R_r = abs(r_r)**2
T_r = abs(t_r)**2

plt.plot(wavelengths, R_l, label=r"$R_l$", color="teal")
plt.plot(wavelengths, T_l, label=r"$T_l$", color="cyan")
plt.plot(wavelengths, R_r, label=r"$R_r$", color="mediumorchid")
plt.plot(wavelengths, T_r, label=r"$T_r$", color="deeppink")

plt.xlabel(r"Wavelength $\lambda$, nm")
plt.ylabel(r"Squares of the absolute values of $r$ and $t$")

plt.legend()
plt.savefig("two_layers.png")