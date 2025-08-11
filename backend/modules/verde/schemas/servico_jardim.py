"""
Schemas Pydantic para ServicoJardim - Módulo Verde
Validação e serialização de serviços de jardinagem
"""

from pydantic import BaseModel, validator
from datetime import date
from typing import Optional

class ServicoJardimBase(BaseModel):
    """Schema base para serviços de jardinagem"""
    tipo: str = "jardinagem"
    data_servico: date
    duracao_horas: int
    descricao: Optional[str] = None
    cliente_id: int
    
    @validator('tipo')
    def validar_tipo(cls, v):
        """Validar que o tipo é sempre 'jardinagem'"""
        if v != "jardinagem":
            raise ValueError("Tipo deve ser 'jardinagem' para este módulo")
        return v
    
    @validator('duracao_horas')
    def validar_duracao(cls, v):
        """Validar que a duração é positiva"""
        if v <= 0:
            raise ValueError("Duração deve ser maior que 0 horas")
        if v > 24:
            raise ValueError("Duração não pode exceder 24 horas")
        return v

class ServicoJardimCreate(ServicoJardimBase):
    """Schema para criação de serviços de jardinagem"""
    pass
    
    class Config:
        json_schema_extra = {
            "example": {
                "tipo": "jardinagem",
                "data_servico": "2025-08-15",
                "duracao_horas": 4,
                "descricao": "Corte de relva, poda de arbustos e limpeza do jardim",
                "cliente_id": 1
            }
        }

class ServicoJardimResponse(ServicoJardimBase):
    """Schema para resposta com dados do serviço"""
    id: int
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "tipo": "jardinagem",
                "data_servico": "2025-08-15",
                "duracao_horas": 4,
                "descricao": "Corte de relva, poda de arbustos e limpeza do jardim",
                "cliente_id": 1
            }
        }

class ServicoJardimUpdate(BaseModel):
    """Schema para actualização de serviços (campos opcionais)"""
    data_servico: Optional[date] = None
    duracao_horas: Optional[int] = None
    descricao: Optional[str] = None
    
    @validator('duracao_horas')
    def validar_duracao(cls, v):
        """Validar duração se fornecida"""
        if v is not None:
            if v <= 0:
                raise ValueError("Duração deve ser maior que 0 horas")
            if v > 24:
                raise ValueError("Duração não pode exceder 24 horas")
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "duracao_horas": 5,
                "descricao": "Serviço actualizado: incluir limpeza de piscina também"
            }
        }
