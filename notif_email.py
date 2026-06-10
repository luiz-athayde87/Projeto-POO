from notificador import Notificador

class NotificadorEmail(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando [EMAIL] com a mensagem: {mensagem}")