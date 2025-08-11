# 🚀 GUIA COMPLETO DE CONFIGURAÇÃO
## GitHub ✅ | Replit | Firebase

---

## 🐙 **1. GITHUB - ✅ CONCLUÍDO**

✅ **Repositório**: https://github.com/Ramos-bot/GestOnGo-App
✅ **Push realizado** com sucesso
✅ **Projeto disponível** no GitHub

### Próximos Passos no GitHub:
1. **Configurar GitHub Pages** (opcional):
   - Settings → Pages → Source: GitHub Actions
   - Deploy automático do frontend

2. **Configurar Secrets** para CI/CD:
   - Settings → Secrets and variables → Actions
   - Adicionar: `DATABASE_URL`, `SECRET_KEY`, etc.

---

## 💻 **2. REPLIT - CONFIGURAÇÃO**

### Passo 1: Importar do GitHub
1. Acesse [replit.com](https://replit.com) e faça login
2. Clique em **"Create Repl"**
3. Selecione **"Import from GitHub"**
4. Cole: `https://github.com/Ramos-bot/GestOnGo-App`
5. Nome: `gestongo-modular`
6. Clique **"Import from GitHub"**

### Passo 2: Configurar Secrets no Replit
No Replit, na aba **"Secrets"** (ícone cadeado), adicione:

```env
SECRET_KEY=sua_chave_secreta_muito_forte_para_jwt_tokens_123456789
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./gestongo.db
ACTIVE_MODULES=verde,aqua
```

### Passo 3: Configurar .replit
```toml
# .replit
run = "cd backend && python main_modular.py"
entrypoint = "backend/main_modular.py"

[nix]
channel = "stable-22_11"

[deployment]
run = ["sh", "-c", "cd backend && python main_modular.py"]
```

### Passo 4: Configurar replit.nix
```nix
# replit.nix
{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.nodejs-18_x
    pkgs.nodePackages.npm
  ];
}
```

### Passo 5: Deploy no Replit
1. **Run** para testar localmente
2. **Deploy** → Autoscale deployment
3. URL será: `https://gestongo-modular.{seu-username}.repl.co`

---

## 🔥 **3. FIREBASE - CONFIGURAÇÃO**

### Passo 1: Criar Projeto Firebase
1. Acesse [console.firebase.google.com](https://console.firebase.google.com)
2. **"Create a project"**
3. Nome: `gestongo-app`
4. ✅ Enable Google Analytics (opcional)
5. Aguarde criação

### Passo 2: Configurar Authentication
1. **Authentication** → **Get started**
2. **Sign-in method** → **Email/Password** → Enable
3. **Users** → **Add user**:
   - Email: `admin@gestongo.com`
   - Password: `admin123`

### Passo 3: Configurar Firestore
1. **Firestore Database** → **Create database**
2. **Production mode** → **Next**
3. **Location**: `europe-west1` (Europa)
4. **Rules** (temporário para desenvolvimento):
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if request.auth != null;
    }
  }
}
```

### Passo 4: Configurar Hosting
1. **Hosting** → **Get started**
2. **Install Firebase CLI**:
```bash
npm install -g firebase-tools
```

3. **Login and Initialize**:
```bash
firebase login
cd frontend
firebase init hosting
```

4. **Configurações**:
   - Use existing project: `gestongo-app`
   - Public directory: `dist`
   - Single-page app: `Yes`
   - GitHub integration: `Yes` (opcional)

### Passo 5: Configurar Web App
1. **Project Overview** → **Add app** → **Web** (<//>)
2. **App nickname**: `GestOnGo Web`
3. ✅ **Firebase Hosting**
4. **Register app**
5. **Copiar config** para o arquivo:

```javascript
// frontend/src/firebase.js
import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
  apiKey: "sua-api-key",
  authDomain: "gestongo-app.firebaseapp.com",
  projectId: "gestongo-app",
  storageBucket: "gestongo-app.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abcdef123456"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
export default app;
```

### Passo 6: Deploy para Firebase
```bash
cd frontend
npm run build
firebase deploy
```

**URL de produção**: `https://gestongo-app.web.app`

---

## 🔧 **CONFIGURAÇÃO COMPLETA DE DESENVOLVIMENTO**

### Environment Variables

#### Backend (.env)
```env
# Segurança
SECRET_KEY=chave_super_secreta_jwt_2024_gestongo_modular_system
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Módulos ativos
ACTIVE_MODULES=verde,aqua

# Base de dados
DATABASE_URL=sqlite:///./gestongo.db

# CORS
FRONTEND_URL=http://localhost:5173

# Debug
DEBUG=true
LOG_LEVEL=INFO
```

#### Frontend (.env)
```env
VITE_API_BASE_URL=http://localhost:8000
VITE_APP_TITLE=GestOnGo - Sistema Modular
VITE_VERSION=1.0.0

# Firebase (desenvolvimento)
VITE_FIREBASE_API_KEY=sua-firebase-api-key
VITE_FIREBASE_AUTH_DOMAIN=gestongo-app.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=gestongo-app
```

---

## 🚀 **COMANDOS DE DEPLOY AUTOMÁTICO**

### GitHub Actions (.github/workflows/deploy.yml)
```yaml
name: Deploy to Multiple Platforms

on:
  push:
    branches: [ main ]

jobs:
  deploy-firebase:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install and Build
        run: |
          cd frontend
          npm install
          npm run build
      
      - name: Deploy to Firebase
        uses: FirebaseExtended/action-hosting-deploy@v0
        with:
          repoToken: '${{ secrets.GITHUB_TOKEN }}'
          firebaseServiceAccount: '${{ secrets.FIREBASE_SERVICE_ACCOUNT }}'
          projectId: gestongo-app
```

---

## 📊 **RESUMO DOS SERVIÇOS**

| Serviço | Função | URL | Status |
|---------|--------|-----|--------|
| **GitHub** | Código fonte | https://github.com/Ramos-bot/GestOnGo-App | ✅ |
| **Replit** | Backend API | `gestongo-modular.{user}.repl.co` | ⏳ |
| **Firebase** | Frontend + Auth | `gestongo-app.web.app` | ⏳ |

---

## 🔄 **PRÓXIMOS PASSOS**

1. ✅ **GitHub configurado**
2. ⏳ **Configurar Replit** (seguir Passo 2)
3. ⏳ **Configurar Firebase** (seguir Passo 3)
4. 🔄 **Testar integração** completa
5. 🚀 **Deploy final** em produção

---

**🎯 Objetivo**: Sistema GestOnGo funcionando em 3 plataformas integradas!
