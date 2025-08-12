# 🎯 Fluxo da App GestOnGo

## 🔄 Arquitetura Geral

```mermaid
flowchart TD
    %% Styling
    classDef frontend fill:#61dafb,stroke:#000,color:#000
    classDef backend fill:#68a063,stroke:#000,color:#fff
    classDef auth fill:#ff6b35,stroke:#000,color:#fff
    classDef database fill:#336791,stroke:#000,color:#fff
    classDef storage fill:#ff9500,stroke:#000,color:#fff

    %% Frontend Layer
    subgraph "🌐 Frontend (React + CRA)"
        Login[🔐 Login Firebase]
        Dashboard[📊 Dashboard]
        Clientes[👥 Gestão Clientes]
        Tarefas[📅 Gestão Tarefas]
        Servicos[🔧 Serviços Prestados]
        Upload[📷 Upload Fotos]
    end

    %% Backend Layer
    subgraph "🚀 Backend (Express.js)"
        AuthMiddleware[🛡️ Auth Middleware]
        APIClientes[👥 API Clientes]
        APITarefas[📅 API Tarefas] 
        APIServicos[🔧 API Serviços]
        APIDashboard[📊 API Dashboard]
        FileUpload[📁 File Upload]
    end

    %% External Services
    subgraph "🔒 Autenticação"
        FirebaseAuth[🔥 Firebase Auth]
    end

    subgraph "💾 Persistência"
        PostgreSQL[(🐘 PostgreSQL)]
        Redis[(⚡ Redis Cache)]
    end

    subgraph "☁️ Storage"
        FirebaseStorage[🔥 Firebase Storage]
    end

    %% User Flow
    Login --> Dashboard
    Dashboard --> Clientes
    Dashboard --> Tarefas
    Dashboard --> Servicos

    %% API Connections
    Clientes --> APIClientes
    Tarefas --> APITarefas
    Servicos --> APIServicos
    Dashboard --> APIDashboard
    Upload --> FileUpload

    %% Auth Flow
    Login --> FirebaseAuth
    APIClientes --> AuthMiddleware
    APITarefas --> AuthMiddleware
    APIServicos --> AuthMiddleware
    APIDashboard --> AuthMiddleware
    AuthMiddleware --> FirebaseAuth

    %% Data Persistence
    APIClientes --> PostgreSQL
    APITarefas --> PostgreSQL
    APIServicos --> PostgreSQL
    APIDashboard --> Redis
    APIDashboard --> PostgreSQL

    %% File Storage
    FileUpload --> FirebaseStorage

    %% Apply styles
    class Login,Dashboard,Clientes,Tarefas,Servicos,Upload frontend
    class AuthMiddleware,APIClientes,APITarefas,APIServicos,APIDashboard,FileUpload backend
    class FirebaseAuth auth
    class PostgreSQL,Redis database
    class FirebaseStorage storage
```

## 🔄 Fluxo de Autenticação

```mermaid
sequenceDiagram
    participant U as 👤 Utilizador
    participant F as 🌐 Frontend
    participant B as 🚀 Backend
    participant FA as 🔥 Firebase Auth

    U->>F: Insere email/password
    F->>FA: Autentica utilizador
    FA-->>F: Retorna JWT token
    F->>F: Guarda token no localStorage
    F->>B: Requests com Authorization header
    B->>FA: Valida token
    FA-->>B: Token válido
    B-->>F: Dados autorizados
    F-->>U: Interface autenticada
```

## 📊 Fluxo de Dados Dashboard

```mermaid
flowchart LR
    subgraph "📊 Dashboard Stats"
        A[📅 Tarefas do dia] --> D[📈 Dashboard]
        B[👥 Total clientes] --> D
        C[💰 Receitas mês] --> D
        E[🔧 Serviços ativos] --> D
    end

    subgraph "⚡ Cache Strategy"
        D --> R[⚡ Redis Cache]
        R --> P[(🐘 PostgreSQL)]
        R --> |TTL 5min| D
    end

    subgraph "🎨 UI Components"
        D --> W1[📊 Widget Tarefas]
        D --> W2[👥 Widget Clientes]
        D --> W3[💰 Widget Receitas]
        D --> W4[📈 Gráficos]
    end
```

## 🔧 Fluxo de Serviços

```mermaid
flowchart TD
    A[🔧 Novo Serviço] --> B{📷 Tem fotos?}
    B -->|Sim| C[📤 Upload Firebase]
    B -->|Não| D[💾 Salvar BD]
    C --> E[🖼️ URLs das fotos]
    E --> D
    D --> F[📄 Gerar PDF]
    F --> G[📧 Enviar cliente]
    G --> H[✅ Serviço concluído]
```

## 🚀 Deployment Flow

```mermaid
flowchart LR
    A[💻 Código] --> B[🔄 CI/CD]
    B --> C[🧪 Testes]
    C --> D[🐳 Docker Build]
    D --> E[📦 GHCR Push]
    E --> F[🚀 Deploy Server]
    F --> G[🏥 Health Check]
    G --> H[✅ Produção]
```

---

## 📋 Notas Técnicas

### **Stack Principal:**
- **Frontend:** React 18 + CRA + Firebase SDK
- **Backend:** Node.js + Express.js + Firebase Admin
- **Database:** PostgreSQL (produção) + Redis (cache)
- **Storage:** Firebase Storage (fotos/documentos)
- **Deploy:** Docker + GitHub Actions + GHCR

### **Padrões Arquiteturais:**
- **API REST** com verbos HTTP semânticos
- **JWT Authentication** via Firebase
- **Cache Strategy** com Redis para dashboard
- **File Upload** com validação e compressão
- **Error Handling** centralizado e logging estruturado

### **Segurança:**
- ✅ **HTTPS** obrigatório em produção
- ✅ **Rate Limiting** nos endpoints sensíveis  
- ✅ **Input Validation** em todas as APIs
- ✅ **CORS** configurado adequadamente
- ✅ **JWT Verification** em rotas protegidas
