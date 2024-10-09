import os
import shutil


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
    print(f'Criptografando diretório {diretorio}...')


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
            print('Criptografando...')
        elif opcao == 2:
            descriptografe_diretorio(DIRETORIO_TESTE)
            print('Descriptografando...')
        elif opcao == 0:
            print('Até mais!')
        else:
            print('Opção inválida!')
