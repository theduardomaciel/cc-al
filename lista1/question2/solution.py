import numpy as np


def gauss(A, B):
    """
    Resolve um sistema de equações lineares Ax = B utilizando o método de eliminação gaussiana.

    @param A: Uma matriz (array do numpy) representando os coeficientes do sistema.
    @param B: Um vetor (array do numpy) representando os termos independentes.

    @return: Um vetor 1D com a solução do sistema se o sistema for consistente,
             ou lança uma exceção se o sistema for singular ou indefinido.
    """

    n = len(A)  # número de variáveis
    A = np.array(A, dtype=np.float64)
    B = np.array(B, dtype=np.float64)

    # Aumenta a matriz A com a coluna de termos independentes B
    A = np.hstack([A, B.reshape(-1, 1)])

    # Etapa de Eliminação Gaussiana
    for i in range(n):
        # Pivotação Parcial: Encontra a linha com o maior valor absoluto na coluna atual
        p = np.argmax(np.abs(A[i:, i])) + i
        if A[p, i] == 0:
            raise Exception("Sistema singular ou indefinido.")

        # Troca a linha atual com a linha pivô, se necessário
        if p != i:
            A[[i, p]] = A[[p, i]]

        # Eliminação para criar zeros abaixo do pivô
        for j in range(i + 1, n):
            fator = A[j, i] / A[i, i]
            A[j, i:] -= fator * A[i, i:]

    # Verificação se o sistema é consistente (checando se há linha de zeros com um termo não-zero em B)
    for i in range(n):
        if np.allclose(A[i, :-1], 0) and not np.isclose(A[i, -1], 0):
            raise Exception("Sistema inconsistente. Não há solução.")

    # Substituição Reversa (Back-substitution)
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if A[i, i] == 0:
            raise Exception("Sistema singular.")

        # Calcula a variável i-ésima
        # X[i] = (B[i] - soma dos termos já calculados) / A[i, i]
        # A[i, i] é o coeficiente da variável i na i-ésima equação
        X[i] = (A[i, -1] - np.sum(A[i, i + 1 : n] * X[i + 1 :])) / A[i, i]

    return X


def combinacao(vetores, vetor_alvo):
    """
    Determina se o vetor alvo pode ser representado como uma combinação linear
    dos vetores dados.

    @param vetores: Conjunto de vetores.
    @param vetor_alvo: Vetor que precisa ser representado como combinação linear.

    @return: bool resultado se é combinação linear ou não (True ou False)
             coef array com os coeficientes da combinação linear
    """

    # Verifica se os vetores e o vetor alvo têm dimensões compatíveis
    if vetores.shape[1] != len(vetor_alvo):
        # raise ValueError("Dimensões incompatíveis entre os vetores e o vetor alvo.")
        return False, None

    # A matriz A é formada pelos vetores (colunas), e o vetor B é o vetor alvo
    try:
        coef = gauss(vetores, vetor_alvo)
        return True, coef
    except Exception as e:
        # Se ocorrer uma exceção, isso significa que o sistema não tem solução
        return False, None


print("Caso 1")
vetores = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
vetor_alvo = np.array([1, 2, 3])

resultado, coef = combinacao(vetores, vetor_alvo)
coef_2 = np.linalg.solve(vetores, vetor_alvo)
print("Caso 1, coef_2", coef_2)

if resultado:
    print(coef)
else:
    print("Não é combinação linear")

print("Caso 2")
vetores = np.array(
    [
        [3.5, 2.1, 2, 4],
        [5.25, 3.15, 3.0, 6.0],
        [4.2, 2.52, 2.4, 4.8],
        [-4.9, -2.94, -2.8, -5.6],
    ]
)
vetor_alvo = np.array([1, 2, 3, 4])

resultado, coef = combinacao(vetores, vetor_alvo)
try:
    caso_2 = np.linalg.solve(vetores, vetor_alvo)
    print("Caso 2, coef_2", caso_2)
except Exception as e:
    print(f"Erro: {e}")

if resultado:
    print(coef)
else:
    print("Não é combinação linear")

print("Caso 3")
vetores = np.array(
    [
        [np.exp(3), np.exp(-2), np.exp(-4), np.sin(np.pi / 2), np.cos(np.pi / 6), 0],
        [5.43, 13, 2.5, 1, 1, 2],
        [8.145, 19.5, 3.75, 1.5, 1.5, 3.0],
        [1, 4, 7.8, np.tan(np.pi / 6), np.tanh(1), 3],
        [1, 4, 7.8, np.tan(np.pi / 6), np.tanh(1), 3],
    ]
)
vetor_alvo = np.array([1, 2, 3, 4, 5, 6])

resultado, coef = combinacao(vetores, vetor_alvo)
try:
    caso_3 = np.linalg.solve(vetores, vetor_alvo)
    print("Caso 3, coef_2", caso_3)
except Exception as e:
    print(f"Erro: {e}")

if resultado:
    print(coef)
else:
    print("Não é combinação linear")


# Alguns outros exemplos de Teste
def executar_testes():
    # Exemplo 1: Vetor é uma combinação linear (caso trivial)
    print("Exemplo 1: Vetor é uma combinação linear (caso trivial)")
    vetores = np.array([[1, 0], [0, 1]])
    vetor_alvo = np.array([3, 4])
    resultado, coef = combinacao(vetores, vetor_alvo)
    if resultado:
        print(f"Coeficientes: {coef}")
    else:
        print("Não é combinação linear")

    # Exemplo 2: Vetor não é combinação linear (vetores dependentes)
    print("\nExemplo 2: Vetor não é combinação linear (vetores dependentes)")
    vetores = np.array([[1, 1], [2, 2]])
    vetor_alvo = np.array([3, 5])
    resultado, coef = combinacao(vetores, vetor_alvo)
    if resultado:
        print(f"Coeficientes: {coef}")
    else:
        print("Não é combinação linear")

    # Exemplo 3: Vetor é combinação linear (vetores 3D)
    print("\nExemplo 3: Vetor é combinação linear (vetores 3D)")
    vetores = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    vetor_alvo = np.array([2, -3, 1])
    resultado, coef = combinacao(vetores, vetor_alvo)
    if resultado:
        print(f"Coeficientes: {coef}")
    else:
        print("Não é combinação linear")

    # Exemplo 4: Vetor não é combinação linear (dimensões diferentes)
    print("\nExemplo 4: Vetor não é combinação linear (dimensões diferentes)")
    vetores = np.array([[1, 2, 3], [4, 5, 6]])
    vetor_alvo = np.array([7, 8])
    try:
        resultado, coef = combinacao(vetores, vetor_alvo)
        if resultado:
            print(f"Coeficientes: {coef}")
        else:
            print("Não é combinação linear")
    except Exception as e:
        print(f"Erro: {e}")


# Executa os exemplos adicionais
# executar_testes()
