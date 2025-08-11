"""
Testes para autenticação de utilizadores.
"""

import pytest


def test_criar_utilizador(client):
    """Testa criação de novo utilizador."""
    user_data = {
        "nome": "Teste Usuario",
        "email": "novo@gestongo.pt",
        "senha": "senha123"
    }
    
    response = client.post("/utilizadores/", json=user_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["nome"] == user_data["nome"]
    assert "id" in data
    assert data["is_active"] is True


def test_criar_utilizador_email_duplicado(client):
    """Testa que não é possível criar utilizador com email duplicado."""
    user_data = {
        "nome": "Teste Usuario",
        "email": "duplicado@gestongo.pt",
        "senha": "senha123"
    }
    
    # Cria primeiro utilizador
    response1 = client.post("/utilizadores/", json=user_data)
    assert response1.status_code == 201
    
    # Tenta criar segundo utilizador com mesmo email
    response2 = client.post("/utilizadores/", json=user_data)
    assert response2.status_code == 400
    assert "já registado" in response2.json()["detail"]


def test_login_sucesso(client):
    """Testa login com credenciais corretas."""
    # Cria utilizador
    user_data = {
        "nome": "Teste Usuario",
        "email": "login@gestongo.pt",
        "senha": "senha123"
    }
    client.post("/utilizadores/", json=user_data)
    
    # Faz login
    login_data = {
        "username": "login@gestongo.pt",
        "password": "senha123"
    }
    response = client.post("/utilizadores/login", data=login_data)
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_credenciais_invalidas(client):
    """Testa login com credenciais inválidas."""
    login_data = {
        "username": "inexistente@gestongo.pt",
        "password": "senhaerrada"
    }
    response = client.post("/utilizadores/login", data=login_data)
    
    assert response.status_code == 401
    assert "Credenciais inválidas" in response.json()["detail"]


def test_acesso_rota_protegida_sem_token(client):
    """Testa acesso a rota protegida sem token."""
    response = client.get("/clientes/")
    assert response.status_code == 401


def test_acesso_rota_protegida_com_token(authenticated_client):
    """Testa acesso a rota protegida com token válido."""
    response = authenticated_client.get("/clientes/")
    assert response.status_code == 200
