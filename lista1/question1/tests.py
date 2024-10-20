import numpy as np

# Testando a multiplicação por escalar

beta = [4, 3]
beta_abs = np.linalg.norm(beta)
print(beta_abs)

v = []
v.append(np.array([1 + 2j, 0, 2j], dtype="complex128"))

scalar_mult = beta_abs * v[0]
print(scalar_mult)

# Testando a criação de um vetor nulo

nulo = np.zeros(3, dtype="complex128")
print(nulo)

nulo = np.array([0 + 0j, 0 + 0j, 0 + 0j], dtype="complex128")
print(nulo)
