"""
Teste da API GestOnGo no Replit com username correto
URL do projeto: https://replit.com/@tiago1982santos/GestOnGo-App
"""

import requests
import json
from datetime import datetime

def test_gestongo_replit_api():
    print("🔍 Testando GestOnGo API no Replit")
    print("=" * 50)
    print(f"🕐 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"👤 Username: tiago1982santos")
    print(f"📁 Projeto: GestOnGo-App")
    
    # URLs baseadas no username correto
    base_url = "https://gestongo-app.tiago1982santos.repl.co"
    
    endpoints_to_test = [
        ("", "API Root"),
        ("/health", "Health Check"),
        ("/modules", "Modules Info"),
        ("/docs", "API Documentation"),
        ("/openapi.json", "OpenAPI Schema")
    ]
    
    print(f"\n🌐 URL Base: {base_url}")
    
    working_endpoints = []
    
    for endpoint, description in endpoints_to_test:
        url = f"{base_url}{endpoint}"
        
        try:
            print(f"\n🔍 Testando {description}...")
            print(f"   URL: {url}")
            
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                print(f"   ✅ Status: {response.status_code} - OK")
                
                # Tentar fazer parse do JSON
                try:
                    data = response.json()
                    print(f"   📊 Resposta JSON:")
                    
                    if endpoint == "":
                        # Endpoint raiz
                        if "status" in data:
                            print(f"      📝 Status: {data['status']}")
                        if "modules" in data:
                            print(f"      🔧 Módulos: {data['modules']}")
                        if "version" in data:
                            print(f"      🏷️ Versão: {data['version']}")
                    
                    elif endpoint == "/health":
                        # Health check
                        if "status" in data:
                            print(f"      💚 Health: {data['status']}")
                        if "features" in data:
                            print(f"      🎛️ Features: {data['features']}")
                    
                    elif endpoint == "/modules":
                        # Módulos
                        if "modules" in data:
                            modules = data["modules"]
                            for module_name, module_info in modules.items():
                                enabled = module_info.get("enabled", False)
                                status_icon = "✅" if enabled else "❌"
                                print(f"      {status_icon} {module_name}: {module_info.get('name', 'N/A')}")
                    
                    else:
                        print(f"      📄 Dados recebidos: {len(str(data))} chars")
                        
                except json.JSONDecodeError:
                    print(f"   📄 Resposta HTML/Text (length: {len(response.text)})")
                
                working_endpoints.append((url, description))
                
            elif response.status_code == 404:
                print(f"   ❌ Status: 404 - Endpoint não encontrado")
            else:
                print(f"   ⚠️ Status: {response.status_code}")
                
        except requests.exceptions.Timeout:
            print(f"   ⏰ Timeout - Servidor pode estar lento")
        except requests.exceptions.ConnectionError:
            print(f"   🔌 Erro de conexão - Servidor pode estar offline")
        except Exception as e:
            print(f"   ❌ Erro: {str(e)}")
    
    print("\n" + "=" * 50)
    print("📊 RESUMO DOS TESTES:")
    
    if working_endpoints:
        print(f"✅ {len(working_endpoints)} endpoint(s) funcionando:")
        for url, desc in working_endpoints:
            print(f"   🔗 {desc}: {url}")
        
        print(f"\n🎉 API GESTONGO ESTÁ ONLINE!")
        print(f"📚 Documentação: {base_url}/docs")
        print(f"💚 Health Check: {base_url}/health")
        
        return True
    else:
        print("❌ Nenhum endpoint funcionando")
        print("\n🔧 POSSÍVEIS PROBLEMAS:")
        print("   1. Servidor não está executando")
        print("   2. Porta 8000 não está exposta")
        print("   3. Erro na aplicação - verificar logs")
        print("   4. Secrets não configurados")
        
        return False

if __name__ == "__main__":
    success = test_gestongo_replit_api()
    exit(0 if success else 1)
