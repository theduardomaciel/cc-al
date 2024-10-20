import numpy as np

v = []
v.append(np.array([1, 1j, 1], dtype="complex128"))
v.append(np.array([4, 3, 2], dtype="complex128"))
v.append(np.array([2 + 3j, complex(np.sqrt(3), np.pi), 3], dtype="complex128"))
v.append(
    np.array(
        [complex(np.cos(np.pi / 2), np.sin(np.pi / 2)), 1, complex(np.exp(-2), 0)],
        dtype="complex128",
    )
)

beta = []
beta.append(3 + 4j)
beta.append(np.exp(-np.pi / 2) + 0j)
beta.append(-12345 + 28413j)

# Testando a multiplicação por escalar

beta_abs = np.linalg.norm(beta[0])
print(beta_abs)

v_2 = []
v_2.append(np.array([1 + 2j, 0, 2j], dtype="complex128"))

scalar_mult = beta_abs * v_2[0]
print(scalar_mult)

# Testando a criação de um vetor nulo

nulo = np.zeros(3, dtype="complex128")
print(nulo)

nulo = np.array([0 + 0j, 0 + 0j, 0 + 0j], dtype="complex128")
print(nulo)

print("Testando o cálculo do vetor inverso")

v_3 = np.array([5 + 12j, 0 + 0j, 0 + 0j], dtype="complex128")

inverso = np.reciprocal(v_3)
print(inverso)

inverso = np.conj(v_3) / np.linalg.norm(v_3) ** 2
print(inverso)

inverso = 1 / v_3
print(inverso)

inverso = np.conj(v_3) / (np.abs(v_3) ** 2)
print(inverso)
