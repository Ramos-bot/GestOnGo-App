"""
Ponto de entrada da aplicação FastAPI - GestOnGo.

Este ficheiro inicializa a base de dados, cria as tabelas e regista
as rotas de utilizadores, clientes e serviços. Para executar a API,
utilize o comando:

    uvicorn backend.main:app --reload --port 8000

Durante o desenvolvimento em Portugal, poderá querer modificar a
configuração para reflectir o fuso horário local ou outras
particularidades regionais.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .app.core.database import Base, engine, SessionLocal
from .app.routers import users, clientes, servicos
from .app.core.security import gerar_hash_senha
from .app.models.user import User

# Cria todas as tabelas definidas nos modelos.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GestOnGo - Gestão de Serviços de Campo",
    description="API para gestão de serviços de jardinagem e manutenção de piscinas",
    version="0.1.0",
)

# Configuração CORS para permitir acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cria utilizador administrador por defeito se não existir
def criar_utilizador_admin():
    db = SessionLocal()
    try:
        admin_existente = db.query(User).filter(User.email == "admin@gestongo.pt").first()
        if not admin_existente:
            hash_senha = gerar_hash_senha("gestongo2025")
            admin_user = User(
                nome="Administrador GestOnGo",
                email="admin@gestongo.pt",
                hash_senha=hash_senha,
                is_active=True
            )
            db.add(admin_user)
            db.commit()
            print("✅ Utilizador administrador criado: admin@gestongo.pt / gestongo2025")
    finally:
        db.close()

# Cria o utilizador admin na inicialização
criar_utilizador_admin()

# Registo das rotas
app.include_router(users.router)
app.include_router(clientes.router)
app.include_router(servicos.router)

@app.get("/")
async def root():
    """Endpoint de boas-vindas da API GestOnGo."""
    return {
        "mensagem": "Bem-vindo à API GestOnGo! 🌿",
        "versao": "0.1.0",
        "docs": "/docs",
        "servicos": ["jardinagem", "piscina"]
    }
