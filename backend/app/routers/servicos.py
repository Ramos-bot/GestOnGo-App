"""
Rotas para gerir serviços.

Permite criar, listar, actualizar e eliminar serviços. Cada serviço está
associado a um cliente e inclui informações sobre o tipo de serviço,
data e duração. As operações exigem autenticação.
"""

from typing import List, Optional
from datetime import date, datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import and_, func

from ..core.database import SessionLocal
from ..models.servico import Servico
from ..models.cliente import Cliente
from ..schemas.servico import (
    ServicoCreate, 
    ServicoResponse, 
    ServicoUpdate, 
    ServicoResumo,
    TipoServico,
    StatusServico
)
from .users import get_current_user


router = APIRouter(prefix="/servicos", tags=["Serviços"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ServicoResponse, status_code=status.HTTP_201_CREATED)
def criar_servico(
    servico: ServicoCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Cria um novo serviço associado a um cliente. Requer autenticação."""
    cliente = db.query(Cliente).filter(Cliente.id == servico.cliente_id).first()
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    # Verifica se já existe serviço para o mesmo cliente na mesma data
    servico_existente = db.query(Servico).filter(
        and_(
            Servico.cliente_id == servico.cliente_id,
            Servico.data_servico == servico.data_servico,
            Servico.status != StatusServico.CANCELADO
        )
    ).first()
    
    if servico_existente:
        raise HTTPException(
            status_code=400,
            detail=f"Já existe um serviço agendado para este cliente em {servico.data_servico}"
        )
    
    novo_servico = Servico(**servico.dict())
    db.add(novo_servico)
    db.commit()
    db.refresh(novo_servico)
    return novo_servico


@router.get("/", response_model=List[ServicoResponse])
def listar_servicos(
    skip: int = Query(0, ge=0, description="Número de registos a saltar"),
    limit: int = Query(100, ge=1, le=100, description="Número máximo de registos"),
    tipo: Optional[TipoServico] = Query(None, description="Filtrar por tipo de serviço"),
    status: Optional[StatusServico] = Query(None, description="Filtrar por status"),
    data_inicio: Optional[date] = Query(None, description="Data início (YYYY-MM-DD)"),
    data_fim: Optional[date] = Query(None, description="Data fim (YYYY-MM-DD)"),
    cliente_id: Optional[int] = Query(None, description="Filtrar por cliente"),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Lista serviços com filtros opcionais. Requer autenticação."""
    query = db.query(Servico)
    
    # Aplicar filtros
    if tipo:
        query = query.filter(Servico.tipo == tipo)
    if status:
        query = query.filter(Servico.status == status)
    if data_inicio:
        query = query.filter(Servico.data_servico >= data_inicio)
    if data_fim:
        query = query.filter(Servico.data_servico <= data_fim)
    if cliente_id:
        query = query.filter(Servico.cliente_id == cliente_id)
    
    # Ordenar por data de serviço (mais recentes primeiro)
    query = query.order_by(Servico.data_servico.desc())
    
    servicos = query.offset(skip).limit(limit).all()
    return servicos


@router.get("/resumo", response_model=List[ServicoResumo])
def listar_servicos_resumo(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Lista serviços em formato resumido com informação do cliente."""
    servicos = db.query(
        Servico.id,
        Servico.tipo,
        Servico.data_servico,
        Servico.status,
        Servico.duracao_horas,
        Cliente.nome.label("cliente_nome")
    ).join(Cliente).order_by(Servico.data_servico.desc()).offset(skip).limit(limit).all()
    
    return [
        ServicoResumo(
            id=s.id,
            tipo=s.tipo,
            data_servico=s.data_servico,
            status=s.status,
            duracao_horas=s.duracao_horas,
            cliente_nome=s.cliente_nome
        )
        for s in servicos
    ]


@router.get("/{servico_id}", response_model=ServicoResponse)
def obter_servico(
    servico_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Obtém um serviço específico pelo ID. Requer autenticação."""
    servico = db.query(Servico).filter(Servico.id == servico_id).first()
    if servico is None:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    return servico


@router.put("/{servico_id}", response_model=ServicoResponse)
def actualizar_servico(
    servico_id: int,
    servico_update: ServicoUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Actualiza um serviço existente. Requer autenticação."""
    servico = db.query(Servico).filter(Servico.id == servico_id).first()
    if servico is None:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    
    # Actualiza apenas os campos fornecidos
    dados_actualizacao = servico_update.dict(exclude_unset=True)
    for campo, valor in dados_actualizacao.items():
        setattr(servico, campo, valor)
    
    db.commit()
    db.refresh(servico)
    return servico


@router.delete("/{servico_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_servico(
    servico_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Elimina um serviço. Requer autenticação."""
    servico = db.query(Servico).filter(Servico.id == servico_id).first()
    if servico is None:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    
    db.delete(servico)
    db.commit()
    return None


@router.get("/estatisticas/dashboard")
def obter_dashboard_servicos(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Obtém estatísticas para dashboard. Requer autenticação."""
    hoje = date.today()
    inicio_mes = hoje.replace(day=1)
    fim_mes = (inicio_mes + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    
    # Estatísticas gerais
    total_servicos = db.query(Servico).count()
    servicos_mes = db.query(Servico).filter(
        and_(Servico.data_servico >= inicio_mes, Servico.data_servico <= fim_mes)
    ).count()
    
    # Por tipo
    servicos_jardinagem = db.query(Servico).filter(Servico.tipo == TipoServico.JARDINAGEM).count()
    servicos_piscina = db.query(Servico).filter(Servico.tipo == TipoServico.PISCINA).count()
    
    # Por status
    servicos_agendados = db.query(Servico).filter(Servico.status == StatusServico.AGENDADO).count()
    servicos_concluidos = db.query(Servico).filter(Servico.status == StatusServico.CONCLUIDO).count()
    
    # Próximos serviços (próximos 7 dias)
    proxima_semana = hoje + timedelta(days=7)
    proximos_servicos = db.query(Servico).filter(
        and_(
            Servico.data_servico >= hoje,
            Servico.data_servico <= proxima_semana,
            Servico.status == StatusServico.AGENDADO
        )
    ).count()
    
    return {
        "total_servicos": total_servicos,
        "servicos_este_mes": servicos_mes,
        "por_tipo": {
            "jardinagem": servicos_jardinagem,
            "piscina": servicos_piscina
        },
        "por_status": {
            "agendados": servicos_agendados,
            "concluidos": servicos_concluidos
        },
        "proximos_7_dias": proximos_servicos
    }
