import sqlite3
from typing import List, Optional, Tuple
from abc import ABC, abstractmethod


class RepositorioUsuario(ABC):
    """Interface abstrata para repositório de usuários (Dependency Inversion Principle)"""
    @abstractmethod
    def criar_tabela(self):
        """Cria a tabela de usuários se não existir"""
        pass
    
    @abstractmethod
    def adicionar(self, plataforma: str, contato: str) -> bool:
        """Adiciona um novo usuário"""
        pass
    
    @abstractmethod
    def buscar_por_plataforma(self, plataforma: str) -> List[Tuple[str, str]]:
        """Busca todos os usuários de uma plataforma específica"""
        pass
    
    @abstractmethod
    def buscar_todos(self) -> List[Tuple[str, str, str]]:
        """Busca todos os usuários cadastrados"""
        pass


class RepositorioUsuarioSQLite(RepositorioUsuario):
    """
    Implementação concreta do repositório usando SQLite
    Segue Single Responsibility Principle - responsável apenas por operações de banco
    """
    
    def __init__(self, nome_banco: str = "notificacoes.db"):
        self.nome_banco = nome_banco
        self.criar_tabela()
    
    def _obter_conexao(self):
        """Método privado para obter conexão com o banco"""
        return sqlite3.connect(self.nome_banco)
    
    def criar_tabela(self):
        """
        Cria a tabela usuarios se ela não existir
        Estrutura: id (auto-incremento), plataforma (Email/SMS/Zap), contato (email/telefone)
        """
        conexao = self._obter_conexao()
        cursor = conexao.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                plataforma TEXT NOT NULL,
                contato TEXT NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conexao.commit()
        conexao.close()
    
    def adicionar(self, plataforma: str, contato: str) -> bool:
        """
        Adiciona um novo usuário ao banco de dados
        Retorna True se sucesso, False se erro
        """
        try:
            conexao = self._obter_conexao()
            cursor = conexao.cursor()
            
            cursor.execute("""
                INSERT INTO usuarios (plataforma, contato)
                VALUES (?, ?)
            """, (plataforma, contato))
            
            conexao.commit()
            conexao.close()
            return True
        except Exception as e:
            print(f"Erro ao adicionar usuário: {e}")
            return False
    
    def buscar_por_plataforma(self, plataforma: str) -> List[Tuple[str, str]]:
        """
        Busca todos os usuários de uma plataforma específica
        Retorna lista de tuplas (id, contato)
        """
        conexao = self._obter_conexao()
        cursor = conexao.cursor()
        
        cursor.execute("""
            SELECT id, contato FROM usuarios 
            WHERE plataforma = ?
        """, (plataforma,))
        
        resultados = cursor.fetchall()
        conexao.close()
        return resultados
    
    def buscar_todos(self) -> List[Tuple[str, str, str]]:
        """
        Busca todos os usuários cadastrados
        Retorna lista de tuplas (id, plataforma, contato)
        """
        conexao = self._obter_conexao()
        cursor = conexao.cursor()
        
        cursor.execute("""
            SELECT id, plataforma, contato FROM usuarios
        """)
        
        resultados = cursor.fetchall()
        conexao.close()
        return resultados

