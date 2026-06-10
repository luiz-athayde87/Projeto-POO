from notif_email import NotificadorEmail
from notif_sms import NotificadorSMS
from notif_whatsapp import NotificadorWhatsapp
from gerenciador import GerenciadorDeNotificacoes
from notif_log import NotificadorLog


#Exemplo de uso:
email = NotificadorEmail()
sms = NotificadorSMS()
log = NotificadorLog()
zap = NotificadorWhatsapp()

gerenciador = GerenciadorDeNotificacoes([email, sms, log, zap])
gerenciador.enviar_todos("Sistema em manutenção às 22h.")

