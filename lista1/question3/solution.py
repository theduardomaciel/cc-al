import numpy as np
from matplotlib import pyplot as plt

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

# Plotando os gráficos
plt.scatter(i, f_l1, c="r", label="L_1")
plt.scatter(i, f_l2, c="g", label="L_2")
plt.scatter(i, f_l3, c="b", label="L_3")
plt.scatter(i, f_l4, c="k", label="L_4")
plt.legend(loc="upper left")
plt.xlabel("Corrente")
plt.ylabel("Força magnética")
plt.show()
