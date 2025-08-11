"""
Modelo ORM para utilizadores.

Este módulo define a tabela `utilizadores` na base de dados, onde são
armazenadas informações sobre cada utilizador registado na aplicação.
"""

from sqlalchemy import Column, Integer, String, Boolean

from ..core.database import Base


class User(Base):
    """Representa um utilizador do sistema."""

    __tablename__ = "utilizadores"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String, index=True)
    email: str = Column(String, unique=True, index=True, nullable=False)
    hash_senha: str = Column(String, nullable=False)
    is_active: bool = Column(Boolean, default=True)
