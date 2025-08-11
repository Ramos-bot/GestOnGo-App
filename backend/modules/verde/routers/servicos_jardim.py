"""
Router de serviços de jardinagem - Módulo Verde
CRUD de serviços com validação específica para jardinagem
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.core.security import get_current_user
from app.models_base.user import User
from app.models_base.cliente import Cliente
from modules.verde.models.servico_jardim import ServicoJardim
from modules.verde.schemas.servico_jardim import (
    ServicoJardimCreate, 
    ServicoJardimResponse, 
    ServicoJardimUpdate
)

router = APIRouter(prefix="/servicos-jardim", tags=["Módulo Verde - Jardinagem"])

@router.post("/", response_model=ServicoJardimResponse, status_code=status.HTTP_201_CREATED)
def criar_servico_jardim(
    servico: ServicoJardimCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Criar novo serviço de jardinagem (requer autenticação)
    
    - **tipo**: Tipo de serviço (fixo: 'jardinagem')
    - **data_servico**: Data em que o serviço será realizado
    - **duracao_horas**: Duração do serviço em horas (1-24)
    - **descricao**: Descrição detalhada do serviço (opcional)
    - **cliente_id**: ID do cliente associado
    """
    # Verificar se cliente existe
    cliente = db.query(Cliente).filter(Cliente.id == servico.cliente_id).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )
    
    # Garantir que o tipo é 'jardinagem'
    servico_data = servico.dict()
    servico_data["tipo"] = "jardinagem"
    
    db_servico = ServicoJardim(**servico_data)
    db.add(db_servico)
    db.commit()
    db.refresh(db_servico)
    
    return db_servico

@router.get("/", response_model=List[ServicoJardimResponse])
def listar_servicos_jardim(
    offset: int = Query(0, ge=0, description="Número de registos a saltar"),
    limit: int = Query(50, ge=1, le=100, description="Número máximo de registos"),
    cliente_id: int = Query(None, description="Filtrar por ID do cliente"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Listar serviços de jardinagem com paginação (requer autenticação)
    
    Ordenados por data de serviço (mais recentes primeiro)
    
    - **offset**: Número de registos a saltar (padrão: 0)
    - **limit**: Número máximo de registos (padrão: 50, máximo: 100)
    - **cliente_id**: Filtrar serviços de um cliente específico (opcional)
    """
    query = db.query(ServicoJardim)
    
    # Filtrar por cliente se especificado
    if cliente_id:
        query = query.filter(ServicoJardim.cliente_id == cliente_id)
    
    # Ordenar por data de serviço (descendente)
    servicos = query.order_by(ServicoJardim.data_servico.desc()).offset(offset).limit(limit).all()
    
    return servicos

@router.get("/{servico_id}", response_model=ServicoJardimResponse)
def obter_servico_jardim(
    servico_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Obter serviço de jardinagem por ID (requer autenticação)
    """
    servico = db.query(ServicoJardim).filter(ServicoJardim.id == servico_id).first()
    
    if not servico:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Serviço de jardinagem não encontrado"
        )
    
    return servico

@router.put("/{servico_id}", response_model=ServicoJardimResponse)
def actualizar_servico_jardim(
    servico_id: int,
    servico_update: ServicoJardimUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Actualizar serviço de jardinagem (requer autenticação)
    """
    servico = db.query(ServicoJardim).filter(ServicoJardim.id == servico_id).first()
    
    if not servico:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Serviço de jardinagem não encontrado"
        )
    
    # Actualizar apenas os campos fornecidos
    update_data = servico_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(servico, field, value)
    
    db.commit()
    db.refresh(servico)
    
    return servico

@router.delete("/{servico_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_servico_jardim(
    servico_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Eliminar serviço de jardinagem (requer autenticação)
    """
    servico = db.query(ServicoJardim).filter(ServicoJardim.id == servico_id).first()
    
    if not servico:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Serviço de jardinagem não encontrado"
        )
    
    db.delete(servico)
    db.commit()
    
    return None
