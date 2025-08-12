# 📚 **DOCUMENTAÇÃO TÉCNICA - GestOnGo**

## 🏗️ **Arquitetura**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │     Backend     │    │    Database     │
│   (React/CRA)   │◄──►│  (Express.js)   │◄──►│  (PostgreSQL)   │
│   Port: 3000    │    │   Port: 3001    │    │   Port: 5432    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### **Stack Tecnológico:**
- **Frontend:** React 18 + Create React App + Jest + React Testing Library
- **Backend:** Node.js 20 + Express.js + Jest + Supertest
- **Database:** PostgreSQL 15 (produção) / SQLite (desenvolvimento)
- **Containerização:** Docker + Docker Compose
- **CI/CD:** GitHub Actions + GitHub Container Registry
- **E2E Testing:** Playwright
- **Proxy:** Nginx (produção)

---

## 🚀 **Quick Start**

### **Desenvolvimento Local:**
```bash
# 1. Clonar repositório
git clone <repo-url>
cd gestongo

# 2. Instalar dependências
cd backend && npm install
cd ../frontend && npm install --legacy-peer-deps

# 3. Configurar ambiente
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# 4. Iniciar desenvolvimento
npm run dev  # Inicia backend + frontend
```

### **Com Docker:**
```bash
# Desenvolvimento
docker-compose up -d

# E2E Testing
docker-compose -f compose.e2e.yaml up --abort-on-container-exit

# Produção
docker-compose -f compose.production.yaml up -d
```

---

## 📁 **Estrutura do Projeto**

```
gestongo/
├── 📂 backend/           # API Express.js
│   ├── 📂 __tests__/     # Testes Jest + Supertest
│   ├── 📂 src/           # Código fonte
│   ├── 📄 server.js      # Entry point
│   └── 📄 package.json
├── 📂 frontend/          # App React
│   ├── 📂 src/           # Componentes React
│   ├── 📂 public/        # Assets estáticos
│   └── 📄 package.json
├── 📂 e2e/              # Testes Playwright
├── 📂 .github/          # CI/CD workflows
│   ├── 📂 workflows/    # GitHub Actions
│   └── 📂 ISSUE_TEMPLATE/  # Templates de issues
├── 📄 docker-compose.yml    # Desenvolvimento
├── 📄 compose.e2e.yaml     # E2E Testing
└── 📄 compose.production.yaml  # Produção
```

---

## 🔧 **Scripts Disponíveis**

### **Root (Monorepo):**
```bash
npm run dev          # Backend + Frontend em paralelo
npm run test         # Testes backend + frontend
npm run test:e2e     # Testes E2E com Playwright
npm run build        # Build de produção
npm run docker:dev   # Docker desenvolvimento
npm run docker:prod  # Docker produção
```

### **Backend:**
```bash
npm start           # Produção (node server.js)
npm run dev         # Desenvolvimento (nodemon)
npm test            # Jest + Supertest
npm run test:watch  # Testes em watch mode
```

### **Frontend:**
```bash
npm start           # Servidor desenvolvimento (CRA)
npm run build       # Build otimizado
npm test            # Jest + React Testing Library
npm run test:coverage  # Coverage report
```

---

## 🌐 **Endpoints da API**

### **Health Check:**
```http
GET /api/health
# Response: { "status": "OK", "timestamp": "2024-01-01T00:00:00.000Z" }
```

### **Estrutura Padrão:**
```http
# CRUD Pattern
GET    /api/resource     # Listar todos
GET    /api/resource/:id # Obter por ID
POST   /api/resource     # Criar novo
PUT    /api/resource/:id # Atualizar completo
PATCH  /api/resource/:id # Atualizar parcial
DELETE /api/resource/:id # Remover
```

---

## 🧪 **Testing Strategy**

### **Níveis de Teste:**

1. **Unit Tests (Jest):**
   ```bash
   # Backend: Funções, middlewares, utils
   npm test backend/__tests__/
   
   # Frontend: Componentes, hooks, utils
   npm test frontend/src/__tests__/
   ```

2. **Integration Tests (Supertest):**
   ```bash
   # API endpoints, database interactions
   npm test backend/__tests__/integration/
   ```

3. **E2E Tests (Playwright):**
   ```bash
   # User flows completos
   npm run test:e2e
   ```

### **Coverage Targets:**
- **Unit Tests:** > 80%
- **Integration Tests:** > 70%
- **E2E Tests:** Critical paths

---

## 🐳 **Docker Strategy**

### **Multi-stage Builds:**
```dockerfile
# 1. Dependencies stage (cache otimizado)
# 2. Build stage (compilação)
# 3. Production stage (runtime mínimo)
```

### **Environments:**

1. **Development:** Hot reload, debugging
2. **Testing:** Isolated containers, test data
3. **Production:** Optimized, security hardened

---

## 🔄 **CI/CD Pipeline**

### **GitHub Actions Workflow:**

```yaml
Trigger: Push to main, Pull Requests
│
├── 📋 Lint & Format
├── 🧪 Unit Tests (Backend + Frontend)
├── 🔒 Security Scan
├── 🏗️ Build Docker Images
├── 📦 Push to GHCR
├── 🧪 E2E Tests
└── 🚀 Deploy (if main branch)
```

### **Deployment Strategy:**
- **Blue-Green Deployment** com health checks
- **Rollback automático** em caso de falha
- **Zero-downtime deployment**

---

## 🔐 **Segurança**

### **Implementações:**
- **CORS** configurado adequadamente
- **Rate limiting** nos endpoints
- **Input validation** com Joi/Zod
- **Security headers** (Helmet.js)
- **Container scanning** no CI

### **Environment Variables:**
```bash
# Backend
PORT=3001
NODE_ENV=production
DATABASE_URL=postgresql://...
JWT_SECRET=...

# Frontend
REACT_APP_API_URL=http://localhost:3001
```

---

## 📊 **Monitoring & Logs**

### **Health Checks:**
- **Frontend:** `/health` (Nginx)
- **Backend:** `/api/health` (Express)
- **Database:** Connection status

### **Logging Strategy:**
```javascript
// Structured logging com Winston
logger.info('User action', {
  userId: 123,
  action: 'login',
  timestamp: new Date().toISOString()
});
```

---

## 🔧 **Troubleshooting**

### **Problemas Comuns:**

1. **Dependency conflicts (Frontend):**
   ```bash
   npm install --legacy-peer-deps
   ```

2. **Port já em uso:**
   ```bash
   lsof -ti:3000 | xargs kill -9  # macOS/Linux
   netstat -ano | findstr :3000   # Windows
   ```

3. **Docker build lento:**
   ```bash
   # Usar BuildKit
   export DOCKER_BUILDKIT=1
   docker build --cache-from=...
   ```

---

## 📈 **Performance**

### **Frontend Optimizations:**
- **Code splitting** automático (CRA)
- **Image optimization** (WebP, lazy loading)
- **Bundle analysis:** `npm run build -- --analyze`

### **Backend Optimizations:**
- **Connection pooling** (database)
- **Caching strategy** (Redis em produção)
- **Compression** (gzip/brotli)

---

## 🤝 **Contribuindo**

### **Workflow:**
1. Fork o repositório
2. Criar feature branch: `git checkout -b feature/nova-feature`
3. Commit: `git commit -m 'feat: adicionar nova feature'`
4. Push: `git push origin feature/nova-feature`
5. Abrir Pull Request

### **Commit Convention:**
```
feat: nova funcionalidade
fix: correção de bug
docs: documentação
style: formatação
refactor: refatoração
test: testes
chore: manutenção
```

---

## 📞 **Suporte**

### **Recursos:**
- 📖 **Documentação:** `/docs`
- 🐛 **Issues:** GitHub Issues
- 💬 **Discussões:** GitHub Discussions
- 📧 **Contato:** dev@gestongo.com

### **Logs Úteis:**
```bash
# Docker logs
docker-compose logs -f

# Application logs
tail -f backend/logs/app.log

# Nginx logs (produção)
docker exec nginx tail -f /var/log/nginx/access.log
```
