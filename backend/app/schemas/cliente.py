"""
Esquemas Pydantic para clientes.

Define os modelos de dados utilizados na criação, leitura e listagem de
clientes. A inclusão dos serviços associados permite obter a relação
completa entre clientes e serviços, quando necessário.
"""

from typing import List, Optional
import re

from pydantic import BaseModel, validator

from .servico import ServicoResponse


class ClienteBase(BaseModel):
    nome: str
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    observacoes: Optional[str] = None

    @validator("nome")
    def validar_nome(cls, v: str) -> str:
        """Valida se o nome tem pelo menos 2 caracteres."""
        if len(v.strip()) < 2:
            raise ValueError("Nome deve ter pelo menos 2 caracteres")
        return v.strip().title()

    @validator("telefone")
    def validar_telefone(cls, v: Optional[str]) -> Optional[str]:
        """Valida formato de telefone português."""
        if v is None or v.strip() == "":
            return None
        
        # Remove espaços e caracteres especiais
        telefone_limpo = re.sub(r'[^\d+]', '', v)
        
        # Padrões válidos para Portugal
        padroes_validos = [
            r'^\+351\d{9}$',  # +351xxxxxxxxx
            r'^351\d{9}$',    # 351xxxxxxxxx
            r'^\d{9}$',       # xxxxxxxxx (9 dígitos)
        ]
        
        if not any(re.match(padrao, telefone_limpo) for padrao in padroes_validos):
            raise ValueError("Formato de telefone inválido. Use +351xxxxxxxxx ou xxxxxxxxx")
        
        return telefone_limpo

    @validator("endereco")
    def validar_endereco(cls, v: Optional[str]) -> Optional[str]:
        """Limpa e valida o endereço."""
        if v is None:
            return None
        endereco_limpo = v.strip()
        return endereco_limpo if endereco_limpo else None


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    """Schema para actualização parcial de clientes."""
    nome: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    observacoes: Optional[str] = None

    @validator("nome")
    def validar_nome(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and len(v.strip()) < 2:
            raise ValueError("Nome deve ter pelo menos 2 caracteres")
        return v.strip().title() if v else None

    @validator("telefone")
    def validar_telefone(cls, v: Optional[str]) -> Optional[str]:
        if v is None or v.strip() == "":
            return None
        
        telefone_limpo = re.sub(r'[^\d+]', '', v)
        padroes_validos = [
            r'^\+351\d{9}$',
            r'^351\d{9}$',
            r'^\d{9}$',
        ]
        
        if not any(re.match(padrao, telefone_limpo) for padrao in padroes_validos):
            raise ValueError("Formato de telefone inválido")
        
        return telefone_limpo


class ClienteResponse(ClienteBase):
    id: int
    servicos: List[ServicoResponse] = []

    class Config:
        orm_mode = True
