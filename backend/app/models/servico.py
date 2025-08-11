"""
Modelo ORM para serviços.

Cada serviço representa uma visita agendada para realizar tarefas de
jardinagem ou manutenção de piscinas. Os serviços estão associados a
clientes e contêm informação sobre a data, duração e descrição.
"""

from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..core.database import Base


class Servico(Base):
    """Representa um serviço de campo."""

    __tablename__ = "servicos"

    id: int = Column(Integer, primary_key=True, index=True)
    tipo: str = Column(String, index=True)  # "jardinagem" ou "piscina"
    data_servico = Column(Date, index=True)
    duracao_horas = Column(Integer)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    descricao: str = Column(Text, nullable=True)
    status: str = Column(String, default="agendado", index=True)  # agendado, em_progresso, concluido, cancelado
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_actualizacao = Column(DateTime(timezone=True), onupdate=func.now())

    # Relação inversa para aceder ao cliente do serviço
    cliente = relationship("Cliente", back_populates="servicos")
