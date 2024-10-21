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
    # A soma de vetores consiste na soma de seus elementos correspondentes
    w = np.add(u, v)

    return w


def produto(beta, u):
    # O produto escalar consiste na multiplicação da norma de beta por cada elemento de u

    beta_norm = np.linalg.norm(beta)
    # print("Beta:", beta)
    # print("Norma de beta:", beta_norm)

    w = beta_norm * u
    # print("Vetor:", u)
    # print("Multiplicação por escalar:", w)

    return w


def verifica_soma(u, v):
    """
    Verifica se o conjunto é fechado sob a operação de soma.

    Aqui, o conjunto é fechado se a soma dos vetores ainda for um vetor de números complexos.

    @param u: Um vetor de V
           v: Um vetor de V
    @return: bool: (True,  "Vetores obedecem à soma.") se os vetores forem fechados sob soma,
                   (False, "Vetores não obedecem à soma.") caso contrário.
    """

    # Precisamos garantir que a soma dos dois vetores seja um vetor válido no conjunto V ⊂ C^3.
    # Como os vetores pertencem a V, que é um subconjunto de C^3, o critério de fechamento na soma
    # é que o resultado da soma também deve pertencer a V, ou seja, deve ser um vetor de números complexos.

    # Assim, a função deve verificar:
    # 1. Se a soma dos vetores ainda é um vetor de números complexos
    # 2. Se o vetor resultante da soma ainda tem exatamente 3 elementos (pertencendo a C^3.

    w = soma(u, v)
    # Verifica se todos os elementos do resultado são complexos e se o vetor resultante tem 3 elementos
    if np.all(np.iscomplexobj(w)) and len(w) == 3:
        return True  # "Vetores obedecem à soma."
    else:
        return False  # "Vetores não obedecem à soma."


def verifica_produto(beta, u):
    """
    Verifica se o conjunto é fechado sob a operação de produto.

    Aqui, o conjunto é fechado se o produto de um vetor por um escalar complexo ainda for
    um vetor de números complexos.

    @param beta: Um valor escalar complexo
           u: Um vetor de V
    @return: bool: (True,  "Vetores obedecem ao produto.") se os vetores forem fechados sob produto,
                   (False, "Vetores não obedecem ao produto.") caso contrário.
    """
    w = produto(beta, u)

    if np.all(
        np.iscomplexobj(w) and len(w) == 3
    ):  # Verifica se todos os elementos do resultado são complexos
        return True  # "Vetores obedecem ao produto."
    else:
        return False  # "Vetores não obedecem ao produto."


print("Testando fechamento da soma:")
for i in range(len(v)):
    for k in range(len(v) - i - 1):
        print(
            verifica_soma(v[i], v[k + i + 1]),  # verifica se a soma é válida
            " => ",
            v[i],  # vetor u
            " , ",
            v[k + i + 1],  # vetor v
        )
        """ " => ",
        soma(v[i], v[k + i + 1]), """,  # resultado da soma
        # print("Resultado:", soma(v[i], v[k + i + 1]))

print("--------------------------------------")
print("Testando fechamento do produto escalar:")
for i in range(len(beta)):
    for k in range(len(v)):
        print(
            verifica_produto(beta[i], v[k]),  # verifica se o produto é válido
            " => ",
            beta[i],  # escalar beta
            " , ",
            v[k],  # vetor u
        )
        """ "=> ",
        produto(beta[i], v[k]), """,  # resultado do produto
        # print("Resultado:", produto(beta[i], v[k]))

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
    # O inverso de um vetor é o vetor com os elementos opostos, de modo que
    # a adição do vetor com seu inverso resulta no vetor nulo (v + (-v) = 0)
    w = -v

    return w


def verifica_inverso(v):
    # Já implementado, não se preocupar
    # print("Inverso de", v, ":", inverso(v))
    # print("Soma de", v, "com seu inverso:", soma(v, inverso(v)))
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

    return np.allclose(
        produto(beta, soma(u, v)), soma(produto(beta, u), produto(beta, v))
    )


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

    # print("(beta + gamma) * u:", produto(soma(beta, gamma), u))
    # print("beta * u + gamma * u:", soma(produto(beta, u), produto(gamma, u)))

    # Se o produto da soma de beta e gamma e u for igual à soma dos produtos de beta e u e gamma e u, então os vetores seguem a regra da distributividade

    print("Beta + Gamma:", soma(beta, gamma))
    print("abs(Beta + Gamma):", np.linalg.norm(soma(beta, gamma)))
    print("u:", u)
    print("(beta + gama) * u:", produto(soma(beta, gamma), u))

    print("Beta * u:", produto(beta, u))
    print("Gamma * u:", produto(gamma, u))
    print("Beta * u + Gamma * u:", soma(produto(beta, u), produto(gamma, u)))

    return np.allclose(
        produto(soma(beta, gamma), u), soma(produto(beta, u), produto(gamma, u))
    )


print("--------------------------------------")
print("Testando distributividade 2:")
for i in range(len(beta)):
    for k in range(len(beta) - i - 1):
        for l in range(len(v)):
            print(
                verifica_distributividade_2(beta[i], beta[i + k + 1], v[l]),
                " => ",
                beta[i],  # beta
                " , ",
                beta[i + k + 1],  # gamma
                " , ",
                v[l],  # u
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

    return np.allclose(
        produto(beta, produto(gamma, u)), produto(produto(beta, gamma), u)
    )


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
