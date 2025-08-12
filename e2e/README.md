# 🧪 GestOnGo E2E Tests

Testes End-to-End usando Playwright e Docker.

## 🚀 **Como executar E2E localmente**

```bash
# Executar E2E completo (build + test)
docker compose -f compose.e2e.yaml up --build --abort-on-container-exit --exit-code-from e2e

# Executar apenas E2E (assumindo que backend/frontend já estão rodando)
cd e2e
npm install
npm test
```

## 🐳 **Estrutura Docker**

### E2E Container
- **Base**: `mcr.microsoft.com/playwright:v1.46.0-jammy`
- **Browsers**: Chrome, Firefox, Safari (WebKit) pré-instalados
- **Runtime**: Node.js 18+

### Dependências
- **API**: Backend Express na porta 8000
- **Web**: Frontend CRA servido pelo Nginx na porta 80

## 🧪 **Testes Incluídos**

### Smoke Tests (`tests/smoke.spec.ts`)
- Homepage carrega corretamente
- API `/health` responde `{ ok: true }`

### Configuração (`playwright.config.ts`)
- **Base URL**: `http://web` (Docker) ou `http://localhost:8080` (local)
- **Retries**: 2x no CI, 0x localmente
- **Mode**: Headless sempre
- **Reporter**: Lista simples

## 🔄 **CI/CD Integration**

### Workflows
1. **docker-publish.yml**: Publica imagens no GHCR
2. **e2e.yml**: Executa E2E contra imagens publicadas

### GHCR Images
- `ghcr.io/ramos-bot/gestongo-app/frontend:latest`
- `ghcr.io/ramos-bot/gestongo-app/backend:latest`

## 🛠 **Scripts Úteis**

```bash
# E2E local (desenvolvimento)
npm run test

# E2E com Docker (produção)
docker compose -f compose.e2e.yaml up --build

# Limpar containers
docker compose -f compose.e2e.yaml down --volumes

# Ver logs detalhados
docker compose -f compose.e2e.yaml logs -f
```
