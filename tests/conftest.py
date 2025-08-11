"""
Configuração de testes para GestOnGo.

Este módulo configura fixtures e utilitários para testes da API.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app.core.database import Base, get_db
from backend.main import app

# Base de dados de teste em memória
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """Override da função get_db para usar base de dados de teste."""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    """Fixture que fornece um cliente de teste para a API."""
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as test_client:
        yield test_client
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def authenticated_client(client):
    """Fixture que fornece um cliente autenticado."""
    # Cria um utilizador
    user_data = {
        "nome": "Teste Usuario",
        "email": "teste@gestongo.pt",
        "senha": "senha123"
    }
    response = client.post("/utilizadores/", json=user_data)
    assert response.status_code == 201
    
    # Faz login
    login_data = {
        "username": "teste@gestongo.pt",
        "password": "senha123"
    }
    response = client.post("/utilizadores/login", data=login_data)
    assert response.status_code == 200
    
    token = response.json()["access_token"]
    
    # Retorna cliente com headers de autenticação
    client.headers.update({"Authorization": f"Bearer {token}"})
    return client


@pytest.fixture
def sample_cliente_data():
    """Dados de exemplo para criar um cliente."""
    return {
        "nome": "João Silva",
        "telefone": "912345678",
        "endereco": "Rua das Flores, 123, Lisboa",
        "observacoes": "Cliente preferencial"
    }


@pytest.fixture
def sample_servico_data():
    """Dados de exemplo para criar um serviço."""
    return {
        "tipo": "jardinagem",
        "data_servico": "2025-08-15",
        "duracao_horas": 3,
        "cliente_id": 1,
        "descricao": "Manutenção de jardim e poda de árvores"
    }
