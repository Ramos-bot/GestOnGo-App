#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌐 Abridor Automático do Replit - GestOnGo
Abre URLs importantes do Replit automaticamente
"""

import webbrowser
import time

def open_replit_urls():
    """Abre URLs importantes do Replit"""
    
    urls = {
        "🏠 Replit Editor": "https://replit.com/@tiago1982santos/GestOnGo-App",
        "🚀 API em Produção": "https://gestongo-app.tiago1982santos.repl.co",
        "📚 Documentação da API": "https://gestongo-app.tiago1982santos.repl.co/docs",
        "💓 Health Check": "https://gestongo-app.tiago1982santos.repl.co/health",
        "🧩 Status dos Módulos": "https://gestongo-app.tiago1982santos.repl.co/modules"
    }
    
    print("🌐 Abrindo URLs do Replit...")
    print("=" * 50)
    
    for description, url in urls.items():
        print(f"🔗 {description}: {url}")
        webbrowser.open(url)
        time.sleep(1)  # Pausa entre aberturas
    
    print("=" * 50)
    print("✅ Todas as URLs foram abertas no browser!")

if __name__ == "__main__":
    open_replit_urls()
