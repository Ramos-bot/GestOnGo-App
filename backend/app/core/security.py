"""
Utilitários de segurança para a aplicação GestOnGo.

Inclui funções para gerar e verificar hashes de senhas, criar e validar
tokens JWT para autenticação, e parâmetros de configuração relacionados
com a segurança. Estas funções são utilizadas nos controladores de
utilizadores para gerir o processo de login e protecção de rotas.
"""

from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext

# Chave secreta usada para assinar os tokens. Em produção, esta chave deverá
# ser gerada de forma segura e nunca ser exposta no código fonte.
SECRET_KEY = "gestongo_chave_secreta_forte_2025"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto de hashing de senhas. O bcrypt é um algoritmo robusto e amplamente
# utilizado. A biblioteca passlib facilita a sua utilização e gestão de versões.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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
