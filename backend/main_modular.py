"""
GestOnGo - Sistema Modular de Gestão de Serviços de Campo
Backend FastAPI com arquitetura modular baseada em feature flags

Módulos disponíveis:
- AQUA: Gestão de serviços de piscinas
- VERDE: Gestão de serviços de jardinagem  
- PHYTO: Gestão de fitoterapia e plantas medicinais

Cada módulo é carregado dinamicamente baseado nas variáveis de ambiente:
- FEATURE_AQUA=true/false
- FEATURE_VERDE=true/false  
- FEATURE_PHYTO=true/false
"""

import os
from typing import Dict, Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ====================================================================
# CONFIGURAÇÃO DE FEATURE FLAGS
# ====================================================================

def get_feature_flag(feature_name: str, default: bool = False) -> bool:
    """
    Lê uma feature flag das variáveis de ambiente
    
    Args:
        feature_name: Nome da feature (ex: 'FEATURE_AQUA')
        default: Valor padrão se a variável não existir
        
    Returns:
        True se a feature estiver ativa, False caso contrário
    """
    value = os.getenv(feature_name, str(default)).lower()
    return value in ('true', '1', 'yes', 'on', 'enabled')

# Leitura das feature flags
FEATURE_AQUA = get_feature_flag('FEATURE_AQUA', True)
FEATURE_VERDE = get_feature_flag('FEATURE_VERDE', True) 
FEATURE_PHYTO = get_feature_flag('FEATURE_PHYTO', False)

print("🔧 Feature Flags carregadas:")
print(f"   🌊 AQUA (Piscinas): {'✅ ATIVO' if FEATURE_AQUA else '❌ INATIVO'}")
print(f"   🌱 VERDE (Jardinagem): {'✅ ATIVO' if FEATURE_VERDE else '❌ INATIVO'}")
print(f"   🌿 PHYTO (Fitoterapia): {'✅ ATIVO' if FEATURE_PHYTO else '❌ INATIVO'}")

# ====================================================================
# INICIALIZAÇÃO DA APLICAÇÃO FASTAPI
# ====================================================================

app = FastAPI(
    title="GestOnGo API",
    description="Sistema modular de gestão de serviços de campo",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# ====================================================================
# CONFIGURAÇÃO DE MIDDLEWARE CORS
# ====================================================================

# CORS liberado para facilitar desenvolvimento
# Em produção, configurar origins específicas
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Em produção, especificar domínios
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

print("🌐 CORS configurado para permitir todas as origens")

# ====================================================================
# CARREGAMENTO DINÂMICO DE MÓDULOS
# ====================================================================

# Dicionário para armazenar o status dos módulos
modules_status: Dict[str, bool] = {}

# --- MÓDULO AQUA (Piscinas) ---
if FEATURE_AQUA:
    try:
        from modules.aqua.routers import aqua_router
        app.include_router(aqua_router, prefix="/aqua", tags=["Aqua - Piscinas"])
        modules_status["aqua"] = True
        print("🌊 Módulo AQUA carregado com sucesso (Prefix: /aqua)")
    except ImportError as e:
        print(f"❌ Erro ao carregar módulo AQUA: {e}")
        modules_status["aqua"] = False
else:
    modules_status["aqua"] = False
    print("⏭️ Módulo AQUA desativado por feature flag")

# --- MÓDULO VERDE (Jardinagem) ---
if FEATURE_VERDE:
    try:
        from modules.verde.routers import verde_router
        app.include_router(verde_router, prefix="/verde", tags=["Verde - Jardinagem"])
        modules_status["verde"] = True
        print("🌱 Módulo VERDE carregado com sucesso (Prefix: /verde)")
    except ImportError as e:
        print(f"❌ Erro ao carregar módulo VERDE: {e}")
        modules_status["verde"] = False
else:
    modules_status["verde"] = False
    print("⏭️ Módulo VERDE desativado por feature flag")

# --- MÓDULO PHYTO (Fitoterapia) ---
if FEATURE_PHYTO:
    try:
        from modules.phyto.routers import phyto_router
        app.include_router(phyto_router, prefix="/phyto", tags=["Phyto - Fitoterapia"])
        modules_status["phyto"] = True
        print("🌿 Módulo PHYTO carregado com sucesso (Prefix: /phyto)")
    except ImportError as e:
        print(f"❌ Erro ao carregar módulo PHYTO: {e}")
        modules_status["phyto"] = False
else:
    modules_status["phyto"] = False
    print("⏭️ Módulo PHYTO desativado por feature flag")

# ====================================================================
# ENDPOINTS PRINCIPAIS
# ====================================================================

@app.get("/", summary="Status da API", description="Retorna o status da API e módulos ativos")
async def root() -> Dict[str, Any]:
    """
    Endpoint raiz que retorna informações sobre o sistema e módulos ativos
    
    Returns:
        Dicionário com status da API e informações dos módulos
    """
    # Contar módulos ativos
    active_modules = [name for name, status in modules_status.items() if status]
    total_modules = len(modules_status)
    active_count = len(active_modules)
    
    return {
        "status": "GestOnGo API online",
        "version": "2.0.0",
        "description": "Sistema modular de gestão de serviços de campo",
        "modules": modules_status,
        "summary": {
            "total_modules": total_modules,
            "active_modules": active_count,
            "inactive_modules": total_modules - active_count,
            "active_module_names": active_modules
        },
        "endpoints": {
            "documentation": "/docs",
            "openapi_schema": "/openapi.json",
            "health_check": "/health"
        }
    }

@app.get("/health", summary="Health Check", description="Endpoint de verificação de saúde do sistema")
async def health_check() -> Dict[str, Any]:
    """
    Endpoint de health check para monitorização
    
    Returns:
        Status de saúde do sistema e módulos
    """
    return {
        "status": "healthy",
        "service": "GestOnGo API",
        "modules": modules_status,
        "features": {
            "aqua": FEATURE_AQUA,
            "verde": FEATURE_VERDE,
            "phyto": FEATURE_PHYTO
        }
    }

@app.get("/modules", summary="Informações dos Módulos", description="Detalhes sobre todos os módulos disponíveis")
async def get_modules_info() -> Dict[str, Any]:
    """
    Retorna informações detalhadas sobre todos os módulos
    
    Returns:
        Informações completas dos módulos e suas funcionalidades
    """
    return {
        "modules": {
            "aqua": {
                "name": "Aqua - Gestão de Piscinas",
                "description": "Módulo para gestão de serviços de piscinas, manutenção e limpeza",
                "prefix": "/aqua",
                "enabled": modules_status.get("aqua", False),
                "feature_flag": "FEATURE_AQUA"
            },
            "verde": {
                "name": "Verde - Gestão de Jardinagem", 
                "description": "Módulo para gestão de serviços de jardinagem e paisagismo",
                "prefix": "/verde",
                "enabled": modules_status.get("verde", False),
                "feature_flag": "FEATURE_VERDE"
            },
            "phyto": {
                "name": "Phyto - Fitoterapia",
                "description": "Módulo para gestão de plantas medicinais e fitoterapia",
                "prefix": "/phyto", 
                "enabled": modules_status.get("phyto", False),
                "feature_flag": "FEATURE_PHYTO"
            }
        },
        "usage": {
            "enable_module": "Set environment variable FEATURE_<MODULE>=true",
            "disable_module": "Set environment variable FEATURE_<MODULE>=false",
            "example": "FEATURE_AQUA=true FEATURE_VERDE=false FEATURE_PHYTO=true"
        }
    }

# ====================================================================
# INICIALIZAÇÃO DO SISTEMA
# ====================================================================

@app.on_event("startup")
async def startup_event():
    """Eventos executados no início da aplicação"""
    print("\n" + "="*60)
    print("🚀 GestOnGo API iniciada com sucesso!")
    print(f"📊 Módulos ativos: {len([m for m in modules_status.values() if m])}/{len(modules_status)}")
    print("📚 Documentação disponível em: /docs")
    print("🔧 Informações dos módulos: /modules")
    print("💚 Health check: /health")
    print("="*60 + "\n")

@app.on_event("shutdown") 
async def shutdown_event():
    """Eventos executados no encerramento da aplicação"""
    print("👋 GestOnGo API encerrada")

# ====================================================================
# PONTO DE ENTRADA PARA DESENVOLVIMENTO
# ====================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("🔧 Executando em modo desenvolvimento...")
    print("📍 Para produção, use: uvicorn main_modular:app --host 0.0.0.0 --port 8000")
    
    uvicorn.run(
        "main_modular:app",
        host="0.0.0.0", 
        port=8000,
        reload=True,
        log_level="info"
    )
