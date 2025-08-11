#!/usr/bin/env python3
"""
Script de verificação para execução no Replit
Verifica se todos os secrets e configurações estão corretos
"""

import os
import sys
import subprocess

def check_python_version():
    """Verifica versão do Python"""
    version = sys.version_info
    print(f"🐍 Python: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 11:
        print("   ✅ Versão adequada (3.11+)")
        return True
    else:
        print("   ❌ Versão inadequada (precisa 3.11+)")
        return False

def check_environment_variables():
    """Verifica se as variáveis de ambiente estão configuradas"""
    required_vars = [
        "JWT_SECRET_KEY",
        "DATABASE_URL", 
        "APP_NAME",
        "ENVIRONMENT",
        "MODULO_VERDE_ATIVO",
        "MODULO_AQUA_ATIVO"
    ]
    
    print("\n🔐 Verificando Secrets/Environment Variables:")
    all_configured = True
    
    for var in required_vars:
        value = os.environ.get(var)
        if value:
            print(f"   ✅ {var}: configurado ({len(value)} chars)")
        else:
            print(f"   ❌ {var}: NÃO CONFIGURADO")
            all_configured = False
    
    return all_configured

def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    print("\n📦 Verificando Dependências Críticas:")
    
    required_packages = [
        "fastapi",
        "uvicorn", 
        "sqlalchemy",
        "pydantic",
        "passlib",
        "python-jose",
        "python-multipart"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"   ✅ {package}: instalado")
        except ImportError:
            print(f"   ❌ {package}: NÃO INSTALADO")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n📋 Para instalar pacotes em falta:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False
    
    return True

def check_file_structure():
    """Verifica estrutura de arquivos"""
    print("\n📁 Verificando Estrutura de Arquivos:")
    
    required_files = [
        "backend/main_modular.py",
        "backend/app/core/replit_config.py",
        "backend/app/core/security.py",
        "backend/requirements.txt",
        ".replit"
    ]
    
    all_files_exist = True
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"   ✅ {file_path}: existe")
        else:
            print(f"   ❌ {file_path}: NÃO ENCONTRADO")
            all_files_exist = False
    
    return all_files_exist

def test_import_config():
    """Testa se a configuração pode ser importada"""
    print("\n⚙️ Testando Import da Configuração:")
    
    try:
        sys.path.append('./backend')
        from app.core.replit_config import config
        
        print(f"   ✅ Config importada com sucesso")
        print(f"   📱 App: {config.APP_NAME} v{config.APP_VERSION}")
        print(f"   🌍 Environment: {config.ENVIRONMENT}")
        print(f"   🔧 Debug: {config.DEBUG}")
        print(f"   🔐 JWT Algorithm: {config.JWT_ALGORITHM}")
        
        # Verificar secrets
        secrets_status = config.verify_secrets()
        all_secrets_ok = all(info["configured"] for info in secrets_status.values())
        
        if all_secrets_ok:
            print(f"   ✅ Todos os secrets configurados")
        else:
            print(f"   ❌ Alguns secrets em falta")
            
        return all_secrets_ok
        
    except Exception as e:
        print(f"   ❌ Erro ao importar config: {str(e)}")
        return False

def test_fastapi_import():
    """Testa se a aplicação FastAPI pode ser importada"""
    print("\n🚀 Testando Import da Aplicação FastAPI:")
    
    try:
        sys.path.append('./backend')
        from main_modular import app
        
        print(f"   ✅ FastAPI app importada com sucesso")
        print(f"   📚 Título: {app.title}")
        print(f"   🏷️ Versão: {app.version}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Erro ao importar FastAPI app: {str(e)}")
        return False

def main():
    print("🔍 GestOnGo - Verificação de Deploy no Replit")
    print("=" * 60)
    
    checks = [
        ("Versão Python", check_python_version),
        ("Environment Variables", check_environment_variables),
        ("Dependências", check_dependencies),
        ("Estrutura de Arquivos", check_file_structure),
        ("Configuração", test_import_config),
        ("Aplicação FastAPI", test_fastapi_import),
    ]
    
    results = []
    
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"   ❌ Erro na verificação {name}: {str(e)}")
            results.append((name, False))
    
    print("\n" + "=" * 60)
    print("📊 RESUMO DA VERIFICAÇÃO:")
    
    all_passed = True
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {status}: {name}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\n🎉 TODAS AS VERIFICAÇÕES PASSARAM!")
        print("🚀 O projeto está pronto para executar!")
        print("\n📋 Para iniciar o servidor:")
        print("   cd backend && python -m uvicorn main_modular:app --host 0.0.0.0 --port 8000")
    else:
        print("\n⚠️ ALGUMAS VERIFICAÇÕES FALHARAM!")
        print("🔧 Resolva os problemas indicados antes de executar")
        
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
