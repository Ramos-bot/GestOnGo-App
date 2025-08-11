"""
Modelo Cliente - Clientes do sistema GestOnGo
Versão base partilhada por todos os módulos
"""

from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Cliente(Base):
    """
    Modelo de clientes do sistema
    
    Campos:
    - id: Chave primária auto-incremento
    - nome: Nome do cliente
    - telefone: Número de telefone (opcional)
    - endereco: Morada do cliente (opcional)
    - observacoes: Notas adicionais sobre o cliente (opcional)
    """
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True, comment="ID único do cliente")
    nome = Column(String(100), nullable=False, comment="Nome do cliente")
    telefone = Column(String(20), nullable=True, comment="Número de telefone")
    endereco = Column(String(255), nullable=True, comment="Morada do cliente")
    observacoes = Column(Text, nullable=True, comment="Notas adicionais sobre o cliente")

    def __repr__(self):
        return f"<Cliente(id={self.id}, nome='{self.nome}', telefone='{self.telefone}')>"
