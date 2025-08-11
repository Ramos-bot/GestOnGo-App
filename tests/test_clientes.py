"""
Testes para operações CRUD de clientes.
"""

import pytest


def test_criar_cliente(authenticated_client, sample_cliente_data):
    """Testa criação de novo cliente."""
    response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["nome"] == sample_cliente_data["nome"]
    assert data["telefone"] == sample_cliente_data["telefone"]
    assert data["endereco"] == sample_cliente_data["endereco"]
    assert "id" in data


def test_listar_clientes_vazio(authenticated_client):
    """Testa listagem quando não há clientes."""
    response = authenticated_client.get("/clientes/")
    assert response.status_code == 200
    assert response.json() == []


def test_listar_clientes_com_dados(authenticated_client, sample_cliente_data):
    """Testa listagem com clientes existentes."""
    # Cria cliente
    authenticated_client.post("/clientes/", json=sample_cliente_data)
    
    # Lista clientes
    response = authenticated_client.get("/clientes/")
    assert response.status_code == 200
    
    clientes = response.json()
    assert len(clientes) == 1
    assert clientes[0]["nome"] == sample_cliente_data["nome"]


def test_obter_cliente_por_id(authenticated_client, sample_cliente_data):
    """Testa obtenção de cliente por ID."""
    # Cria cliente
    create_response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    cliente_id = create_response.json()["id"]
    
    # Obtém cliente
    response = authenticated_client.get(f"/clientes/{cliente_id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == cliente_id
    assert data["nome"] == sample_cliente_data["nome"]


def test_obter_cliente_inexistente(authenticated_client):
    """Testa obtenção de cliente que não existe."""
    response = authenticated_client.get("/clientes/999")
    assert response.status_code == 404


def test_actualizar_cliente(authenticated_client, sample_cliente_data):
    """Testa actualização de cliente."""
    # Cria cliente
    create_response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    cliente_id = create_response.json()["id"]
    
    # Actualiza cliente
    update_data = {"nome": "João Santos", "telefone": "987654321"}
    response = authenticated_client.put(f"/clientes/{cliente_id}", json=update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["nome"] == update_data["nome"]
    assert data["telefone"] == update_data["telefone"]
    assert data["endereco"] == sample_cliente_data["endereco"]  # Não alterado


def test_eliminar_cliente(authenticated_client, sample_cliente_data):
    """Testa eliminação de cliente."""
    # Cria cliente
    create_response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    cliente_id = create_response.json()["id"]
    
    # Elimina cliente
    response = authenticated_client.delete(f"/clientes/{cliente_id}")
    assert response.status_code == 204
    
    # Verifica que cliente foi eliminado
    get_response = authenticated_client.get(f"/clientes/{cliente_id}")
    assert get_response.status_code == 404


def test_filtrar_clientes_por_nome(authenticated_client):
    """Testa filtragem de clientes por nome."""
    # Cria múltiplos clientes
    clientes = [
        {"nome": "João Silva", "telefone": "911111111"},
        {"nome": "Maria Santos", "telefone": "922222222"},
        {"nome": "João Pedro", "telefone": "933333333"}
    ]
    
    for cliente in clientes:
        authenticated_client.post("/clientes/", json=cliente)
    
    # Filtra por "João"
    response = authenticated_client.get("/clientes/?nome=João")
    assert response.status_code == 200
    
    resultado = response.json()
    assert len(resultado) == 2
    assert all("João" in cliente["nome"] for cliente in resultado)


def test_paginacao_clientes(authenticated_client):
    """Testa paginação na listagem de clientes."""
    # Cria múltiplos clientes
    for i in range(5):
        cliente_data = {"nome": f"Cliente {i}", "telefone": f"91000000{i}"}
        authenticated_client.post("/clientes/", json=cliente_data)
    
    # Primeira página (limite 3)
    response = authenticated_client.get("/clientes/?limit=3&skip=0")
    assert response.status_code == 200
    assert len(response.json()) == 3
    
    # Segunda página
    response = authenticated_client.get("/clientes/?limit=3&skip=3")
    assert response.status_code == 200
    assert len(response.json()) == 2
