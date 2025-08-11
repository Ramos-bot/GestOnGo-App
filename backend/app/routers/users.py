"""
Rotas relacionadas com utilizadores.

Este módulo define endpoints para criar novos utilizadores, efectuar login e
obter o utilizador actual com base no token. Inclui um esquema de
autenticação OAuth2 básico usando senhas e tokens JWT.
"""

from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..core.database import SessionLocal
from ..core.security import (
    criar_token_acesso,
    gerar_hash_senha,
    verificar_senha,
    verificar_token,
)
from ..models.user import User
from ..schemas.user import UserCreate, UserResponse


router = APIRouter(prefix="/utilizadores", tags=["Utilizadores"])

# Define o esquema OAuth2 que irá extrair o token do cabeçalho Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/utilizadores/login")


def get_db():
    """Cria e encerra sessões de base de dados conforme necessário."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def criar_utilizador(utilizador: UserCreate, db: Session = Depends(get_db)):
    """Cria um novo utilizador."""
    db_user = db.query(User).filter(User.email == utilizador.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registado")
    hash_senha = gerar_hash_senha(utilizador.senha)
    novo_user = User(nome=utilizador.nome, email=utilizador.email, hash_senha=hash_senha)
    db.add(novo_user)
    db.commit()
    db.refresh(novo_user)
    return novo_user


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Endpoint de autenticação."""
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verificar_senha(form_data.password, user.hash_senha):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    access_token_expires = timedelta(minutes=30)
    access_token = criar_token_acesso(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    """Obtém o utilizador actual com base no token JWT fornecido."""
    email = verificar_token(token)
    if email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido ou expirado")
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Utilizador não encontrado")
    return user
