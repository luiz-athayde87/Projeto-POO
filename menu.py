from gerenciador import GerenciadorDeNotificacoes
from usuario import ServicoUsuario
from typing import List


class MenuInterativo:
    """
    Classe responsável pela interface de menu interativo
    Segue Single Responsibility Principle - responsável apenas pela interação com usuário
    """
    
    def __init__(self, gerenciador: GerenciadorDeNotificacoes, servico_usuario: ServicoUsuario):
        self.gerenciador = gerenciador
        self.servico_usuario = servico_usuario
    
    def exibir_menu_principal(self):
        """Exibe o menu principal e processa a escolha do usuário"""
        while True:
            print("\n" + "="*50)
            print("    SISTEMA DE NOTIFICAÇÕES MULTIPLATAFORMA")
            print("="*50)
            print("\nDigite 1 Para enviar uma mensagem para TODOS os usuários")
            print("Digite 2 Para enviar Mensagem para um Grupo de Usuários")
            print("         (Email: REAL | SMS/Zap: SIMULAÇÃO)")
            print("Digite 3 Para cadastro de Usuários")
            print("Digite 0 Para sair")
            print("="*50)
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self._opcao_enviar_todos()
            elif opcao == "2":
                self._opcao_enviar_grupo()
            elif opcao == "3":
                self._opcao_cadastrar_usuario()
            elif opcao == "0":
                print("\nSaindo do sistema...")
                break
            else:
                print("\nOpção inválida! Tente novamente.")
    
    def _opcao_enviar_todos(self):
        """
        Opção 1: Envia mensagem para todos os usuários cadastrados
        por todos os notificadores possíveis
        """
        print("\n" + "-"*50)
        print("ENVIAR MENSAGEM PARA TODOS OS USUÁRIOS")
        print("-"*50)
        
        mensagem = input("\nDigite a mensagem a ser enviada: ").strip()
        
        if not mensagem:
            print("Mensagem não pode estar vazia!")
            return
        
        # Busca todos os usuários cadastrados
        usuarios = self.servico_usuario.obter_todos()
        
        if not usuarios:
            print("Nenhum usuário cadastrado no sistema!")
            return
        
        print(f"\nEnviando mensagem para {len(usuarios)} usuário(s) através de todas as plataformas...")
        
        # Envia através de todos os notificadores
        self.gerenciador.enviar_todos(mensagem, usuarios)
        
        print("\nMensagem enviada com sucesso!")
    
    def _opcao_enviar_grupo(self):
        """
        Opção 2: Envia mensagem para um grupo específico de usuários
        (Email, SMS ou Zap)
        """
        print("\n" + "-"*50)
        print("ENVIAR MENSAGEM PARA GRUPO DE USUÁRIOS")
        print("-"*50)
        print("\nPara qual plataforma você quer enviar a mensagem?")
        print("1 - Email (ENVIO REAL)")
        print("2 - SMS (SIMULAÇÃO)")
        print("3 - Zap/WhatsApp (SIMULAÇÃO)")
        
        opcao_plataforma = input("\nEscolha a plataforma (1, 2 ou 3): ").strip()
        
        plataforma_map = {
            "1": "Email",
            "2": "Sms",
            "3": "Zap"
        }
        
        if opcao_plataforma not in plataforma_map:
            print("Opção inválida!")
            return
        
        plataforma = plataforma_map[opcao_plataforma]
        
        mensagem = input(f"\nDigite a mensagem a ser enviada via {plataforma}: ").strip()
        
        if not mensagem:
            print("Mensagem não pode estar vazia!")
            return
        
        # Busca usuários da plataforma selecionada
        usuarios = self.servico_usuario.obter_por_plataforma(plataforma)
        
        if not usuarios:
            print(f"Nenhum usuário cadastrado para a plataforma {plataforma}!")
            return
        
        print(f"\nEnviando mensagem para {len(usuarios)} usuário(s) via {plataforma}...")
        
        # Envia apenas pela plataforma selecionada
        self.gerenciador.enviar_por_plataforma(mensagem, plataforma, usuarios)
        
        print(f"\nMensagem enviada com sucesso via {plataforma}!")
    
    def _opcao_cadastrar_usuario(self):
        """
        Opção 3: Cadastra um novo usuário em uma plataforma específica
        """
        print("\n" + "-"*50)
        print("CADASTRO DE USUÁRIOS")
        print("-"*50)
        print("\nEm qual notificador você quer cadastrar o usuário?")
        print("1 - Email (envio real)")
        print("2 - SMS (simulação)")
        print("3 - Zap/WhatsApp (simulação)")
        
        opcao_plataforma = input("\nEscolha a plataforma (1, 2 ou 3): ").strip()
        
        plataforma_map = {
            "1": "Email",
            "2": "Sms",
            "3": "Zap"
        }
        
        if opcao_plataforma not in plataforma_map:
            print("Opção inválida!")
            return
        
        plataforma = plataforma_map[opcao_plataforma]
        
        # Solicita o contato baseado na plataforma
        if plataforma == "Email":
            contato = input(f"\nDigite o email do usuário: ").strip()
        else:
            contato = input(f"\nDigite o telefone do usuário (com DDD): ").strip()
        
        if not contato:
            print("Contato não pode estar vazio!")
            return
        
        # Tenta cadastrar
        sucesso = self.servico_usuario.cadastrar(plataforma, contato)
        
        if sucesso:
            print(f"\nUsuário cadastrado com sucesso na plataforma {plataforma}!")
        else:
            print(f"\nErro ao cadastrar usuário. Verifique os dados e tente novamente.")

