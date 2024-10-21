import numpy as np
from matplotlib import pyplot as plt
from numpy.linalg import pinv

# Aquisição dos dados
i = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5])
L_1 = 0.0125
L_2 = 0.025
L_3 = 0.05
L_4 = 0.1
f_l1 = np.array([31.5, 31.55, 31.63, 31.7, 31.74, 31.82, 31.9, 31.94, 32, 32.04])
f_l2 = np.array([30.65, 30.8, 30.92, 31.03, 31.15, 31.25, 31.36, 31.5, 31.63, 31.73])
f_l3 = np.array([37.86, 38.1, 38.31, 38.53, 38.72, 38.94, 39.15, 39.4, 39.62, 39.71])
f_l4 = np.array([40.31, 40.75, 41.15, 41.5, 41.97, 42.42, 42.83, 43.22, 43.64, 44.04])

# Tratamento dos dados - ajustando para que as forças comecem em 0 e convertendo para mN
g = 9.8  # aceleração da gravidade

f_l1_novo = (f_l1 - f_l1[0]) * g
f_l2_novo = (f_l2 - f_l2[0]) * g
f_l3_novo = (f_l3 - f_l3[0]) * g
f_l4_novo = (f_l4 - f_l4[0]) * g

# Construindo a matriz A com os valores de i * L_k
A = np.vstack([i * L_1, i * L_2, i * L_3, i * L_4]).T

# Vetores das forças tratadas
f_novo = np.vstack([f_l1_novo, f_l2_novo, f_l3_novo, f_l4_novo]).T

# Aplicação da pseudo-inversa de Moore-Penrose
B = pinv(A).dot(f_novo)

# Extraindo os valores aproximados de B para cada comprimento
B_1, B_2, B_3, B_4 = B[:, 0]

# Plotando o gráfico tratado para L_1 com ajuste
plt.scatter(i, f_l1_novo, c="r", label="L_1 obs")
plt.plot(i, i * L_1 * B_1, c="r", label="L_1 pred")
plt.legend(loc="upper left")
plt.xlabel("Corrente")
plt.ylabel("Força magnética (tratada)")
plt.show()

# Resultados de B para cada comprimento
B_1, B_2, B_3, B_4
