"""
Configuração da base de dados SQLAlchemy para GestOnGo
Sistema modular com suporte para versão base e módulos pagos
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# URL da base de dados (SQLite para desenvolvimento)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./gestongo.db")

# Configurar engine SQLite com check_same_thread=False para FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)

# Criar SessionLocal para ligações à base de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para todos os modelos ORM
Base = declarative_base()

def get_db():
    """
    Dependência para obter uma sessão da base de dados
    Usado nas rotas FastAPI com Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def criar_tabelas():
    """
    Criar todas as tabelas na base de dados
    Chamado no arranque da aplicação
    """
    # Importar todos os modelos para garantir que estão registados
    from app.models_base import user, cliente
    
    # Módulos opcionais (podem ser comentados para desativar)
    try:
        from modules.verde.models import servico_jardim
        print("✅ Módulo Verde (Jardinagem) carregado")
    except ImportError:
        print("ℹ️ Módulo Verde não disponível")
    
    try:
        from modules.aqua.models import servico_piscina
        print("✅ Módulo Aqua (Piscinas) carregado")
    except ImportError:
        print("ℹ️ Módulo Aqua não disponível")
    
    # Criar todas as tabelas
    Base.metadata.create_all(bind=engine)
    print("📊 Base de dados inicializada com sucesso")
