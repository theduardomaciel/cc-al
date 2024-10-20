<center><h1></h1></center>

<center><h1>Questão 3</h1></center>

---

Quando um condutor é percorrido por uma corrente elétrica de intensidade $i$ e está imerso em um campo magnético $B$, uma força magnética $F_m$, conhecida como força de Lorentz, atuará sobre este condutor. Esta força magnética, ou força de interação magnética, surge devido ao movimento dos portadores de carga, elétrons, no condutor, pois o campo magnético não atua em cargas em repouso.

Considerando que um pedaço de fio reto de comprimento $L$ imerso num campo magnético uniforme $B$ e conduzindo uma corrente $i$ teremos que a força de Lorentz dado por:

$$F_m = i*L*B$$

onde:
* $F_m$ é a força de Lorentz
* $i$ é a corrente elétrica (A)
* $L$ é o comprimento do condutor (m)
* $B$ é o campo magnético

Um experimento ultilizando espirais de material condutor com comprimentos variados onde serão inseridos em um campo magnético uniforme de um imã permanente: $L_1 = 12.5mm$, $L_2 = 25mm$, $L_3 = 50mm$, $L_4 = 100mm$

---

## Foram realizados 10 experimentos, sendo mensurados os seguintes dados de corrente e forças, para cada comprimento do condutor:
* $i = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]$
* $F_{L_1} = [31.5, 31.55, 31.63, 31.7, 31.74, 31.82, 31.9, 31.94, 32, 32.04]$
* $F_{L_2} = [30.65, 30.8, 30.92, 31.03, 31.15, 31.25, 31.36, 31.5, 31.63, 31.73]$
* $F_{L_3} = [37.86, 38.1, 38.31, 38.53, 38.72, 38.94, 39.15, 39.4, 39.62, 39.71]$
* $F_{L_4} = [40.31, 40.75, 41.15, 41.5, 41.97, 42.42, 42.83, 43.22, 43.64, 44.04]$

## Tratamento linear da base:
Para que os gráficos possam ser comparáveis a retas passando pela origem (linear, ao invés de afim), a seguinte equação de ajuste deve ser aplicada. Ela faz com que as séries de dados de forças iniciem em 0 e em seguida converte de gramas (pela forma que foi medido) para $mN$ considerando a aceleração da gravidade como $9,8m/s^2$

$$F_{L_k}|_{k=1}^4 = (F_{L_k} - F_{L_k}[0])*9,8$$

## Problema

Usando os dados fornecidos de corrente ($i$) e força em função da corrente para cada comprimento de espiral, ajuste os gráficos e calcule o valor aproximado de $B$ em $mN/(A*mm)$ para cada espiral

## *Deve ser mantido o formalismo das demais questões*

DICA: Resolva usando curve fitting. Veja que o sistema criado $(i*L_k)*B = F_{L_k}$ vai ter mais equações do que incógnitas e não é consistente, de forma que não será possível fazer $B = (i*L_k)^{-1} * F_{L_k}$ pois não é possível encontrar uma reta que passe por todos os pontos. Apesar disso, podemos usar a [pseudo-inversa de Moore Penrose](https://pt.wikipedia.org/wiki/Inversa_de_Moore-Penrose).