"""
Script para testar múltiplas variações de URLs do Replit
Baseado em diferentes padrões de nomenclatura
"""

import requests
import time

def test_replit_urls():
    print("🔍 Testando variações de URLs do Replit...")
    
    # Possíveis variações baseadas em padrões do Replit
    base_patterns = [
        "gestongo-app",
        "gestongo",
        "gestongoapp", 
        "gestongoappp",
        "gestongo-backend",
        "gestongo-api"
    ]
    
    user_patterns = [
        "ramos-bot",
        "ramosbot", 
        "tiago",
        "peralta-ramos-bot"
    ]
    
    url_formats = [
        "https://{project}.{user}.repl.co",
        "https://{project}--{user}.repl.co",
        "https://{user}.repl.co/{project}",
        "https://replit.com/@{user}/{project}"
    ]
    
    found_urls = []
    
    for project in base_patterns:
        for user in user_patterns:
            for url_format in url_formats:
                url = url_format.format(project=project, user=user)
                
                try:
                    print(f"🔍 Testando: {url}")
                    response = requests.get(url, timeout=5)
                    
                    if response.status_code == 200:
                        print(f"   ✅ ENCONTRADO! Status: {response.status_code}")
                        
                        # Tentar fazer parse do JSON
                        try:
                            data = response.json()
                            if "status" in data or "mensagem" in data:
                                print(f"   📊 API Response: {data}")
                                found_urls.append((url, "API"))
                            else:
                                found_urls.append((url, "HTML"))
                        except:
                            print(f"   📄 HTML content found")
                            found_urls.append((url, "HTML"))
                    
                    elif response.status_code == 404:
                        print(f"   ❌ 404 - Não encontrado")
                    else:
                        print(f"   ⚠️ Status: {response.status_code}")
                        
                except requests.exceptions.Timeout:
                    print(f"   ⏰ Timeout")
                except requests.exceptions.ConnectionError:
                    print(f"   🔌 Conexão falhada")
                except Exception as e:
                    print(f"   ❌ Erro: {str(e)}")
                
                # Pausa pequena para não sobrecarregar
                time.sleep(0.2)
    
    print("\n" + "="*60)
    print("📊 RESULTADOS ENCONTRADOS:")
    
    if found_urls:
        for url, type_found in found_urls:
            print(f"   ✅ {type_found}: {url}")
    else:
        print("   ❌ Nenhuma URL funcional encontrada")
    
    return found_urls

if __name__ == "__main__":
    found = test_replit_urls()
    
    if found:
        print(f"\n🎉 Encontradas {len(found)} URL(s) funcionais!")
        print("🔧 Use uma destas URLs para testar a API")
    else:
        print("\n💡 DICAS PARA DEBUG:")
        print("   1. Verificar se o Repl está a executar")
        print("   2. Verificar nome exato do projeto no Replit")
        print("   3. Verificar se a porta 8000 está exposta")
        print("   4. Verificar logs de erro no console do Replit")
