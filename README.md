# Ransomware para a disciplina Cognitive Cybersecurity

## Grupo

- Cristiano Washington Dias – RM555992
- Santiago Nascimento Bernardes – RM557447

## Repositório

- https://github.com/santiagonbernardes/ransomware-cybersecurity

## Requisitos do Projeto

O código deve ser capaz de:

- Criptografar uma pasta alvo
- Exibir uma mensagem em tela informando do ataque
- Salvar a chave de criptografia em um arquivo denominado `key.rans` na mesma pasta dos arquivos criptografados
- Na tela informando o ataque deve existir um campo para inserir a chave e descriptografar os arquivos
- Realizar a descriptografia dos arquivos na pasta após a chave ser inserida

## Instruções para Execução do Projeto

### 1. Instalando as dependências manualmente

1. Certifique-se de ter o Python instalado (versão 3.10 ou superior).
2. Instale as dependências necessárias:
    ```sh
    pip install cryptography
    ```

### 2. Instalando as dependências usando o arquivo `requirements.txt`

1. Certifique-se de ter o Python instalado (versão 3.10 ou superior).
2. Instale as dependências listadas no arquivo `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

### 3. Usando `venv` e instalando as dependências usando o arquivo `requirements.txt`

1. Certifique-se de ter o Python instalado (versão 3.10 ou superior).
2. Crie um ambiente virtual:
    ```sh
    python -m venv .venv
    ```
3. Ative o ambiente virtual:
    - No Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```sh
        source .venv/bin/activate
        ```
4. Instale as dependências listadas no arquivo `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

## Executando o Projeto

1. Para criptografar a pasta alvo, execute o script `ransomware.py`:
    ```sh
    python ransomware.py
    ```
2. Siga as instruções exibidas na tela para inserir a chave de descriptografia e descriptografar os arquivos.

## Estrutura do Projeto

- `ransomware.py`: Script principal que executa o ransomware.
- `classes.py`: Contém as classes `GerenciadorDeChave` e `Ransomware`.
- `excecoes.py`: Define exceções personalizadas.
- `arquivos_utils.py`: Utilitários para leitura e escrita de arquivos.
- `requirements.txt`: Lista de dependências do projeto.
- `exemplos`: Contém alguns arquivos para que o ransomware possa ser testado.