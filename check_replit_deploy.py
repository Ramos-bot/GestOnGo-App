"""
Script para verificar o status do deploy no Replit
Testa diferentes URLs possíveis do projeto GestOnGo
"""

import requests
import json
from datetime import datetime

def test_url(url, description):
    """Testa uma URL e retorna o status"""
    try:
        print(f"\n🔍 Testando {description}...")
        print(f"   URL: {url}")
        
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print(f"   ✅ Status: {response.status_code} - OK")
            
            # Tentar fazer parse do JSON se possível
            try:
                data = response.json()
                if isinstance(data, dict):
                    if "mensagem" in data:
                        print(f"   📝 Mensagem: {data['mensagem']}")
                    if "versao" in data:
                        print(f"   🏷️ Versão: {data['versao']}")
                    if "modulos_activos" in data:
                        print(f"   🔧 Módulos: {', '.join(data['modulos_activos'])}")
                    if "ambiente" in data:
                        print(f"   🌍 Ambiente: {data['ambiente']}")
            except:
                print(f"   📄 Conteúdo HTML recebido (length: {len(response.text)})")
            
            return True
        else:
            print(f"   ❌ Status: {response.status_code}")
            return False
            
    except requests.exceptions.Timeout:
        print(f"   ⏰ Timeout - Servidor pode estar a inicializar")
        return False
    except requests.exceptions.ConnectionError:
        print(f"   🔌 Erro de conexão - URL pode não existir")
        return False
    except Exception as e:
        print(f"   ❌ Erro: {str(e)}")
        return False

def main():
    print("🔍 Verificação do Deploy GestOnGo no Replit")
    print("=" * 60)
    print(f"🕐 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # URLs possíveis do Replit
    urls_to_test = [
        ("https://gestongo-app.ramos-bot.repl.co", "URL Principal (novo formato)"),
        ("https://gestongo-app.ramos-bot.repl.co/", "URL Principal com /"),
        ("https://gestongo-app.ramos-bot.repl.co/health", "Health Check"),
        ("https://gestongo-app.ramos-bot.repl.co/config", "Config Status"),
        ("https://gestongo-app.ramos-bot.repl.co/docs", "API Documentation"),
        ("https://replit.com/@Ramos-bot/GestOnGo-App", "Replit Editor"),
        ("https://gestongo-app--ramos-bot.repl.co", "URL Alternativa"),
        ("https://gestongo--ramos-bot.repl.co", "URL Encurtada"),
    ]
    
    working_urls = []
    
    for url, description in urls_to_test:
        if test_url(url, description):
            working_urls.append(url)
    
    print("\n" + "=" * 60)
    print("📊 RESUMO DOS TESTES:")
    
    if working_urls:
        print(f"✅ {len(working_urls)} URL(s) funcionando:")
        for url in working_urls:
            print(f"   🔗 {url}")
    else:
        print("❌ Nenhuma URL encontrada funcionando")
        print("\n🔧 POSSÍVEIS SOLUÇÕES:")
        print("   1. Verificar se o projeto foi importado no Replit")
        print("   2. Verificar se o servidor está a executar")
        print("   3. Verificar configuração dos secrets")
        print("   4. Verificar logs do Replit para erros")
    
    print(f"\n📋 PRÓXIMOS PASSOS:")
    print(f"   1. Abrir https://replit.com/@Ramos-bot")
    print(f"   2. Procurar projeto 'GestOnGo-App'")
    print(f"   3. Clicar 'Run' se não estiver a executar")
    print(f"   4. Configurar secrets na aba 'Secrets'")
    print(f"   5. Verificar logs na aba 'Console'")

if __name__ == "__main__":
    main()
