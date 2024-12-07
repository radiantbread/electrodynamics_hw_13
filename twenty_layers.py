import lib
import numpy as np
from matplotlib import pyplot as plt

eps1 = 4 + 0.05j
eps2 = 16 + 0.1j
d1 = 100
d2 = 50

wavelengths = np.linspace(500, 1200, 1000)

layers = [(d1, eps1), (d2, eps2)] * 10

left_matrices = [lib.total_matrix(lam, layers) for lam in wavelengths]
right_matrices = [lib.total_matrix(lam, reversed(layers)) for lam in wavelengths]

# Left coefficients.
r_l = np.array([lib.r(matrix) for matrix in left_matrices])
t_l = np.array([lib.t(matrix) for matrix in left_matrices])
R_l = abs(r_l)**2
T_l = abs(t_l)**2

plt.plot(wavelengths, R_l, label=r"$R_l$", color="teal")
plt.plot(wavelengths, T_l, label=r"$T_l$", color="cyan")

plt.xlabel(r"Wavelength $\lambda$, nm")
plt.ylabel(r"Squares of the absolute values of $r$ and $t$")

plt.legend()
plt.savefig("twenty_layers.png")