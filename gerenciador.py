from notificador import Notificador


class GerenciadorDeNotificacoes:
    def __init__(self, notificadores: list[Notificador]):
        self.notificadores = notificadores

    def enviar_todos(self, mensagem):
        for notificador in self.notificadores:
            notificador.enviar(mensagem)