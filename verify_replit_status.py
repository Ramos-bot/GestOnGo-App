#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 Verificador de Status do GestOnGo no Replit
Verifica se o servidor está online e funcionando corretamente
"""

import requests
import json
from datetime import datetime
import time

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header():
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("🔍 VERIFICADOR DE STATUS - GestOnGo Replit")
    print("=" * 50)
    print(f"{Colors.END}")

def check_endpoint(url, name, timeout=10):
    """Verifica um endpoint específico"""
    try:
        print(f"{Colors.YELLOW}🔄 Testando {name}:{Colors.END} {url}")
        
        response = requests.get(url, timeout=timeout)
        
        if response.status_code == 200:
            print(f"{Colors.GREEN}✅ {name}: ONLINE{Colors.END}")
            
            # Tentar mostrar resposta se for JSON
            try:
                if 'application/json' in response.headers.get('content-type', ''):
                    data = response.json()
                    print(f"{Colors.BLUE}   📄 Resposta: {json.dumps(data, indent=2, ensure_ascii=False)[:200]}...{Colors.END}")
                else:
                    content = response.text[:100]
                    print(f"{Colors.BLUE}   📄 Conteúdo: {content}...{Colors.END}")
            except:
                print(f"{Colors.BLUE}   📄 Status: {response.status_code}{Colors.END}")
                
            return True
            
        else:
            print(f"{Colors.RED}❌ {name}: HTTP {response.status_code}{Colors.END}")
            return False
            
    except requests.exceptions.ConnectTimeout:
        print(f"{Colors.RED}❌ {name}: TIMEOUT - Servidor não responde{Colors.END}")
        return False
    except requests.exceptions.ConnectionError:
        print(f"{Colors.RED}❌ {name}: CONEXÃO FALHOU - Servidor offline{Colors.END}")
        return False
    except Exception as e:
        print(f"{Colors.RED}❌ {name}: ERRO - {str(e)}{Colors.END}")
        return False

def main():
    print_header()
    
    # URL base correta
    base_url = "https://gestongo-app.tiago1982santos.repl.co"
    
    print(f"{Colors.BOLD}🎯 URL Base:{Colors.END} {base_url}")
    print(f"{Colors.BOLD}🕒 Timestamp:{Colors.END} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Endpoints para testar
    endpoints = [
        ("/", "🏠 Página Principal"),
        ("/health", "💓 Health Check"),
        ("/modules", "🧩 Módulos"),
        ("/docs", "📚 Documentação"),
        ("/openapi.json", "🔧 OpenAPI Schema")
    ]
    
    online_count = 0
    total_count = len(endpoints)
    
    for endpoint, name in endpoints:
        url = f"{base_url}{endpoint}"
        if check_endpoint(url, name):
            online_count += 1
        print()
        time.sleep(1)  # Pequena pausa entre requests
    
    # Resultado final
    print("=" * 50)
    if online_count == total_count:
        print(f"{Colors.GREEN}{Colors.BOLD}🎉 STATUS: TODOS OS ENDPOINTS ONLINE!{Colors.END}")
        print(f"{Colors.GREEN}✅ {online_count}/{total_count} endpoints funcionando{Colors.END}")
    elif online_count > 0:
        print(f"{Colors.YELLOW}{Colors.BOLD}⚠️  STATUS: PARCIALMENTE ONLINE{Colors.END}")
        print(f"{Colors.YELLOW}⚠️  {online_count}/{total_count} endpoints funcionando{Colors.END}")
    else:
        print(f"{Colors.RED}{Colors.BOLD}💥 STATUS: SERVIDOR COMPLETAMENTE OFFLINE{Colors.END}")
        print(f"{Colors.RED}❌ {online_count}/{total_count} endpoints funcionando{Colors.END}")
        print()
        print(f"{Colors.YELLOW}🔧 AÇÕES RECOMENDADAS:{Colors.END}")
        print(f"   1. Abrir: https://replit.com/@tiago1982santos/GestOnGo-App")
        print(f"   2. Clicar no botão 'Run' ▶️")
        print(f"   3. Verificar console por erros")
        print(f"   4. Configurar Secrets necessários")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
