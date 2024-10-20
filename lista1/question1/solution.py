import numpy as np  # Importando a biblioteca de computação numérica

# Definição de vetores
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

# Funções


def soma(u, v):
    # A soma de vetores é simplesmente a soma de seus elementos correspondentes
    w = np.add(u, v)

    return w


def produto(beta, u):
    # O produto escalar consiste na multiplicação da norma de beta por cada elemento de u
    w = np.linalg.norm(beta) * u

    return w


def verifica_soma(u, v):
    """
    Verifica se o conjunto é fechado sob a operação de soma.

    @param u: Um vetor de V
           v: Um vetor de V
    @return: bool: (True,  "Vetores obedecem à soma.") se os vetores forem fechados sob soma,
                   (False, "Vetores não obedecem à soma.") caso contrário.
    """

    # Se a soma de u e v estiver contida em v, então o conjunto é fechado sob a operação de soma
    if np.all(soma(u, v) in v):
        return True

    return False


def verifica_produto(beta, u):
    """
    Verifica se o conjunto é fechado sob a operação de produto.

    @param beta: Um valor escalar complexo
           u: Um vetor de V
    @return: bool: (True,  "Vetores obedecem ao produto.") se os vetores forem fechados sob soma,
                   (False, "Vetores não obedecem ao produto.") caso contrário.
    """

    # Se o produto de beta e u estiver contido em u, então o conjunto é fechado sob a operação de produto
    if np.all(produto(beta, u) in u):
        return True

    return False


print("Testando fechamento da soma:")
for i in range(len(v)):
    for k in range(len(v) - i - 1):
        print(verifica_soma(v[i], v[k + i + 1]), " => ", v[i], " , ", v[k + i + 1])

print("--------------------------------------")
print("Testando fechamento do produto escalar:")
for i in range(len(beta)):
    for k in range(len(v)):
        print(verifica_produto(beta[i], v[k]), " => ", beta[i], " , ", v[k])

# proponha o vetor nulo
nulo = np.array([0 + 0j, 0 + 0j, 0 + 0j], dtype="complex128")
# ou nulo = np.zeros(3, dtype="complex128")


def verifica_nulo(v):
    # Já implementado, não se preocupar
    return np.all(
        soma(v, nulo) == v
    )  # retorna True se todos valores de v+nulo forem iguais a v e False caso contrário


print("--------------------------------------")
print("Testando vetor nulo:")
for i in range(len(v)):
    print(verifica_nulo(v[i]), " => ", v[i])


# proponha o vetor inverso
# material de apoio: https://www.uel.br/projetos/matessencial/basico/medio/ncomplexos.html#sec06
def inverso(v):
    w = np.reciprocal(v)
    # ou: np.conj(v) / np.linalg.norm(v) ** 2
    # ou 1 / v

    return w


def verifica_inverso(v):
    # Já implementado, não se preocupar
    return np.all(
        soma(v, inverso(v)) == nulo
    )  # retorna True se todos valores de v+inverso(v) forem iguais a nulo e False caso contrário


print("--------------------------------------")
print("Testando vetor inverso:")
for i in range(len(v)):
    print(verifica_inverso(v[i]), " => ", v[i])


def verifica_comutatividade(u, v):
    """
    Verifica se u + v = v + u

    @param u: Um vetor de V
           v: Um vetor de V
    @return: bool: True se os vetores forem comutativos,
                   False caso contrário.
    """

    # Se a soma de u e v for igual à soma de v e u, então os vetores são comutativos
    if np.all(soma(u, v) == soma(v, u)):
        return True

    return False


print("--------------------------------------")
print("Testando comutatividade:")
for i in range(len(v)):
    for k in range(len(v) - i - 1):
        print(
            verifica_comutatividade(v[i], v[k + i + 1]),
            " => ",
            v[i],
            " , ",
            v[k + i + 1],
        )


def verifica_associatividade(u, v, w):
    """
    Verifica se u + (v + w) = (v + u) + w

    @param v: Um vetor de V
           u: Um vetor de V
           w: Um vetor de V
    @return: bool: True se os vetores seguirem a regra da associação,
                   False caso contrário.
    """

    # Se a soma de u e a soma de v e w for igual à soma de v e u e w, então os vetores são associativos
    if np.all(soma(u, soma(v, w)) == soma(soma(u, v), w)):
        return True

    return False


print("--------------------------------------")
print("Testando associatividade:")
for i in range(len(v)):
    for k in range(len(v) - i - 1):
        for l in range(len(v) - i - k - 2):
            print(
                verifica_associatividade(v[i], v[k + i + 1], v[k + i + l + 2]),
                " => ",
                v[i],
                " , ",
                v[k + i + 1],
                " , ",
                v[k + i + l + 2],
            )


def verifica_distributividade_1(beta, u, v):
    """
    Verifica se beta * (u + v) = beta * u + beta * v

    @param beta: Um valor escalar complexo
           u: Um vetor de V
           v: Um vetor de V
    @return: bool: True se os vetores seguirem a regra da distributividade,
                   False caso contrário.
    """

    # Se o produto de beta e a soma de u e v for igual à soma dos produtos de beta e u e beta e v, então os vetores seguem a regra da distributividade
    if np.all(produto(beta, soma(u, v)) == soma(produto(beta, u), produto(beta, v))):
        return True

    return False


print("--------------------------------------")
print("Testando distributividade 1:")
for i in range(len(beta)):
    for k in range(len(v)):
        for l in range(len(v) - k - 1):
            print(
                verifica_distributividade_1(beta[i], v[k], v[k + l + 1]),
                " => ",
                beta[i],
                " , ",
                v[k],
                " , ",
                v[k + l + 1],
            )


def verifica_distributividade_2(beta, gamma, u):
    """
    Verifica se (beta + gamma) * u = beta * u + gamma * u

    @param beta: Um valor escalar complexo
           gamma: Um valor escalar complexo
           u: Um vetor de V
    @return: bool: True se os vetores seguirem a regra da distributividade,
                   False caso contrário.
    """

    # Se o produto da soma de beta e gamma e u for igual à soma dos produtos de beta e u e gamma e u, então os vetores seguem a regra da distributividade
    if np.all(
        produto(soma(beta, gamma), u) == soma(produto(beta, u), produto(gamma, u))
    ):
        return True

    return False


print("--------------------------------------")
print("Testando distributividade 2:")
for i in range(len(beta)):
    for k in range(len(beta) - i - 1):
        for l in range(len(v)):
            print(
                verifica_distributividade_2(beta[i], beta[i + k + 1], v[l]),
                " => ",
                beta[i],
                " , ",
                beta[i + k + 1],
                " , ",
                v[l],
            )


def verifica_distributividade_3(beta, gamma, u):
    """
    Verifica se beta * (gamma * u) = (beta * gamma) * u

    @param beta: Um valor escalar complexo
           gamma: Um valor escalar complexo
           u: Um vetor de V
    @return: bool: True se os vetores seguirem a regra da distributividade,
                   False caso contrário.
    """

    # Se o produto de beta e o produto de gamma e u for igual ao produto de beta e gamma e u, então os vetores seguem a regra da distributividade
    if np.all(produto(beta, produto(gamma, u)) == produto(produto(beta, gamma), u)):
        return True

    return False


print("--------------------------------------")
print("Testando distributividade 3:")
for i in range(len(beta)):
    for k in range(len(beta) - i - 1):
        for l in range(len(v)):
            print(
                verifica_distributividade_3(beta[i], beta[i + k + 1], v[l]),
                " => ",
                beta[i],
                " , ",
                beta[i + k + 1],
                " , ",
                v[l],
            )


def verifica_escalar_unitario(u):
    """
    Verifica se 1 * u = u

    @param : Um vetor de V
    @return: bool: True se os vetores seguirem a regra da distributividade,
                   False caso contrário.
    """

    # Se o produto de 1 e u for igual a u, então o vetor segue a regra do escalar unitário
    if np.all(produto(1, u) == u):
        return True

    return False


print("--------------------------------------")
print("Testando o axioma do escalar unitário:")
for i in range(len(v)):
    print(verifica_escalar_unitario(v[i]), " => ", v[i])
