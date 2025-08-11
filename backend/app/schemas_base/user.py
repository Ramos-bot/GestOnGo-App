"""
Schemas Pydantic para User - Versão base
Validação e serialização de dados de utilizadores
"""

from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    """Schema base partilhado para utilizadores"""
    nome: str
    email: EmailStr
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    """Schema para criação de utilizadores"""
    senha: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "nome": "João Silva",
                "email": "joao@exemplo.pt",
                "senha": "senha_forte_123",
                "is_active": True
            }
        }

class UserResponse(UserBase):
    """Schema para resposta com dados do utilizador (sem senha)"""
    id: int
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "nome": "João Silva", 
                "email": "joao@exemplo.pt",
                "is_active": True
            }
        }

class UserLogin(BaseModel):
    """Schema para login de utilizadores"""
    email: EmailStr
    senha: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "joao@exemplo.pt",
                "senha": "senha_forte_123"
            }
        }

class Token(BaseModel):
    """Schema para resposta de token JWT"""
    access_token: str
    token_type: str = "bearer"
    
    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer"
            }
        }
