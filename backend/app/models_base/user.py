"""
Modelo User - Utilizadores do sistema GestOnGo
Versão base com autenticação e gestão de utilizadores
"""

from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class User(Base):
    """
    Modelo de utilizadores do sistema
    
    Campos:
    - id: Chave primária auto-incremento
    - nome: Nome completo do utilizador
    - email: Email único para login
    - hash_senha: Senha hasheada com bcrypt
    - is_active: Utilizador activo (permite desactivar sem eliminar)
    """
    __tablename__ = "utilizadores"

    id = Column(Integer, primary_key=True, index=True, comment="ID único do utilizador")
    nome = Column(String(100), nullable=False, comment="Nome completo do utilizador")
    email = Column(String(255), unique=True, index=True, nullable=False, comment="Email único para login")
    hash_senha = Column(String(255), nullable=False, comment="Senha hasheada com bcrypt")
    is_active = Column(Boolean, default=True, comment="Utilizador activo no sistema")

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}', nome='{self.nome}')>"
