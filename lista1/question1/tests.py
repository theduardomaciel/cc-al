import numpy as np

u = np.array([1 + 2j, 0, 4j], dtype="complex128")
v = np.array([4j, -2, 6], dtype="complex128")

v2 = np.array([1 + 2j, 0, 2j], dtype="complex128")

beta = 4 + 3j

# Testando a soma de vetores
print("Testando a soma de vetores ===================")

print("Vetor 1:", u)
print("Vetor 2:", v)

soma = u + v  # 1
print("Soma:", soma)

soma = np.add(u, v)  # 2
print("Soma:", soma)

# Testando a multiplicação por escalar
print("Testando a multiplicação por escalar ===================")

beta = beta
print("Beta:", beta)

beta_norm = np.linalg.norm(beta)
print("Norma de beta:", beta_norm)

beta_norm = np.abs(beta)
print("Norma de beta:", beta_norm)

print("Vetor:", v2)

scalar_mult = beta_norm * v2
print("Multiplicação por escalar:", scalar_mult)

scalar_mult = np.multiply(beta_norm, v2)
print("Multiplicação por escalar:", scalar_mult)

# Testando a criação de um vetor nulo
print("Testando a criação de um vetor nulo ===================")

nulo = np.zeros(3, dtype="complex128")
print(nulo)

nulo = np.array([0 + 0j, 0 + 0j, 0 + 0j], dtype="complex128")
print(nulo)

print("Testando o cálculo do vetor inverso ===================")
# Referência: https://www.uel.br/projetos/matessencial/basico/medio/ncomplexos.html#
# Se z = 5 + 12i, z^-1 = 5/169 - 12/169i = 0,0296 - 0,0710i

v3 = np.array([5 + 12j], dtype="complex128")
print("Vetor:", v3)

inverso = np.reciprocal(v3)
print("Inverso:", inverso)

inverso = np.conj(v3) / np.linalg.norm(v3) ** 2
print("Inverso:", inverso)

inverso = 1 / v3
print("Inverso:", inverso)

inverso = np.conj(v3) / (np.abs(v3) ** 2)
print("Inverso:", inverso)
