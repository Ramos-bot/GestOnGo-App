"""
Esquemas Pydantic para serviços.

Define os campos que são aceites ao criar um serviço e os campos
que são devolvidos ao cliente quando um serviço é consultado.
"""

from datetime import date, datetime
from typing import Optional, Literal
from enum import Enum

from pydantic import BaseModel, validator


class TipoServico(str, Enum):
    """Tipos de serviço disponíveis."""
    JARDINAGEM = "jardinagem"
    PISCINA = "piscina"


class StatusServico(str, Enum):
    """Estados do serviço."""
    AGENDADO = "agendado"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDO = "concluido"
    CANCELADO = "cancelado"


class ServicoBase(BaseModel):
    tipo: TipoServico
    data_servico: date
    duracao_horas: int
    cliente_id: int
    descricao: Optional[str] = None
    status: StatusServico = StatusServico.AGENDADO

    @validator("data_servico")
    def validar_data_servico(cls, v: date) -> date:
        """Valida se a data do serviço não é no passado."""
        if v < date.today():
            raise ValueError("A data do serviço não pode ser no passado")
        return v

    @validator("duracao_horas")
    def validar_duracao(cls, v: int) -> int:
        """Valida a duração do serviço."""
        if v < 1:
            raise ValueError("Duração deve ser pelo menos 1 hora")
        if v > 12:
            raise ValueError("Duração não pode exceder 12 horas por dia")
        return v

    @validator("cliente_id")
    def validar_cliente_id(cls, v: int) -> int:
        """Valida o ID do cliente."""
        if v <= 0:
            raise ValueError("ID do cliente deve ser um número positivo")
        return v

    @validator("descricao")
    def validar_descricao(cls, v: Optional[str]) -> Optional[str]:
        """Limpa e valida a descrição."""
        if v is None:
            return None
        descricao_limpa = v.strip()
        if len(descricao_limpa) > 500:
            raise ValueError("Descrição não pode ter mais de 500 caracteres")
        return descricao_limpa if descricao_limpa else None


class ServicoCreate(ServicoBase):
    pass


class ServicoUpdate(BaseModel):
    """Schema para actualização parcial de serviços."""
    tipo: Optional[TipoServico] = None
    data_servico: Optional[date] = None
    duracao_horas: Optional[int] = None
    descricao: Optional[str] = None
    status: Optional[StatusServico] = None

    @validator("data_servico")
    def validar_data_servico(cls, v: Optional[date]) -> Optional[date]:
        if v is not None and v < date.today():
            raise ValueError("A data do serviço não pode ser no passado")
        return v

    @validator("duracao_horas")
    def validar_duracao(cls, v: Optional[int]) -> Optional[int]:
        if v is not None:
            if v < 1 or v > 12:
                raise ValueError("Duração deve estar entre 1 e 12 horas")
        return v


class ServicoResponse(ServicoBase):
    id: int
    data_criacao: Optional[datetime] = None

    class Config:
        orm_mode = True


class ServicoResumo(BaseModel):
    """Schema resumido para listagens."""
    id: int
    tipo: TipoServico
    data_servico: date
    status: StatusServico
    cliente_nome: str
    duracao_horas: int

    class Config:
        orm_mode = True
