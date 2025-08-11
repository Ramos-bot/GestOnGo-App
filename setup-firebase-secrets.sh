#!/bin/bash

# Script para configurar secrets no Firebase
# Execute: chmod +x setup-firebase-secrets.sh && ./setup-firebase-secrets.sh

echo "🔐 Configurando secrets do Firebase para GestOnGo..."

# 1. Login no Firebase (se necessário)
echo "1. Verificando login Firebase..."
firebase login

# 2. Selecionar projeto
echo "2. Selecionando projeto gestongo-app..."
firebase use gestongo-app

# 3. Configurar secrets para Cloud Functions
echo "3. Configurando secrets..."

# JWT Secret para autenticação
echo "Configurando JWT_SECRET_KEY..."
firebase functions:secrets:set JWT_SECRET_KEY

# Base de dados
echo "Configurando DATABASE_URL..."
firebase functions:secrets:set DATABASE_URL

# Email service
echo "Configurando EMAIL_API_KEY..."
firebase functions:secrets:set EMAIL_API_KEY

# Stripe (se usar pagamentos)
echo "Configurando STRIPE_SECRET_KEY..."
firebase functions:secrets:set STRIPE_SECRET_KEY

# 4. Verificar secrets configurados
echo "4. Verificando secrets configurados..."
firebase functions:secrets:list

echo "✅ Secrets configurados com sucesso!"
echo ""
echo "Para usar nos Cloud Functions:"
echo "const { defineSecret } = require('firebase-functions/params');"
echo "const jwtSecret = defineSecret('JWT_SECRET_KEY');"
echo ""
echo "Para deploy com secrets:"
echo "firebase deploy --only functions"
