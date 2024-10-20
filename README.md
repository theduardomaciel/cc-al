# Aplicação prática de álgebra na computação

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./.github/cover.png">
  <source media="(prefers-color-scheme: light)" srcset="./.github/cover_light.png">
  <img alt="Aplicação prática de álgebra na computação" src="/.github/cover_light.png">
</picture>

Este repositório contém as listas de exercícios da disciplina de Álgebra Linear do curso de Ciência da Computação da Universidade Federal de Alagoas (UFAL) durante o período letivo 2024.1.

## Estrutura de Pastas

A estrutura de pastas do repositório é a seguinte:

```
├── .vscode
├── lista[1-2]
│   ├── question[n]
│   │   ├── base.py (arquivo base fornecido)
│   │   ├── README.md (enunciado da questão)
│   │   └── solution.py (solução da questão)
└── README.md
```

- **.vscode**: Configurações específicas do Visual Studio Code para o projeto, majoritariamente para Spell Check.
- **lista[1-1]**: Diretório contendo as listas de exercícios.
  - **question[n]**: Diretório contendo os arquivos referentes à questão n da lista.
    - **base.py**: Arquivo base fornecido para a questão.
    - **README.md**: Enunciado da questão.
    - **solution.py**: Solução da questão.

## Requisitos

Para rodar os scripts deste repositório, você precisará ter o Python instalado em sua máquina. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

## Uso

1. Clone este repositório para a sua máquina local:

   ```bash
   git clone https://github.com/theduardomaciel/cc-al.git
   ```

2. Navegue até o diretório do repositório:

   ```bash
   cd cc-al
   ```

3. Crie um ambiente virtual para o projeto:

   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No Linux:

     ```bash
     source venv/bin/activate
     ```

5. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

## Material Teórico
Para acessar o material teórico, você pode visitar o [Notion]() do professor Glauber.

## Links Úteis

- [Python](https://www.python.org/)
- [VSCode](https://code.visualstudio.com/)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar _pull requests_ ou abrir _issues_ para reportar bugs ou sugerir melhorias.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.