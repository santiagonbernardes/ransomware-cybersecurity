def ler_arquivo(caminho_para_arquivo, modo='rb') -> str:
    with open(caminho_para_arquivo, modo) as arquivo:
        return arquivo.read()


def escrever_arquivo(caminho_para_arquivo, conteudo, modo='wb') -> None:
    with open(caminho_para_arquivo, modo) as arquivo:
        arquivo.write(conteudo)
