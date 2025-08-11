"""
GestOnGo - Sistema Modular de Gestão de Serviços de Campo
Aplicação FastAPI com arquitectura modular para serviços de jardinagem e piscinas
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# Importar configuração do Replit
from app.core.replit_config import config

# Importar configuração da base de dados
from app.core.database import criar_tabelas

# Importar routers da versão base
from app.routers_base.users import router as users_router
from app.routers_base.clientes import router as clientes_router

# Importar routers dos módulos (podem ser comentados para desativar)
try:
    from modules.verde.routers.servicos_jardim import router as verde_router
    MODULO_VERDE_DISPONIVEL = config.MODULO_VERDE_ATIVO
    if MODULO_VERDE_DISPONIVEL:
        print("✅ Módulo Verde (Jardinagem) registado")
except ImportError:
    MODULO_VERDE_DISPONIVEL = False
    print("⚠️ Módulo Verde não disponível")

try:
    from modules.aqua.routers.servicos_piscina import router as aqua_router
    MODULO_AQUA_DISPONIVEL = config.MODULO_AQUA_ATIVO
    if MODULO_AQUA_DISPONIVEL:
        print("✅ Módulo Aqua (Piscinas) registado")
except ImportError:
    MODULO_AQUA_DISPONIVEL = False
    print("⚠️ Módulo Aqua não disponível")

# Criar aplicação FastAPI
app = FastAPI(
    title=config.APP_NAME,
    description="Sistema modular de gestão de serviços de campo com suporte para jardinagem e piscinas",
    version=config.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    debug=config.DEBUG
)

# Configurar CORS com configurações do Replit
cors_settings = config.get_cors_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_settings["allow_origins"],
    allow_credentials=cors_settings["allow_credentials"],
    allow_methods=cors_settings["allow_methods"],
    allow_headers=cors_settings["allow_headers"],
)

# Registar routers da versão base (sempre disponíveis)
app.include_router(users_router)
app.include_router(clientes_router)

# Registar routers dos módulos (condicionais)
if MODULO_VERDE_DISPONIVEL:
    app.include_router(verde_router)

if MODULO_AQUA_DISPONIVEL:
    app.include_router(aqua_router)

@app.on_event("startup")
async def startup_event():
    """
    Eventos de arranque da aplicação
    - Criar tabelas da base de dados
    - Criar utilizador admin padrão se não existir
    """
    print("🚀 A inicializar GestOnGo...")
    
    # Criar tabelas
    criar_tabelas()
    
    # Criar utilizador admin padrão
    from sqlalchemy.orm import sessionmaker
    from app.core.database import engine
    from app.models_base.user import User
    from app.core.security import gerar_hash_senha
    
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        # Verificar se já existe utilizador admin
        admin_user = db.query(User).filter(User.email == "admin@gestongo.com").first()
        
        if not admin_user:
            # Criar utilizador admin padrão
            admin_user = User(
                nome="Administrador",
                email="admin@gestongo.com",
                hash_senha=gerar_hash_senha("admin123"),
                is_active=True
            )
            db.add(admin_user)
            db.commit()
            print("👤 Utilizador admin criado: admin@gestongo.com / admin123")
        else:
            print("👤 Utilizador admin já existe")
            
    except Exception as e:
        print(f"❌ Erro ao criar utilizador admin: {e}")
        db.rollback()
    finally:
        db.close()
    
    print("✅ GestOnGo iniciado com sucesso!")
    print(f"📚 Documentação disponível em: http://localhost:8000/docs")
    print(f"🔧 Módulos activos: Base{', Verde' if MODULO_VERDE_DISPONIVEL else ''}{', Aqua' if MODULO_AQUA_DISPONIVEL else ''}")

@app.get("/")
async def root():
    """
    Endpoint raiz com informações do sistema
    """
    modulos_activos = ["Base"]
    if MODULO_VERDE_DISPONIVEL:
        modulos_activos.append("Verde (Jardinagem)")
    if MODULO_AQUA_DISPONIVEL:
        modulos_activos.append("Aqua (Piscinas)")
    
    return {
        "mensagem": "Bem-vindo ao GestOnGo!",
        "versao": config.APP_VERSION,
        "descricao": "Sistema modular de gestão de serviços de campo",
        "ambiente": config.ENVIRONMENT,
        "modulos_activos": modulos_activos,
        "documentacao": "/docs",
        "credenciais_teste": {
            "email": "admin@gestongo.com",
            "senha": "admin123"
        }
    }

@app.get("/config")
async def config_status():
    """
    Endpoint para verificar configuração (sem mostrar valores sensíveis)
    """
    secrets_status = config.verify_secrets()
    
    return {
        "app_name": config.APP_NAME,
        "version": config.APP_VERSION,
        "environment": config.ENVIRONMENT,
        "debug": config.DEBUG,
        "database_type": config.DATABASE_TYPE,
        "modules": {
            "verde": config.MODULO_VERDE_ATIVO,
            "aqua": config.MODULO_AQUA_ATIVO
        },
        "cors_origins_count": len(config.ALLOWED_ORIGINS),
        "secrets_configured": {
            secret: info["configured"] 
            for secret, info in secrets_status.items()
        }
    }

@app.get("/health")
async def health_check():
    """
    Endpoint de verificação de saúde do sistema
    """
    return {
        "status": "ok",
        "modulos": {
            "base": True,
            "verde": MODULO_VERDE_DISPONIVEL,
            "aqua": MODULO_AQUA_DISPONIVEL
        }
    }
