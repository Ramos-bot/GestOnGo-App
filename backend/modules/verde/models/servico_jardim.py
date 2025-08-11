"""
Modelo ServicoJardim - Módulo Verde (Jardinagem)
Serviços de jardinagem e manutenção de espaços verdes
"""

from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class ServicoJardim(Base):
    """
    Modelo de serviços de jardinagem
    
    Campos:
    - id: Chave primária auto-incremento
    - tipo: Tipo de serviço (fixo: 'jardinagem')
    - data_servico: Data em que o serviço foi/será realizado
    - duracao_horas: Duração do serviço em horas
    - descricao: Descrição detalhada do serviço
    - cliente_id: Referência ao cliente (FK)
    """
    __tablename__ = "servicos_jardim"

    id = Column(Integer, primary_key=True, index=True, comment="ID único do serviço")
    tipo = Column(String(20), default="jardinagem", nullable=False, comment="Tipo de serviço (fixo)")
    data_servico = Column(Date, nullable=False, comment="Data do serviço")
    duracao_horas = Column(Integer, nullable=False, comment="Duração em horas")
    descricao = Column(Text, nullable=True, comment="Descrição detalhada do serviço")
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False, comment="ID do cliente")

    # Relacionamento com Cliente
    cliente = relationship("Cliente", back_populates="servicos_jardim")

    def __repr__(self):
        return f"<ServicoJardim(id={self.id}, tipo='{self.tipo}', data='{self.data_servico}', cliente_id={self.cliente_id})>"

# Adicionar relacionamento reverso ao modelo Cliente
from app.models_base.cliente import Cliente
Cliente.servicos_jardim = relationship("ServicoJardim", back_populates="cliente")
