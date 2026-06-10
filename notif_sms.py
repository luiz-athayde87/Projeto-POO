from notificador import Notificador

class NotificadorSMS(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando [SMS] com a mensagem: {mensagem}")