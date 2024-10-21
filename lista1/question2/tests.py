import numpy as np

# Definindo a matriz dos coeficientes e o vetor alvo
matriz_coeficientes = np.array([[1, 2, 3], [4, 5, 6]])
vetor_alvo = np.array([[7], [8]])

# Criando a matriz aumentada
matriz_aumentada = np.hstack((matriz_coeficientes, vetor_alvo))

# Calculando os postos
posto_coeficientes = np.linalg.matrix_rank(matriz_coeficientes)
posto_aumentada = np.linalg.matrix_rank(matriz_aumentada)

# Verificando se o sistema possui solução
tem_solucao = posto_coeficientes == posto_aumentada
print("O sistema possui solução?", tem_solucao)

# Verificando se o sistema possui solução única
if tem_solucao:
    n = matriz_coeficientes.shape[1]
    tem_solucao_unica = posto_coeficientes == n
    print("O sistema possui solução única?", tem_solucao_unica)

# Verificando por meio da eliminação de Gauss
try:
    coeficientes = np.linalg.solve(matriz_coeficientes, vetor_alvo)
    print("Coeficientes:", coeficientes)
except Exception as e:
    print("Erro:", e)
