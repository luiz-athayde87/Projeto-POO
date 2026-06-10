from notificador import Notificador

class NotificadorWhatsapp(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando [WHATSAPP] com a mensagem: {mensagem}")