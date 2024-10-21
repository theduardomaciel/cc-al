<center><h1></h1></center>

<center><h1>Álgebra Aplicada - Manipulação de Áudio</h1></center>
<br>

---

Considere 2 arquivos de audio no formato WAV, por exemplo: `audio1.wav` e `audio2.wav`. Considere que cada áudio pode ser visto como um vetor em um espaço vetorial de senoides, onde cada componente do áudio é uma coordenada do vetor, siga os passos a seguir:

*   `A leitura do arquivo WAV considera cada posição do vetor como o valor do pico da onda sonora`;
*   Gerar combinações lineares dos vetores das amostras dos audios;
*   Exporte o resultado final como um arquivo WAV chamado resultado.wav

---

### Sobre as manipulações

> "Fique à vontade para manipular os arquivo e assim validar as observações."

Tanto no PDF quanto no script em Python, estão descritos alguns experimentos que testamos e podem ser reproduzidos com os arquivos de áudio disponíveis 😊

---

### Respostas

**1.   Qual o resultado de somar os 2 vetores?**
<br>
> Resposta: <br>

A soma dos dois vetores (áudios) resulta em um novo vetor onde cada componente é a soma das amplitudes correspondentes de audio1 e audio2. <br>
Se a soma ultrapassar o limite de amplitude do formato WAV (normalmente -32768 a 32767 para 16 bits¹), isso pode causar distorção (no nosso caso, alguns estalos ou ruídos).<br>
Portanto, para evitar isso, podemos normalizar a soma, caso necessário, resultando em um novo vetor de áudio sem falhas composto pelo som dos dois áudios.

> ¹Cada bit pode ser 0 ou 1, o que significa que, em 16 bits, são 65.536 valores de volume possíveis.

<br>
<br>

**2.   Qual o resultado de multiplicação por escalar?** 
<br>
> Resposta: <br>

A multiplicação por um escalar k de um vetor de áudio resulta em um vetor de áudio onde cada componente é multiplicado por k. Isso ajusta a amplitude do áudio. <br>
Por exemplo, multiplicar por 0.5 reduzirá o volume pela metade.
<br>
<br>

**3.   O vetor nulo representa o quê?** 
<br>
> Resposta: <br>

O vetor nulo em um espaço vetorial de áudio representa a ausência de som, ou seja, um áudio onde todas as amplitudes são zero em todas as amostras. Esse vetor não produz nenhum som quando reproduzido.
<br>
<br>

**4.   Adicionando para um som o som correspondente ao seu vetor inverso, considere como inversão de fase, devemos obter qual resultado?**
<br>
> Resposta: <br>

A adição de um vetor e seu inverso resulta no vetor nulo. Portanto, ao adicionar um áudio ao seu inverso (ou seja, um áudio que possui amplitudes opostas), o resultado deve ser um silêncio absoluto. <br>
Isso ocorre porque as amplitudes de um áudio são exatamente canceladas pelas amplitudes opostas do outro áudio.

