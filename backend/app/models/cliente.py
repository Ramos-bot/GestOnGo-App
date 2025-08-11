"""
Modelo ORM para clientes.

Este módulo define a tabela `clientes`, representando os clientes que
contratam serviços de jardinagem e manutenção de piscinas. Cada cliente
pode ter múltiplos serviços associados.
"""

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from ..core.database import Base


class Cliente(Base):
    """Representa um cliente que contrata serviços."""

    __tablename__ = "clientes"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String, index=True)
    telefone: str = Column(String, nullable=True)
    endereco: str = Column(String, nullable=True)
    observacoes: str = Column(Text, nullable=True)

    # Relação um-para-muitos com serviços: um cliente pode ter vários serviços
    servicos = relationship("Servico", back_populates="cliente", cascade="all, delete-orphan")
