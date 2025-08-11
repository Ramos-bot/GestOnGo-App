"""
Schemas Pydantic para Cliente - Versão base
Validação e serialização de dados de clientes
"""

from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    """Schema base partilhado para clientes"""
    nome: str
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    observacoes: Optional[str] = None

class ClienteCreate(ClienteBase):
    """Schema para criação de clientes"""
    pass
    
    class Config:
        json_schema_extra = {
            "example": {
                "nome": "Maria Santos",
                "telefone": "+351 912 345 678",
                "endereco": "Rua das Flores, 123, 1000-000 Lisboa",
                "observacoes": "Cliente preferencial, sempre pontual nos pagamentos"
            }
        }

class ClienteResponse(ClienteBase):
    """Schema para resposta com dados do cliente"""
    id: int
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "nome": "Maria Santos",
                "telefone": "+351 912 345 678", 
                "endereco": "Rua das Flores, 123, 1000-000 Lisboa",
                "observacoes": "Cliente preferencial, sempre pontual nos pagamentos"
            }
        }

class ClienteUpdate(BaseModel):
    """Schema para actualização de clientes (todos os campos opcionais)"""
    nome: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    observacoes: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "telefone": "+351 912 999 888",
                "observacoes": "Actualização: novo número de telefone"
            }
        }
