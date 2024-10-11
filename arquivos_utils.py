import os
import shutil

DIRETORIO_EXEMPLOS = './exemplos'


def ler_arquivo(caminho_para_arquivo, modo='rb') -> str:
    with open(caminho_para_arquivo, modo) as arquivo:
        return arquivo.read()


def escrever_arquivo(caminho_para_arquivo, conteudo, modo='wb') -> None:
    with open(caminho_para_arquivo, modo) as arquivo:
        arquivo.write(conteudo)


def garanta_existencia_diretorio_teste(diretorio_de_teste):
    print(f'Garantindo existência do diretório teste {diretorio_de_teste}...')
    if os.path.exists(diretorio_de_teste):
        print(f'Diretório {diretorio_de_teste} já existe. Sobrescrendo.')
        shutil.rmtree(diretorio_de_teste)
    else:
        print(f'Criando diretório {diretorio_de_teste}...')

    print(f'Copiando arquivos de {DIRETORIO_EXEMPLOS} para {diretorio_de_teste}...')
    shutil.copytree(DIRETORIO_EXEMPLOS, diretorio_de_teste)
    print('Arquivos copiados com sucesso!')


def remova_chave_de_execucao_anterior(gerenciador_de_chave):
    try:
        gerenciador_de_chave.remova_chave()
    except FileNotFoundError:
        pass


def prepare_ambiente_de_teste(diretorio_de_teste, gerenciador_de_chave):
    garanta_existencia_diretorio_teste(diretorio_de_teste)
    remova_chave_de_execucao_anterior(gerenciador_de_chave)
