"""
Esquemas Pydantic para utilizadores.

Os esquemas definem a forma como os dados são validados e serializados
ao entrar ou sair da API.
"""

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    nome: str


class UserCreate(UserBase):
    senha: str


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
