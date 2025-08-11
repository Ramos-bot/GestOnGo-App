#!/usr/bin/env python3
"""
Script de deploy para Replit - GestOnGo

Este script serve tanto o backend FastAPI quanto o frontend buildado
numa única porta para deployment no Replit.
"""

import os
import subprocess
import sys
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Importa a aplicação principal
sys.path.append(str(Path(__file__).parent))
from backend.main import app as fastapi_app


def build_frontend():
    """Faz build do frontend React."""
    print("🏗️ Fazendo build do frontend...")
    
    frontend_dir = Path(__file__).parent / "frontend"
    
    # Instala dependências
    result = subprocess.run(
        ["npm", "install"], 
        cwd=frontend_dir, 
        capture_output=True, 
        text=True
    )
    
    if result.returncode != 0:
        print(f"❌ Erro ao instalar dependências: {result.stderr}")
        return False
    
    # Faz build
    result = subprocess.run(
        ["npm", "run", "build"], 
        cwd=frontend_dir, 
        capture_output=True, 
        text=True
    )
    
    if result.returncode != 0:
        print(f"❌ Erro no build: {result.stderr}")
        return False
    
    print("✅ Build do frontend concluído!")
    return True


def create_production_app():
    """Cria aplicação FastAPI configurada para produção."""
    # Monta arquivos estáticos do frontend
    frontend_dist = Path(__file__).parent / "frontend" / "dist"
    
    if frontend_dist.exists():
        fastapi_app.mount("/static", StaticFiles(directory=frontend_dist), name="static")
        
        # Serve index.html na raiz
        @fastapi_app.get("/")
        async def serve_frontend():
            from fastapi.responses import FileResponse
            return FileResponse(frontend_dist / "index.html")
        
        print("✅ Frontend estático configurado!")
    else:
        print("⚠️ Diretório de build do frontend não encontrado!")
    
    return fastapi_app


def main():
    """Função principal de deploy."""
    print("🚀 Iniciando deploy do GestOnGo...")
    
    # Verifica se está no Replit
    if os.getenv("REPLIT_DB_URL"):
        print("📡 Deploy no Replit detectado")
    
    # Faz build do frontend
    if not build_frontend():
        print("❌ Falha no build do frontend")
        sys.exit(1)
    
    # Cria aplicação de produção
    app = create_production_app()
    
    # Obtém porta do ambiente (Replit usa PORT)
    port = int(os.getenv("PORT", 8000))
    
    print(f"🌟 Iniciando servidor na porta {port}...")
    print(f"📍 API: http://localhost:{port}/docs")
    print(f"🌐 Frontend: http://localhost:{port}/")
    
    # Inicia servidor
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )


if __name__ == "__main__":
    main()
