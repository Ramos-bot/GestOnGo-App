"""
Router de utilizadores - Versão base
Autenticação JWT e gestão de utilizadores
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from app.core.database import get_db
from app.core.security import (
    gerar_hash_senha, 
    verificar_senha, 
    criar_token_acesso, 
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from app.models_base.user import User
from app.schemas_base.user import UserCreate, UserResponse, Token

router = APIRouter(prefix="/utilizadores", tags=["Utilizadores"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def criar_utilizador(user: UserCreate, db: Session = Depends(get_db)):
    """
    Criar novo utilizador no sistema
    
    - **nome**: Nome completo do utilizador
    - **email**: Email único para login
    - **senha**: Senha em texto simples (será hasheada)
    - **is_active**: Utilizador activo (opcional, padrão True)
    """
    # Verificar se email já existe
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já está registado no sistema"
        )
    
    # Criar novo utilizador com senha hasheada
    hashed_password = gerar_hash_senha(user.senha)
    db_user = User(
        nome=user.nome,
        email=user.email,
        hash_senha=hashed_password,
        is_active=user.is_active
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@router.post("/login", response_model=Token)
def login_utilizador(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Login de utilizador com email e senha
    
    Retorna token JWT válido por 30 minutos
    """
    # Buscar utilizador por email
    user = db.query(User).filter(User.email == form_data.username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verificar senha
    if not verificar_senha(form_data.password, user.hash_senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verificar se utilizador está activo
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Utilizador inactivo"
        )
    
    # Criar token de acesso
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = criar_token_acesso(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def obter_utilizador_actual(current_user: User = Depends(get_current_user)):
    """
    Obter dados do utilizador autenticado
    
    Requer token JWT válido no cabeçalho Authorization
    """
    return current_user
