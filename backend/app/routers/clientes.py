"""
Rotas para gerir clientes.

Este módulo permite criar, listar, actualizar e eliminar clientes. 
As operações estão protegidas por autenticação: apenas um utilizador 
autenticado pode executar estas acções.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from ..core.database import SessionLocal
from ..models.cliente import Cliente
from ..schemas.cliente import ClienteCreate, ClienteResponse, ClienteUpdate
from .users import get_current_user


router = APIRouter(prefix="/clientes", tags=["Clientes"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def criar_cliente(
    cliente: ClienteCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Cria um novo cliente. Requer autenticação."""
    # Verifica se já existe cliente com o mesmo nome
    cliente_existente = db.query(Cliente).filter(Cliente.nome == cliente.nome).first()
    if cliente_existente:
        raise HTTPException(
            status_code=400, 
            detail=f"Já existe um cliente com o nome '{cliente.nome}'"
        )
    
    novo_cliente = Cliente(**cliente.dict())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente


@router.get("/", response_model=List[ClienteResponse])
def listar_clientes(
    skip: int = Query(0, ge=0, description="Número de registos a saltar"),
    limit: int = Query(100, ge=1, le=100, description="Número máximo de registos"),
    nome: str = Query(None, description="Filtrar por nome (busca parcial)"),
    db: Session = Depends(get_db), 
    current_user=Depends(get_current_user)
):
    """Lista clientes com filtros opcionais. Requer autenticação."""
    query = db.query(Cliente)
    
    # Filtro por nome (busca parcial, insensível a maiúsculas)
    if nome:
        query = query.filter(Cliente.nome.ilike(f"%{nome}%"))
    
    clientes = query.offset(skip).limit(limit).all()
    return clientes


@router.get("/{cliente_id}", response_model=ClienteResponse)
def obter_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Obtém um cliente específico pelo ID. Requer autenticação."""
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente


@router.put("/{cliente_id}", response_model=ClienteResponse)
def actualizar_cliente(
    cliente_id: int,
    cliente_update: ClienteUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Actualiza um cliente existente. Requer autenticação."""
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    # Actualiza apenas os campos fornecidos
    dados_actualizacao = cliente_update.dict(exclude_unset=True)
    for campo, valor in dados_actualizacao.items():
        setattr(cliente, campo, valor)
    
    db.commit()
    db.refresh(cliente)
    return cliente


@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Elimina um cliente. Requer autenticação."""
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    # Verifica se o cliente tem serviços associados
    if cliente.servicos:
        raise HTTPException(
            status_code=400,
            detail="Não é possível eliminar cliente com serviços associados"
        )
    
    db.delete(cliente)
    db.commit()
    return None


@router.get("/estatisticas/resumo")
def obter_estatisticas_clientes(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Obtém estatísticas básicas dos clientes. Requer autenticação."""
    total_clientes = db.query(Cliente).count()
    clientes_com_telefone = db.query(Cliente).filter(Cliente.telefone.isnot(None)).count()
    clientes_com_endereco = db.query(Cliente).filter(Cliente.endereco.isnot(None)).count()
    
    return {
        "total_clientes": total_clientes,
        "clientes_com_telefone": clientes_com_telefone,
        "clientes_com_endereco": clientes_com_endereco,
        "percentagem_telefone": round((clientes_com_telefone / total_clientes * 100) if total_clientes > 0 else 0, 1),
        "percentagem_endereco": round((clientes_com_endereco / total_clientes * 100) if total_clientes > 0 else 0, 1),
    }
