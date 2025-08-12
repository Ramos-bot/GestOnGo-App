#!/usr/bin/env python3
"""
Teste End-to-End do GestOnGo
Testa a integração completa Frontend ↔ Backend
"""

import requests
import json
import time
from datetime import datetime

class GestOnGoE2ETest:
    def __init__(self, backend_url, frontend_url=None):
        self.backend_url = backend_url.rstrip('/')
        self.frontend_url = frontend_url.rstrip('/') if frontend_url else None
        self.token = None
        
    def test_backend_health(self):
        """Testa se o backend está online"""
        print("🔍 Testando Backend Health...")
        
        try:
            response = requests.get(f"{self.backend_url}/", timeout=10)
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Backend online: {data.get('mensagem', 'OK')}")
                print(f"   📱 Versão: {data.get('versao', 'N/A')}")
                print(f"   🔧 Módulos: {', '.join(data.get('modulos_activos', []))}")
                return True
            else:
                print(f"   ❌ Backend retornou: {response.status_code}")
                return False
        except Exception as e:
            print(f"   ❌ Erro ao conectar backend: {str(e)}")
            return False
    
    def test_backend_config(self):
        """Testa configuração do backend"""
        print("\n🔧 Testando Configuração Backend...")
        
        try:
            response = requests.get(f"{self.backend_url}/config", timeout=10)
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Config acessível")
                print(f"   🌍 Environment: {data.get('environment')}")
                print(f"   🔐 Secrets configurados: {data.get('secrets_configured')}")
                
                secrets = data.get('secrets_configured', {})
                all_secrets = all(secrets.values())
                if all_secrets:
                    print("   ✅ Todos os secrets configurados")
                else:
                    print("   ⚠️ Alguns secrets em falta")
                
                return all_secrets
            else:
                print(f"   ❌ Config endpoint retornou: {response.status_code}")
                return False
        except Exception as e:
            print(f"   ❌ Erro ao acessar config: {str(e)}")
            return False
    
    def test_authentication(self):
        """Testa autenticação JWT"""
        print("\n🔐 Testando Autenticação...")
        
        try:
            # Tentar fazer login
            login_data = {
                "username": "admin@gestongo.com",
                "password": "admin123"
            }
            
            response = requests.post(
                f"{self.backend_url}/utilizadores/login",
                data=login_data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                self.token = data.get('access_token')
                print(f"   ✅ Login bem-sucedido")
                print(f"   🎫 Token type: {data.get('token_type')}")
                return True
            else:
                print(f"   ❌ Login falhou: {response.status_code}")
                try:
                    error_data = response.json()
                    print(f"   📄 Erro: {error_data}")
                except:
                    print(f"   📄 Resposta: {response.text}")
                return False
                
        except Exception as e:
            print(f"   ❌ Erro na autenticação: {str(e)}")
            return False
    
    def test_protected_endpoints(self):
        """Testa endpoints protegidos"""
        if not self.token:
            print("\n❌ Não é possível testar endpoints protegidos - sem token")
            return False
        
        print("\n🛡️ Testando Endpoints Protegidos...")
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        endpoints = [
            ("/clientes", "GET", "Listar Clientes"),
            ("/verde/servicos", "GET", "Serviços de Jardim"),
            ("/aqua/servicos", "GET", "Serviços de Piscina"),
        ]
        
        success_count = 0
        
        for endpoint, method, description in endpoints:
            try:
                response = requests.get(
                    f"{self.backend_url}{endpoint}",
                    headers=headers,
                    timeout=10
                )
                
                if response.status_code == 200:
                    data = response.json()
                    count = len(data) if isinstance(data, list) else "N/A"
                    print(f"   ✅ {description}: {count} items")
                    success_count += 1
                else:
                    print(f"   ❌ {description}: {response.status_code}")
                    
            except Exception as e:
                print(f"   ❌ {description}: {str(e)}")
        
        return success_count == len(endpoints)
    
    def test_frontend(self):
        """Testa se o frontend está acessível"""
        if not self.frontend_url:
            print("\n⏭️ Teste de frontend ignorado - URL não fornecida")
            return True
        
        print(f"\n🌐 Testando Frontend: {self.frontend_url}")
        
        try:
            response = requests.get(self.frontend_url, timeout=10)
            if response.status_code == 200:
                print("   ✅ Frontend acessível")
                print(f"   📄 Tamanho: {len(response.text)} bytes")
                
                # Verificar se contém conteúdo React
                if "react" in response.text.lower() or "vite" in response.text.lower():
                    print("   ✅ Aplicação React detectada")
                    return True
                else:
                    print("   ⚠️ Conteúdo não parece ser React")
                    return True
            else:
                print(f"   ❌ Frontend retornou: {response.status_code}")
                return False
        except Exception as e:
            print(f"   ❌ Erro ao acessar frontend: {str(e)}")
            return False
    
    def run_full_test(self):
        """Executa teste completo"""
        print("🧪 GestOnGo End-to-End Test")
        print("=" * 50)
        print(f"🕐 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🔗 Backend URL: {self.backend_url}")
        if self.frontend_url:
            print(f"🌐 Frontend URL: {self.frontend_url}")
        
        tests = [
            ("Backend Health", self.test_backend_health),
            ("Backend Config", self.test_backend_config),
            ("Authentication", self.test_authentication),
            ("Protected Endpoints", self.test_protected_endpoints),
            ("Frontend Access", self.test_frontend),
        ]
        
        results = []
        
        for test_name, test_func in tests:
            try:
                result = test_func()
                results.append((test_name, result))
            except Exception as e:
                print(f"\n❌ Erro no teste {test_name}: {str(e)}")
                results.append((test_name, False))
        
        print("\n" + "=" * 50)
        print("📊 RESUMO DOS TESTES:")
        
        passed_tests = 0
        for test_name, passed in results:
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"   {status}: {test_name}")
            if passed:
                passed_tests += 1
        
        success_rate = (passed_tests / len(results)) * 100
        print(f"\n🎯 Taxa de Sucesso: {success_rate:.1f}% ({passed_tests}/{len(results)})")
        
        if success_rate >= 80:
            print("🎉 SISTEMA FUNCIONANDO CORRETAMENTE!")
        elif success_rate >= 60:
            print("⚠️ Sistema parcialmente funcional - verificar falhas")
        else:
            print("❌ Sistema com problemas críticos")
        
        return success_rate >= 80

if __name__ == "__main__":
    # URLs para teste
    backend_url = "https://gestongo-app.ramos-bot.repl.co"
    frontend_url = None  # Será definido após deploy
    
    # Executar teste
    tester = GestOnGoE2ETest(backend_url, frontend_url)
    success = tester.run_full_test()
    
    exit(0 if success else 1)
