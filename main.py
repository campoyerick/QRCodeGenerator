import os
import qrcode
from qrcode.constants import ERROR_CORRECT_L

class GeradorQRCode:
    def __init__(self, tamanho_caixa=10, borda=1, versao=1, correcao_erro=ERROR_CORRECT_L, cor_preenchimento="#000000"):
        self.tamanho_caixa = tamanho_caixa
        self.borda = borda
        self.versao = versao
        self.correcao_erro = correcao_erro
        self.cor_preenchimento = cor_preenchimento

    def gerar_qr_code(self, texto):
        qr = qrcode.QRCode(
            version=self.versao,
            error_correction=self.correcao_erro,
            box_size=self.tamanho_caixa,
            border=self.borda
        )
        qr.add_data(texto)
        qr.make(fit=True)
        img = qr.make_image(fill_color=self.cor_preenchimento, back_color="white")
        return img

    def salvar_qr_code(self, texto, nome_arquivo):
        img = self.gerar_qr_code(texto)
        img.save(nome_arquivo)
        print(f"QR code salvo como {nome_arquivo}")
        
        # Use-o como desejar e, em seguida, exclua o arquivo com o seguinte comando para economizar espaço:
        #self._excluir_arquivo(nome_arquivo)

    def _excluir_arquivo(self, nome_arquivo):
        try:
            os.remove(nome_arquivo)
            print(f"Arquivo {nome_arquivo} excluído com sucesso!")
        except OSError as e:
            print(f"Erro ao excluir {nome_arquivo}: {e}")

if __name__ == '__main__':
    texto = "https://legacystore.store"  # Altere isso para o que deseja codificar
    nome_arquivo = "qr-code.png"  # Altere isso para o nome desejado do seu arquivo
    gerador_qr = GeradorQRCode()
    gerador_qr.salvar_qr_code(texto, nome_arquivo)
  
