# 🔧 **CONFIGURAÇÃO AMBIENTE - GestOnGo**

## 🚀 **Setup Rápido**

### **1. Desenvolvimento Local**
```bash
# Backend
cd backend
cp .env.example .env
npm install
npm run dev         # http://localhost:8000

# Frontend (novo terminal)
cd ../frontend
cp .env.example .env
npm install
npm start           # http://localhost:3000
```

### **2. Docker (Produção)**
```bash
# Build e subir todos os serviços
docker compose up --build

# Frontend: http://localhost:8080
# API: http://localhost:8080/api/health (via proxy Nginx)
```

### **3. E2E Tests**
```bash
# E2E completo
docker compose -f compose.e2e.yaml up --build --abort-on-container-exit --exit-code-from e2e
```

## 🔑 **Variáveis de Ambiente**

### **Backend (.env)**
```bash
PORT=8000
NODE_ENV=development
# DATABASE_URL=postgresql://...
# JWT_SECRET=your-secret-key
```

### **Frontend (.env)**
```bash
REACT_APP_API_BASE=http://localhost:8000
```

## 🔄 **Proxy Configuration**

### **Desenvolvimento (CRA)**
- `package.json` tem `"proxy": "http://localhost:8000"`
- Permite chamar `/api/health` diretamente (sem CORS)

### **Produção (Nginx)**
- `nginx.conf` faz proxy `/api/*` → `backend:8000`
- Frontend servido diretamente pelo Nginx

## 🧪 **Testing**

### **Local**
```bash
# Backend
cd backend && npm test

# Frontend
cd frontend && npm test -- --watchAll=false

# Linting global
npm run lint
```

### **CI/CD**
- GitHub Actions executa testes automaticamente
- Publica imagens Docker no GHCR
- Deploy Firebase Hosting

## 🔗 **Secrets GitHub Actions**

Configurar em **Settings → Secrets and variables → Actions**:

- `FIREBASE_SERVICE_ACCOUNT` → JSON da conta de serviço
- `FIREBASE_PROJECT_ID` → ID do projeto Firebase
- `GITHUB_TOKEN` → Automático (para GHCR)

## 🛠 **Hooks de Pre-commit**

```bash
# Instalar Husky (raiz do projeto)
npm install
npx husky init
echo 'npx lint-staged' > .husky/pre-commit

# Agora commits executam lint automaticamente
```

## 📊 **Smoke Tests**

### **API Health Check**
```bash
curl http://localhost:8000/health
# → { "ok": true }
```

### **Frontend**
```bash
# Com proxy CRA
curl http://localhost:3000/api/health

# Com Docker
curl http://localhost:8080/api/health
```

### **E2E**
```bash
# Playwright tests
cd e2e
npm install
npm test
```

## 🎯 **URLs Importantes**

- **Local Dev Frontend**: http://localhost:3000
- **Local Dev Backend**: http://localhost:8000
- **Docker (Nginx)**: http://localhost:8080
- **E2E Tests**: Automático via Docker Compose

---

## ✅ **Checklist Setup**

- [ ] Backend: `.env` criado e dependências instaladas
- [ ] Frontend: `.env` criado e dependências instaladas  
- [ ] Docker: `docker compose up --build` funciona
- [ ] Tests: Backend e Frontend passam
- [ ] E2E: Playwright executa corretamente
- [ ] GitHub: Secrets configurados
- [ ] Hooks: Pre-commit instalado e funcionando
