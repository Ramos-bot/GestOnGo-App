# GestOnGo — Monorepo

![CI](https://github.com/ramos-bot/gestongo-app/actions/workflows/ci.yml/badge.svg)

Estrutura:
- `frontend/` — React (CRA) para web
- `backend/` — API Express

## Requisitos
- Node 20+
- npm 10+

## Fluxo rápido
```bash
# Frontend
cd frontend
npm ci
npm start        # http://localhost:3000
npm test -- --watchAll=false
npm run build

# Backend
cd ../backend
npm ci
npm run dev      # http://localhost:8000
npm test
```

## CI/CD
O GitHub Actions (`.github/workflows/ci.yml`) executa:
- testes frontend e backend
- (opcional) docker build
- deploy Firebase Hosting (apenas main)

## Pastas
- `frontend/public/` — HTML base da app web
- `frontend/src/` — código React
- `backend/` — API + testes (Jest/Supertest)
- **API Documentation**: Auto-generated OpenAPI docs
- **Professional Development**: Full testing, CI/CD, and deployment setup

## 🛠️ Tech Stack

**Backend:**
- FastAPI 0.111.0
- SQLAlchemy 2.0.29
- JWT Authentication
- SQLite (dev) / PostgreSQL (prod)
- Pytest testing

**Frontend:**
- React 18
- Vite 5.0.8
- Axios for API calls
- Modern ES6+ JavaScript

**Development:**
- Ruff + Black (Python formatting)
- ESLint + Prettier (JavaScript)
- GitHub Actions CI/CD
- Docker support
- Replit deployment ready

## 📦 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 20+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd GestOnGo/App
   ```

2. **Backend Setup**
   ```bash
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Set up environment
   cp .env.example .env
   
   # Initialize database
   make init-db
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   cp .env.example .env.local
   ```

4. **Start Development Servers**
   ```bash
   # Terminal 1: Backend
   make dev-backend
   
   # Terminal 2: Frontend
   make dev-frontend
   ```

## 🏗️ Estrutura do Projecto Modular

```
App/
├── backend/                    # API FastAPI modular
│   ├── main.py                # Ponto de entrada (versão original)
│   ├── main_modular.py        # Ponto de entrada modular
│   ├── app/                   # Versão base do sistema
│   │   ├── core/              # Configurações centrais
│   │   │   ├── database.py    # Base de dados com suporte modular
│   │   │   └── security.py    # Autenticação JWT
│   │   ├── models_base/       # Modelos base (User, Cliente)
│   │   │   ├── user.py        # Utilizadores
│   │   │   └── cliente.py     # Clientes
│   │   ├── schemas_base/      # Schemas Pydantic base
│   │   │   ├── user.py        # Validação utilizadores
│   │   │   └── cliente.py     # Validação clientes
│   │   └── routers_base/      # Rotas base
│   │       ├── users.py       # Autenticação e utilizadores
│   │       └── clientes.py    # CRUD de clientes
│   └── modules/               # Módulos opcionais
│       ├── verde/             # Módulo Verde (Jardinagem)
│       │   ├── models/        # ServicoJardim
│       │   ├── schemas/       # Validação jardinagem
│       │   └── routers/       # API jardinagem
│       └── aqua/              # Módulo Aqua (Piscinas)
│           ├── models/        # ServicoPiscina
│           ├── schemas/       # Validação piscinas
│           └── routers/       # API piscinas
├── frontend/                  # Interface React modular
│   ├── src/
│   │   ├── App.jsx           # Aplicação original
│   │   ├── App_modular.jsx   # Aplicação modular
│   │   ├── components/       # Componentes base
│   │   │   ├── LoginForm.jsx
│   │   │   └── ClienteManager.jsx
│   │   └── modules/          # Módulos frontend
│   │       ├── verde/        # Interface jardinagem
│   │       │   └── ServicoJardimManager.jsx
│   │       └── aqua/         # Interface piscinas
│   │           └── ServicoPiscinaManager.jsx
│   ├── .env                  # Configuração modular
│   └── package.json          # Dependências melhoradas
├── tests/                    # Testes automatizados
├── .github/workflows/        # CI/CD pipeline
├── docker-compose.yml        # Containerização
└── README.md                 # Documentação completa
```

## 🔧 Configuração Modular

### **Activar/Desactivar Módulos**

#### Backend (main_modular.py):
```python
# Comentar estas linhas para desactivar módulos:
from modules.verde.routers.servicos_jardim import router as verde_router
from modules.aqua.routers.servicos_piscina import router as aqua_router
```

#### Frontend (App_modular.jsx):
```javascript
// Comentar estas linhas para desactivar módulos:
const modulosDisponiveis = {
  verde: true,  // Módulo Verde (Jardinagem)
  aqua: true,   // Módulo Aqua (Piscinas)
};
```

### **Executar Versão Modular**

1. **Backend modular:**
   ```bash
   uvicorn main_modular:app --reload --port 8000
   ```

2. **Frontend modular:**
   ```bash
   # Actualizar App.jsx para usar App_modular.jsx
   cp src/App_modular.jsx src/App.jsx
   npm run dev
   ```

## 🚀 Funcionalidades Modulares

### **Versão Base (sempre activa)**
- ✅ Autenticação JWT com utilizadores
- ✅ Gestão completa de clientes (CRUD)
- ✅ Sistema de segurança e permissões
- ✅ Base de dados SQLite/PostgreSQL

### **Módulo Verde - Jardinagem** 🌿
- ✅ Serviços de jardinagem e manutenção
- ✅ Validação específica (tipo='jardinagem')
- ✅ Interface dedicada com formulários
- ✅ Relatórios por cliente e data

### **Módulo Aqua - Piscinas** 🏊
- ✅ Serviços de piscinas e tratamento
- ✅ Validação específica (tipo='piscina')
- ✅ Interface dedicada com formulários
- ✅ Gestão de tratamentos químicos

## 🔐 Autenticação Modular

**Credenciais padrão:**
- Email: `admin@gestongo.com`
- Senha: `admin123`

**Todas as rotas de módulos requerem autenticação JWT**

## 📊 API Endpoints Modulares

### **Base (sempre disponível):**
- `POST /utilizadores/` - Criar utilizador
- `POST /utilizadores/login` - Login JWT
- `GET /utilizadores/me` - Utilizador actual
- `GET|POST|PUT|DELETE /clientes/` - CRUD clientes

### **Módulo Verde (condicional):**
- `GET|POST|PUT|DELETE /servicos-jardim/` - CRUD jardinagem

### **Módulo Aqua (condicional):**
- `GET|POST|PUT|DELETE /servicos-piscina/` - CRUD piscinas

### **Sistema:**
- `GET /` - Info sistema e módulos activos
- `GET /health` - Estado dos módulos

## 💡 Vantagens da Arquitectura Modular

1. **Escalabilidade:** Adicionar novos módulos sem alterar o core
2. **Flexibilidade:** Activar/desactivar funcionalidades conforme necessário  
3. **Manutenção:** Código organizado por domínio de negócio
4. **Deployment:** Opção de distribuir apenas módulos específicos
5. **Testing:** Testes isolados por módulo
6. **Comercial:** Módulos podem ser funcionalidades pagas

## 🔄 Migração para Modular

Se tem a versão anterior, pode migrar gradualmente:

1. **Manter backend original:** Use `main.py` 
2. **Testar backend modular:** Use `main_modular.py`
3. **Frontend híbrido:** Pode usar ambas as versões
4. **Base de dados:** Compatível entre versões

## 📁 Estrutura do Projeto

```
App/
├── backend/                    # API FastAPI
│   ├── main.py                # Ponto de entrada da API
│   └── app/
│       ├── core/              # Configurações centrais
│       │   ├── database.py    # Configuração da base de dados
│       │   └── security.py    # Autenticação e segurança
│       ├── models/            # Modelos ORM (SQLAlchemy)
│       │   ├── user.py        # Modelo de utilizadores
│       │   ├── cliente.py     # Modelo de clientes
│       │   └── servico.py     # Modelo de serviços
│       ├── schemas/           # Esquemas Pydantic
│       │   ├── user.py        # Esquemas de utilizadores
│       │   ├── cliente.py     # Esquemas de clientes
│       │   └── servico.py     # Esquemas de serviços
│       └── routers/           # Endpoints da API
│           ├── users.py       # Rotas de utilizadores
│           ├── clientes.py    # Rotas de clientes
│           └── servicos.py    # Rotas de serviços
├── frontend/                  # Interface React
│   ├── index.html            # Página principal
│   ├── package.json          # Dependências Node.js
│   ├── vite.config.js        # Configuração Vite
│   ├── src/
│   │   ├── main.jsx          # Ponto de entrada React
│   │   ├── App.jsx           # Componente principal
│   │   ├── firebase.js       # Configuração Firebase (opcional)
│   │   └── components/       # Componentes React
│   │       ├── LoginForm.jsx     # Formulário de login
│   │       ├── ClienteManager.jsx # Gestão de clientes
│   │       └── ServicoManager.jsx # Gestão de serviços
└── requirements.txt          # Dependências Python
```

## 🚀 Como Executar

### Backend (FastAPI)

1. **Instalar dependências Python:**
   ```bash
   cd App
   pip install -r requirements.txt
   ```

2. **Executar a API:**
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

3. **Aceder à documentação da API:**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Frontend (React)

1. **Instalar dependências Node.js:**
   ```bash
   cd App/frontend
   npm install
   ```

2. **Executar o servidor de desenvolvimento:**
   ```bash
   npm run dev
   ```

3. **Aceder à aplicação:**
   - URL: http://localhost:5173

## 🔧 Funcionalidades Implementadas

### 🔐 Autenticação & Segurança
- ✅ Sistema de login com JWT
- ✅ Protecção de rotas
- ✅ Hashing seguro de senhas (bcrypt)
- ✅ Tokens com expiração automática
- ✅ Utilizador admin criado automaticamente

### 👥 Gestão de Clientes
- ✅ Criar novos clientes
- ✅ Listar clientes com paginação
- ✅ Editar clientes existentes
- ✅ Eliminar clientes (com validações)
- ✅ Busca por nome
- ✅ Validação de telefones portugueses
- ✅ Estatísticas de clientes

### 🛠️ Gestão de Serviços
- ✅ Criar novos serviços
- ✅ Listar serviços com filtros
- ✅ Editar serviços existentes
- ✅ Eliminar serviços
- ✅ Tipos: jardinagem ou piscina
- ✅ Status: agendado, em_progresso, concluído, cancelado
- ✅ Agendamento por data
- ✅ Controlo de duração em horas
- ✅ Associação a clientes
- ✅ Validações de conflitos de horário
- ✅ Dashboard com estatísticas

### 🎨 Interface de Utilizador
- ✅ Design responsivo e moderno
- ✅ Dashboard com visão geral
- ✅ Navegação por abas
- ✅ Formulários intuitivos
- ✅ Validação em tempo real
- ✅ Feedback visual de erros
- ✅ Lista de próximos serviços
- ✅ Cards de estatísticas

## 💾 Base de Dados

A aplicação utiliza SQLite para desenvolvimento (ficheiro `gestongo.db` criado automaticamente).

### Tabelas:
- **utilizadores**: Gestão de contas de utilizador
- **clientes**: Informações dos clientes
- **servicos**: Agendamento e registo de serviços

### Utilizador Padrão:
- **Email**: admin@gestongo.pt
- **Senha**: gestongo2025

## 🌐 API Endpoints

### Utilizadores
- `POST /utilizadores/` - Criar utilizador
- `POST /utilizadores/login` - Login

### Clientes
- `GET /clientes/` - Listar clientes (com filtros)
- `POST /clientes/` - Criar cliente
- `GET /clientes/{id}` - Obter cliente específico
- `PUT /clientes/{id}` - Actualizar cliente
- `DELETE /clientes/{id}` - Eliminar cliente
- `GET /clientes/estatisticas/resumo` - Estatísticas

### Serviços
- `GET /servicos/` - Listar serviços (com filtros)
- `POST /servicos/` - Criar serviço
- `GET /servicos/resumo` - Lista resumida
- `GET /servicos/{id}` - Obter serviço específico
- `PUT /servicos/{id}` - Actualizar serviço
- `DELETE /servicos/{id}` - Eliminar serviço
- `GET /servicos/estatisticas/dashboard` - Dashboard

## 🔒 Validações Implementadas

### Clientes
- Nome obrigatório (mínimo 2 caracteres)
- Validação de telefones portugueses (+351xxxxxxxxx)
- Verificação de duplicados por nome

### Serviços
- Tipo obrigatório (jardinagem ou piscina)
- Data não pode ser no passado
- Duração entre 1 e 12 horas
- Cliente deve existir
- Não permite conflitos de horário

## 🔧 Características Técnicas

### Backend
- **FastAPI** com documentação automática
- **SQLAlchemy** ORM com modelos relacionais
- **Pydantic** para validação de dados
- **JWT** para autenticação
- **CORS** configurado para frontend
- **Enums** para valores controlados
- **Filtros e paginação** em listagens

### Frontend
- **React 18** com Hooks
- **Componentes modulares** reutilizáveis
- **Axios** para comunicação com API
- **Estado local** com useState/useEffect
- **Design responsivo** com CSS inline
- **Validação de formulários** client-side
- **Gestão de erros** centralizada

## 🌍 Configuração Firebase (Opcional)

O projeto inclui configuração para Firebase (comentada):
1. Autenticação em tempo real
2. Firestore para dados
3. Storage para ficheiros

Para activar:
```bash
npm install firebase
```

## 📱 Próximas Funcionalidades

- [ ] Sistema de relatórios
- [ ] Calendário visual
- [ ] Notificações
- [ ] App mobile (React Native)
- [ ] Integração com mapas
- [ ] Sistema de faturação
- [ ] Gestão de equipamentos
- [ ] Photos dos serviços
- [ ] Backup automático
- [ ] Multi-tenancy

## 🚀 Deploy em Produção

### Backend
```bash
# PostgreSQL em produção
pip install psycopg2
# Configurar DATABASE_URL

# Docker
docker build -t gestongo-api .
docker run -p 8000:8000 gestongo-api
```

### Frontend
```bash
npm run build
# Deploy para Netlify, Vercel, etc.
```

---

**GestOnGo v0.1.0** - Desenvolvido para gestão eficiente de serviços de campo em Portugal 🇵🇹

## 📞 Suporte

Para dúvidas ou sugestões sobre a aplicação GestOnGo, consulte a documentação da API em `/docs` quando o servidor estiver a correr.
