# 🐳 **DOCKER & E2E - GestOnGo**

Guia completo para Docker, E2E e deployment em produção.

## 🧪 **E2E Tests (Playwright)**

### **Execução Local:**
```bash
# E2E completo com Docker
docker compose -f compose.e2e.yaml up --build --abort-on-container-exit --exit-code-from e2e

# E2E apenas (assumindo serviços rodando)
cd e2e && npm install && npm test
```

### **Estrutura E2E:**
```
e2e/
├── Dockerfile           # Playwright + browsers
├── package.json         # Dependências E2E
├── playwright.config.ts # Configuração testes
├── tests/
│   └── smoke.spec.ts   # Testes smoke
└── README.md           # Documentação E2E
```

## 🚀 **Docker Images (GHCR)**

### **Publicação Automática:**
- **Trigger**: Push para `main` ou workflow manual
- **Registry**: GitHub Container Registry (GHCR)
- **Tags**: `:latest` + `:sha-XXXXXXX`
- **Platforms**: `linux/amd64` + `linux/arm64`

### **Images Disponíveis:**
```bash
# Frontend (Nginx + build React)
ghcr.io/ramos-bot/gestongo-app/frontend:latest

# Backend (Node.js + Express)
ghcr.io/ramos-bot/gestongo-app/backend:latest
```

## 🏭 **Produção (Docker Compose)**

### **Deploy Rápido:**
```bash
# Usar imagens GHCR
docker compose -f compose.prod.yaml up -d

# Ver logs
docker compose -f compose.prod.yaml logs -f

# Parar
docker compose -f compose.prod.yaml down
```

### **Monitoramento:**
- **Frontend**: http://localhost (porta 80)
- **Backend**: http://localhost:8000/health
- **Logs**: `docker compose logs -f api web`

## 🔄 **Workflows GitHub Actions**

### **1. CI Pipeline (`ci.yml`)**
- Testes frontend (Jest + CRA)
- Testes backend (Jest + Supertest)
- Build verification

### **2. Docker Publish (`docker-publish.yml`)**
- Build multi-architecture
- Push para GHCR
- Tags automáticos

### **3. E2E Pipeline (`e2e.yml`)**
- Usa imagens publicadas no GHCR
- Testes end-to-end completos
- Validação de produção

## 📋 **Comandos Úteis**

### **Desenvolvimento:**
```bash
# Frontend local
cd frontend && npm start

# Backend local  
cd backend && npm run dev

# E2E local
cd e2e && npm test
```

### **Docker Local:**
```bash
# Build e test completo
docker compose -f compose.e2e.yaml up --build

# Produção com imagens GHCR
docker compose -f compose.prod.yaml up -d

# Limpar tudo
docker system prune -a
```

### **Monitoramento:**
```bash
# Status dos serviços
docker compose ps

# Logs em tempo real
docker compose logs -f

# Métricas de uso
docker stats
```

## 🎯 **Próximos Passos**

- [ ] Adicionar mais testes E2E (login, CRUD)
- [ ] Configurar monitoring (Prometheus + Grafana)
- [ ] Implementar blue-green deployment
- [ ] Adicionar backup automático
- [ ] SSL/TLS com Let's Encrypt

---

## 🏆 **Resultado Final:**

✅ **E2E Tests**: Playwright + Docker + CI/CD
✅ **Multi-arch Images**: AMD64 + ARM64 no GHCR  
✅ **Production Ready**: Compose + Health checks
✅ **Automated Pipeline**: Build → Test → Deploy
✅ **Monitoring**: Logs + Health endpoints
