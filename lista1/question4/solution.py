import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt


# Função para leitura dos arquivos WAV
def read(file):
    sample_rate, data = wav.read(file)
    if len(data.shape) == 2:  # Verifica se tem 2 canais
        data = np.mean(data, axis=1)  # Caso tenha, converte para mono
    return sample_rate, data


# Função para plotar os gráficos
def plot_graph(time1, audio1, time2, audio2, result_time, result):
    # Plot do audio1
    plt.subplot(3, 1, 1)
    plt.plot(time1, audio1, label="Áudio 1")
    plt.xlabel("Tempo [s]")
    plt.ylabel("Amplitude")
    plt.legend()

    # Plot do audio 2
    plt.subplot(3, 1, 2)
    plt.plot(time2, audio2, label="Áudio 2")
    plt.xlabel("Tempo [s]")
    plt.ylabel("Amplitude")
    plt.legend()

    # Plot do result
    plt.subplot(3, 1, 3)
    plt.plot(result_time, result, label="Resultado")
    plt.xlabel("Tempo [s]")
    plt.ylabel("Amplitude")
    plt.legend()

    # Ajusta o layout para não sobrepor os gráficos e exibe o plot
    plt.tight_layout()
    plt.show()


# ------- Manipulação: Somando os dois áudios ===========================================


def linear_combination(audio1, audio2, k1, k2, rate1):
    # Temos como escalares para a combinação linear: k1 e k2
    # k1 é o peso para o audio1
    # k2 é o peso para o audio2

    # Na prática, o que os escalares fazem é controlar o volume de cada áudio na combinação linear
    # Por exemplo, se k1 = 1 e k2 = 1, o resultado será a soma dos dois áudios
    # - Se k1 = 1 e k2 = 0, o resultado será o áudio1
    # - Se k1 = 0 e k2 = 1, o resultado será o áudio2
    # - Se k1 = 0.5 e k2 = 0.5, o resultado será a média dos dois áudios

    # O que é interessante é que podemos anular a presença de determinadas frequências,
    # caso um dos áudios tenha uma frequência isolada que não queremos no resultado final
    # Portanto, na teoria, se k1 = 1 e k2 = -1, sendo audio1 uma voz e audio2 um ruído de fundo,
    # o resultado será a diferença entre os dois áudios, ou seja, a voz isolada

    # Infelizmente, realizar a filtragem de ruídos envolve técnicas mais avançadas de processamento de sinais
    # e não é tão simples quanto apenas inverter o sinal de um dos áudios. (acreditem, já tentamos 😅)
    # No entanto, caso estejamos tratando de uma música com voz e instrumental, e tenhamos o arquivo
    # de voz isolado, a diferença entre os dois áudios resulta no instrumental isolado! 😯

    # Para testar essa ideia, basta trocar os arquivos para audio1 e audio2 como:
    # audio1: "examples/snippet-all.wav"
    # audio2: "examples/snippet-vocal.wav"
    # E ajustar os pesos para que k1 = 1 e k2 = -1

    result = k1 * audio1 + k2 * audio2  # Combinação linear dos vetores

    # Normalização para evitar clipping (distorção)
    result = result / np.max(np.abs(result))  # Normaliza entre -1 e 1
    result = np.int16(result * 32767)  # Converte de volta para 16-bit

    result_time = np.linspace(0.0, len(result) / rate1, len(result))

    return result_time, result


""" 
Algumas manipulações nos levaram aos seguintes resultados:
    -   k1 = 1 e k2 = 1 (resultado = audio1 + audio2)
        Com esses valores, caso os áudios sejam iguais, o resultado será um áudio com o dobro do volume
        Caso sejam diferentes, o resultado será a junção dos dois áudios
        
        Como exemplo prático, podemos somar um áudio de voz com um instrumental, resultando numa música completa!
        Para testar essa ideia, basta trocar os arquivos para audio1 e audio2 como:
        - audio1: "examples/snippet-instrumental.wav"
        - audio2: "examples/snippet-vocal.wav"
        Mas lembre-se de ajustar os pesos para k1 = 1 e k2 = 1!

    -   k1 = 1 e k2 = -1 (resultado = audio1 - audio2)
        Com esses valores, caso os áudios sejam iguais, o resultado será um áudio nulo
        Assim, caso tenhamos somente um arquivo de áudio como audio1 e audio2, podemos realizar sua
        combinação linear com seu inverso, resultando num áudio nulo (silêncio absoluto). 
        Isso ocorre pois a soma de um sinal com seu inverso resulta em zero, ou seja, o áudio é cancelado.

        Agora um aspecto interessante!
        Caso sejam diferentes, porém haja alguma semelhança entre as faixas dos dois arquivos, 
        o resultado será a remoção da informação comum (intersecção) entre os dois áudios!
        Fizemos um exemplo prático envolvendo voz e instrumental no PDF e nos comentários
        da função "linear_combination()" acima! 😊

    -   k1 = 1 e k2 = 0 (resultado = audio1)
    -   k1 = 0 e k2 = 1 (resultado = audio2)
"""


def get_default(audio1_path="audios/audio1.wav", audio2_path="audios/audio2.wav"):
    # Leitura dos arquivos de áudio
    rate1, audio1 = read(audio1_path)
    rate2, audio2 = read(audio2_path)
    min_len = min(audio1.shape[0], audio2.shape[0])

    # Para testar a nulificação de um áudio, basta trocar os arquivos para:
    #   - audio1_path: "audios/audio1.wav"
    #   - audio2_path: "audios/audio1.wav"
    # Com os áudios 1 e 2 iguais, basta ajustar os pesos para k1 = 1 e k2 = -1

    # Ajuste do tamanho dos áudios
    audio1 = audio1[:min_len]
    audio2 = audio2[:min_len]

    # Criação do vetor de tempo
    time1 = np.linspace(0.0, len(audio1) / rate1, len(audio1))
    time2 = np.linspace(0.0, len(audio2) / rate2, len(audio2))

    return rate1, audio1, rate2, audio2, time1, time2


def main():
    # ============================ Configurações Iniciais ===========================
    rate1, audio1, rate2, audio2, time1, time2 = get_default()

    k1 = 1  # Peso para audio1, ajuste conforme necessário
    k2 = 1  # Peso para audio2, ajuste conforme necessário
    # ===============================================================================

    # Para alguns exemplos práticos com os snippets, basta trocar os arquivos para:
    #   1. Obtenção do equivalente à musica original (com voz e instrumental)
    #       - get_default("examples/snippet-instrumental.wav", "examples/snippet-vocal.wav")
    #       - k1 = 1 e k2 = 1
    #   2. Remoção da voz da música original/completa
    #      - get_default("examples/snippet-all.wav", "examples/snippet-vocal.wav")
    #      - k1 = 1 e k2 = -1

    result_time, result = linear_combination(audio1, audio2, k1, k2, rate1)

    # Cuidado!
    # O resultado precisa ser processado antes do gráfico, caso contrário,
    # o arquivo só seria salvo após o fechamento do gráfico
    result = np.int16(result)
    wav.write("resultado.wav", rate1, result)  # O arquivo fica nos arquivos do Collab

    plot_graph(time1, audio1, time2, audio2, result_time, result)


main()
