"""
🔥 Setup automático do Firebase para GestOnGo
Script para configurar Firebase Authentication, Firestore e Hosting
"""

import os
import json
import subprocess
import sys

def print_step(step, message):
    print(f"\n🔥 {step}. {message}")
    print("=" * 50)

def run_command(command, description):
    print(f"Executando: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Sucesso!")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Erro: {e}")
        return None

def create_firebase_config():
    """Criar configuração base do Firebase"""
    config = {
        "hosting": {
            "public": "dist",
            "ignore": [
                "firebase.json",
                "**/.*",
                "**/node_modules/**"
            ],
            "rewrites": [
                {
                    "source": "**",
                    "destination": "/index.html"
                }
            ]
        },
        "firestore": {
            "rules": "firestore.rules",
            "indexes": "firestore.indexes.json"
        }
    }
    
    with open('frontend/firebase.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("✅ firebase.json criado")

def create_firestore_rules():
    """Criar regras do Firestore"""
    rules = '''rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Permitir leitura/escrita apenas para utilizadores autenticados
    match /{document=**} {
      allow read, write: if request.auth != null;
    }
    
    // Regras específicas para clientes
    match /clientes/{clienteId} {
      allow read, write: if request.auth != null;
    }
    
    // Regras específicas para serviços
    match /servicos/{servicoId} {
      allow read, write: if request.auth != null;
    }
  }
}'''
    
    with open('frontend/firestore.rules', 'w') as f:
        f.write(rules)
    
    print("✅ firestore.rules criado")

def create_firestore_indexes():
    """Criar índices do Firestore"""
    indexes = {
        "indexes": [],
        "fieldOverrides": []
    }
    
    with open('frontend/firestore.indexes.json', 'w') as f:
        json.dump(indexes, f, indent=2)
    
    print("✅ firestore.indexes.json criado")

def main():
    print("🔥 FIREBASE SETUP - GestOnGo")
    print("=" * 50)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists('frontend'):
        print("❌ Erro: Execute este script na raiz do projeto (onde está a pasta frontend)")
        sys.exit(1)
    
    print_step(1, "Criando configurações do Firebase")
    create_firebase_config()
    create_firestore_rules()
    create_firestore_indexes()
    
    print_step(2, "Verificando Firebase CLI")
    firebase_version = run_command("firebase --version", "Verificar Firebase CLI")
    if not firebase_version:
        print("❌ Firebase CLI não encontrado. Instale com:")
        print("npm install -g firebase-tools")
        sys.exit(1)
    
    print_step(3, "Instruções para configuração manual")
    print("""
🔥 PRÓXIMOS PASSOS MANUAIS:

1. Acesse: https://console.firebase.google.com
2. Crie um novo projeto: 'gestongo-app'
3. Ative Authentication (Email/Password)
4. Ative Firestore Database
5. Configure Hosting

6. Execute os comandos:
   cd frontend
   firebase login
   firebase init
   
7. Selecione:
   - ✅ Firestore
   - ✅ Hosting
   - ✅ Use existing project: gestongo-app
   
8. Para deploy:
   npm run build
   firebase deploy

📱 URLs após deploy:
- Hosting: https://gestongo-app.web.app
- Console: https://console.firebase.google.com/project/gestongo-app
""")

if __name__ == "__main__":
    main()
