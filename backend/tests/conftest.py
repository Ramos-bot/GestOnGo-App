"""
Configurações e fixtures para testes do GestOnGo Backend
"""
import pytest
from fastapi.testclient import TestClient
import os

# Configurar variáveis de ambiente para testes
os.environ["FEATURE_AQUA"] = "true"
os.environ["FEATURE_VERDE"] = "true" 
os.environ["FEATURE_PHYTO"] = "false"

@pytest.fixture
def client():
    """
    Fixture que fornece um cliente de teste para a API
    """
    try:
        from main_modular import app
        return TestClient(app)
    except ImportError:
        # Se main_modular não existir, retorna None
        return None

@pytest.fixture
def test_user():
    """
    Fixture com dados de usuário para testes
    """
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    }
