from notificador import Notificador
from datetime import datetime

class NotificadorLog(Notificador):
    def enviar(self, mensagem):
        timestamp = self._generate_timestamp()

        with open("log.txt", "a") as file: # Abre o arquivo log.txt em modo de anexação (append)
            file.write(f'{timestamp} [LOG] {mensagem} \n')  # Adiciona a mensagem ao arquivo
    
    def _generate_timestamp(self):
        """Gera timestamp formatado para o log"""
        return datetime.now().strftime("%d/%m/%Y-%H:%M:%S")