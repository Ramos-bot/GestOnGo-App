# Makefile para GestOnGo - Scripts de desenvolvimento

.PHONY: help install-backend install-frontend install dev-backend dev-frontend dev test clean build

# Variáveis
PYTHON_BIN = python
PIP_BIN = pip
NODE_BIN = npm
BACKEND_DIR = backend
FRONTEND_DIR = frontend

help: ## Mostra esta ajuda
	@echo "GestOnGo - Scripts de Desenvolvimento"
	@echo "====================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: install-backend install-frontend ## Instala todas as dependências

install-backend: ## Instala dependências do backend (Python)
	cd $(BACKEND_DIR) && $(PYTHON_BIN) -m pip install -r ../requirements.txt

install-frontend: ## Instala dependências do frontend (Node.js)
	cd $(FRONTEND_DIR) && $(NODE_BIN) install

dev: ## Inicia ambos os servidores de desenvolvimento
	@echo "🚀 Iniciando GestOnGo em modo desenvolvimento..."
	@echo "Backend: http://localhost:8000"
	@echo "Frontend: http://localhost:5173"
	@echo "API Docs: http://localhost:8000/docs"
	@make -j2 dev-backend dev-frontend

dev-backend: ## Inicia apenas o servidor backend
	@echo "🐍 Iniciando backend FastAPI..."
	cd $(BACKEND_DIR) && uvicorn main:app --reload --port 8000

dev-frontend: ## Inicia apenas o servidor frontend
	@echo "⚛️ Iniciando frontend React..."
	cd $(FRONTEND_DIR) && $(NODE_BIN) run dev

test: ## Executa testes
	@echo "🧪 Executando testes..."
	cd $(BACKEND_DIR) && $(PYTHON_BIN) -m pytest -v

test-watch: ## Executa testes em modo watch
	cd $(BACKEND_DIR) && $(PYTHON_BIN) -m pytest -v --watch

lint: ## Executa linting
	@echo "🔍 Verificando código..."
	cd $(BACKEND_DIR) && ruff check .
	cd $(FRONTEND_DIR) && $(NODE_BIN) run lint

format: ## Formata código
	@echo "✨ Formatando código..."
	cd $(BACKEND_DIR) && ruff format .
	cd $(FRONTEND_DIR) && $(NODE_BIN) run format

build: ## Faz build de produção
	@echo "🏗️ Fazendo build de produção..."
	cd $(FRONTEND_DIR) && $(NODE_BIN) run build

clean: ## Limpa ficheiros temporários
	@echo "🧹 Limpando ficheiros temporários..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -delete
	rm -rf $(FRONTEND_DIR)/dist
	rm -rf $(FRONTEND_DIR)/node_modules/.cache

setup-dev: install ## Configuração inicial para desenvolvimento
	@echo "⚙️ Configurando ambiente de desenvolvimento..."
	@echo "✅ Dependências instaladas"
	@echo "✅ Pronto para desenvolvimento!"
	@echo ""
	@echo "Para iniciar:"
	@echo "  make dev    # Inicia backend e frontend"
	@echo "  make test   # Executa testes"

# Comandos específicos do Windows
ifeq ($(OS),Windows_NT)
dev-backend-win: ## Inicia backend no Windows
	cd $(BACKEND_DIR) && uvicorn main:app --reload --port 8000

dev-frontend-win: ## Inicia frontend no Windows
	cd $(FRONTEND_DIR) && npm run dev
endif
