"""
Testes para operações CRUD de serviços.
"""

import pytest


def test_criar_servico(authenticated_client, sample_cliente_data, sample_servico_data):
    """Testa criação de novo serviço."""
    # Cria cliente primeiro
    cliente_response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    cliente_id = cliente_response.json()["id"]
    
    # Actualiza dados do serviço com ID do cliente
    sample_servico_data["cliente_id"] = cliente_id
    
    # Cria serviço
    response = authenticated_client.post("/servicos/", json=sample_servico_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["tipo"] == sample_servico_data["tipo"]
    assert data["data_servico"] == sample_servico_data["data_servico"]
    assert data["duracao_horas"] == sample_servico_data["duracao_horas"]
    assert data["cliente_id"] == cliente_id


def test_criar_servico_cliente_inexistente(authenticated_client, sample_servico_data):
    """Testa criação de serviço com cliente inexistente."""
    sample_servico_data["cliente_id"] = 999
    
    response = authenticated_client.post("/servicos/", json=sample_servico_data)
    assert response.status_code == 404
    assert "Cliente não encontrado" in response.json()["detail"]


def test_criar_servico_tipo_invalido(authenticated_client, sample_cliente_data, sample_servico_data):
    """Testa criação de serviço com tipo inválido."""
    # Cria cliente
    cliente_response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    cliente_id = cliente_response.json()["id"]
    
    # Tipo inválido
    sample_servico_data["cliente_id"] = cliente_id
    sample_servico_data["tipo"] = "tipo_invalido"
    
    response = authenticated_client.post("/servicos/", json=sample_servico_data)
    assert response.status_code == 422  # Validation error


def test_criar_servico_data_passado(authenticated_client, sample_cliente_data, sample_servico_data):
    """Testa criação de serviço com data no passado."""
    # Cria cliente
    cliente_response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    cliente_id = cliente_response.json()["id"]
    
    # Data no passado
    sample_servico_data["cliente_id"] = cliente_id
    sample_servico_data["data_servico"] = "2020-01-01"
    
    response = authenticated_client.post("/servicos/", json=sample_servico_data)
    assert response.status_code == 422


def test_listar_servicos(authenticated_client, sample_cliente_data, sample_servico_data):
    """Testa listagem de serviços."""
    # Cria cliente e serviço
    cliente_response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    cliente_id = cliente_response.json()["id"]
    
    sample_servico_data["cliente_id"] = cliente_id
    authenticated_client.post("/servicos/", json=sample_servico_data)
    
    # Lista serviços
    response = authenticated_client.get("/servicos/")
    assert response.status_code == 200
    
    servicos = response.json()
    assert len(servicos) == 1
    assert servicos[0]["tipo"] == sample_servico_data["tipo"]


def test_filtrar_servicos_por_tipo(authenticated_client, sample_cliente_data):
    """Testa filtragem de serviços por tipo."""
    # Cria cliente
    cliente_response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    cliente_id = cliente_response.json()["id"]
    
    # Cria serviços de diferentes tipos
    servicos = [
        {
            "tipo": "jardinagem",
            "data_servico": "2025-08-15",
            "duracao_horas": 3,
            "cliente_id": cliente_id
        },
        {
            "tipo": "piscina",
            "data_servico": "2025-08-16",
            "duracao_horas": 2,
            "cliente_id": cliente_id
        }
    ]
    
    for servico in servicos:
        authenticated_client.post("/servicos/", json=servico)
    
    # Filtra por jardinagem
    response = authenticated_client.get("/servicos/?tipo=jardinagem")
    assert response.status_code == 200
    
    resultado = response.json()
    assert len(resultado) == 1
    assert resultado[0]["tipo"] == "jardinagem"


def test_obter_servico_por_id(authenticated_client, sample_cliente_data, sample_servico_data):
    """Testa obtenção de serviço por ID."""
    # Cria cliente e serviço
    cliente_response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    cliente_id = cliente_response.json()["id"]
    
    sample_servico_data["cliente_id"] = cliente_id
    create_response = authenticated_client.post("/servicos/", json=sample_servico_data)
    servico_id = create_response.json()["id"]
    
    # Obtém serviço
    response = authenticated_client.get(f"/servicos/{servico_id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == servico_id
    assert data["tipo"] == sample_servico_data["tipo"]


def test_actualizar_servico(authenticated_client, sample_cliente_data, sample_servico_data):
    """Testa actualização de serviço."""
    # Cria cliente e serviço
    cliente_response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    cliente_id = cliente_response.json()["id"]
    
    sample_servico_data["cliente_id"] = cliente_id
    create_response = authenticated_client.post("/servicos/", json=sample_servico_data)
    servico_id = create_response.json()["id"]
    
    # Actualiza serviço
    update_data = {"duracao_horas": 5, "status": "concluido"}
    response = authenticated_client.put(f"/servicos/{servico_id}", json=update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["duracao_horas"] == 5
    assert data["status"] == "concluido"


def test_eliminar_servico(authenticated_client, sample_cliente_data, sample_servico_data):
    """Testa eliminação de serviço."""
    # Cria cliente e serviço
    cliente_response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    cliente_id = cliente_response.json()["id"]
    
    sample_servico_data["cliente_id"] = cliente_id
    create_response = authenticated_client.post("/servicos/", json=sample_servico_data)
    servico_id = create_response.json()["id"]
    
    # Elimina serviço
    response = authenticated_client.delete(f"/servicos/{servico_id}")
    assert response.status_code == 204
    
    # Verifica que serviço foi eliminado
    get_response = authenticated_client.get(f"/servicos/{servico_id}")
    assert get_response.status_code == 404


def test_dashboard_servicos(authenticated_client, sample_cliente_data):
    """Testa endpoint de dashboard com estatísticas."""
    # Cria cliente
    cliente_response = authenticated_client.post("/clientes/", json=sample_cliente_data)
    cliente_id = cliente_response.json()["id"]
    
    # Cria alguns serviços
    servicos = [
        {"tipo": "jardinagem", "data_servico": "2025-08-15", "duracao_horas": 3, "cliente_id": cliente_id},
        {"tipo": "piscina", "data_servico": "2025-08-16", "duracao_horas": 2, "cliente_id": cliente_id}
    ]
    
    for servico in servicos:
        authenticated_client.post("/servicos/", json=servico)
    
    # Obtém dashboard
    response = authenticated_client.get("/servicos/estatisticas/dashboard")
    assert response.status_code == 200
    
    data = response.json()
    assert "total_servicos" in data
    assert "por_tipo" in data
    assert data["total_servicos"] == 2
    assert data["por_tipo"]["jardinagem"] == 1
    assert data["por_tipo"]["piscina"] == 1
