"""
Utilitários de segurança para a aplicação GestOnGo.

Inclui funções para gerar e verificar hashes de senhas, criar e validar
tokens JWT para autenticação, e parâmetros de configuração relacionados
com a segurança. Estas funções são utilizadas nos controladores de
utilizadores para gerir o processo de login e protecção de rotas.
"""

from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models_base.user import User

# Chave secreta usada para assinar os tokens. Em produção, esta chave deverá
# ser gerada de forma segura e nunca ser exposta no código fonte.
SECRET_KEY = "gestongo_chave_secreta_forte_2025"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto de hashing de senhas. O bcrypt é um algoritmo robusto e amplamente
# utilizado. A biblioteca passlib facilita a sua utilização e gestão de versões.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Esquema OAuth2 para extração do token Bearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def gerar_hash_senha(senha: str) -> str:
    """Gera um hash a partir de uma senha em texto plano."""
    return pwd_context.hash(senha)


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """Verifica se a senha corresponde ao hash fornecido."""
    return pwd_context.verify(senha, hash_senha)


def criar_token_acesso(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Cria um token JWT para acesso autenticado."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verificar_token(token: str) -> Optional[str]:
    """Verifica e decodifica um token JWT."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        return email
    except JWTError:
        return None


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    """Obtém o utilizador actual a partir do token JWT."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    
    return user
