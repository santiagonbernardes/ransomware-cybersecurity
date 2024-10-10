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
