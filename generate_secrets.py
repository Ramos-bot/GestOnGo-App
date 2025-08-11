#!/usr/bin/env python3
"""
Gerador de chaves JWT seguras para GestOnGo
Execute este script para gerar chaves seguras para usar nos Secrets do Replit
"""

import secrets
import string
import base64
import os

def generate_jwt_secret(length=64):
    """Gera uma chave JWT segura"""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    return ''.join(secrets.choice(alphabet) for i in range(length))

def generate_base64_secret(length=32):
    """Gera uma chave em base64"""
    random_bytes = secrets.token_bytes(length)
    return base64.urlsafe_b64encode(random_bytes).decode('utf-8')

def generate_hex_secret(length=32):
    """Gera uma chave em hexadecimal"""
    return secrets.token_hex(length)

def main():
    print("🔐 Gerador de Secrets para GestOnGo no Replit")
    print("=" * 50)
    
    print("\n1. JWT Secret Key (64 caracteres):")
    jwt_secret = generate_jwt_secret(64)
    print(f"   {jwt_secret}")
    
    print("\n2. JWT Secret Key (Base64):")
    jwt_base64 = generate_base64_secret(32)
    print(f"   {jwt_base64}")
    
    print("\n3. JWT Secret Key (Hex):")
    jwt_hex = generate_hex_secret(32)
    print(f"   {jwt_hex}")
    
    print("\n4. Exemplo de Email App Password (Gmail):")
    email_password = generate_jwt_secret(16)
    print(f"   {email_password}")
    
    print("\n" + "=" * 50)
    print("📋 COPIE UMA DAS CHAVES ACIMA PARA O REPLIT:")
    print("   1. No Replit, abra a aba 'Secrets' (🔑)")
    print("   2. Clique 'Add new secret'")
    print("   3. Nome: JWT_SECRET_KEY")
    print("   4. Valor: Cole uma das chaves geradas acima")
    print("   5. Clique 'Add secret'")
    print("\n🎯 RECOMENDAÇÃO: Use a chave de 64 caracteres (opção 1)")

if __name__ == "__main__":
    main()
