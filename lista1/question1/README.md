<center><h1></h1></center>
<center><h1>Questão 1</h1></center>

---

O conjunto das sequências finitas de números complexos $\mathbb{C}^n$ forma um espaço vetorial sobre $\mathbb{C}$ usando as operações padrão. A ideia desta questão é implementar testes com vetores específicos em um subconjunto, o das sequências de 3 elementos complexos, mas com operações diferentes.

$$ V \subset \mathbb{C}^3 \subset \mathbb{C}^n ⇒ V = \{(v_1, v_2, v_3) : v_i = a_i + b_i j \space ; \space a_i, b_i \in \mathbb{R} \} $$

Esses testes vão verificar se esses vetores obedecem os axiomas, caso seja verificado que um deles não funcionou, mesmo que apenas para um caso apenas, poderemos dizer que o conjunto com essas operações não é espaço vetorial.

DICA: Se você não lembra as operações dos números complexos, recomendo dar uma olhada em [link](https://www.uel.br/projetos/matessencial/basico/medio/ncomplexos.html).

---

### <center>Soma Vetorial</center>

Dados os vetores $\mathrm{\vec{v}} = \{v_1, v_2, v_3\}$ e $\mathrm{\vec{u}} = \{u_1, u_2, u_3\}$, onde $v_i, u_i \in \mathbb{C}$ e são do tipo $a$ $+$ $bj$ | $a, b \in \mathbb{R}$ e $j^2 = -1$

A **soma** dos vetores é dada por:

$$\vec{u} \oplus \vec{v} = \{u_1+v_1, u_2+v_2, u_3+v_3\}$$

Ex.: $$\{1 + 2j, 0, 4j\} \oplus \{4j, -2, 6 \} = \{ 1+6j, -2, 6+4j \}$$

<br>

---

### <center>Produto Vetorial por escalar</center>

Dado o vetor $\mathrm{\vec{u}} = \{u_1, u_2, u_3\}$, o produto por escalar complexo $\beta \in \mathbb{C}$ pode ser definido como:


$$\beta \odot \vec{u} = \{|\beta|*u_1, |\beta|*u_2, |\beta|*u_3\}$$

Lembre-se que, como $\beta = \beta_{real} + \beta_{imag}j \in \mathbb{C}$,
$$|\beta| = \sqrt{\beta_{real}^2 + \beta_{imag}^2}$$

Ex.: $$(4+3j) \odot \{1 + 2j, 0, 2j\} = \{ 5 + 10j, 0, 10j \}$$



<br>

---

<br>
O objetivo da Questão é verificar se o conjunto é um espaço vetorial sobre $\mathbb{C}$ através de inspeção de exemplos e checagem de situações de quebra de axioma.

1. Implemente as funções de soma e produto
2. Implemente as funções de verificação de fechamento
3. Proponha um vetor nulo do espaço vetorial
4. Proponha um vetor inverso
5. Implemente as funções de checagem de axiomas de soma
6. Implemente as funções de checagem de axiomas de produto