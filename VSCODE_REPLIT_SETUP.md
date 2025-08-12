# 🔗 CONFIGURAÇÃO VS CODE + REPLIT

## 🎯 **Integração VS Code com Replit**

### **Cenário:**
- **Local**: VS Code para desenvolvimento
- **Deploy**: Replit para backend em produção
- **Sync**: Git como ponte entre ambos

## 🔧 **Configurações VS Code para Replit**

### **1. Configuração de Remote Development**

Adicionar ao `.vscode/settings.json`:
```json
{
    "// Configurações Replit": "",
    "remote.SSH.defaultForwardedPorts": [
        {
            "localPort": 8000,
            "remotePort": 8000,
            "name": "GestOnGo API"
        }
    ],
    
    "// URL da API Replit": "",
    "rest-client.environmentVariables": {
        "local": {
            "apiUrl": "http://localhost:8000"
        },
        "replit": {
            "apiUrl": "https://gestongo-app.tiago1982santos.repl.co"
        }
    }
}
```

### **2. Tasks para Replit**

Adicionar ao `.vscode/tasks.json`:
```json
{
    "label": "🔄 Sync to Replit (Git Push)",
    "type": "shell",
    "command": "git",
    "args": ["push", "origin", "main"],
    "group": "deploy",
    "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": true,
        "panel": "shared"
    }
},
{
    "label": "🧪 Test Replit API",
    "type": "shell", 
    "command": "python",
    "args": ["verify_replit_status.py"],
    "group": "test",
    "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": true,
        "panel": "shared"
    }
},
{
    "label": "🌐 Open Replit in Browser",
    "type": "shell",
    "command": "start",
    "args": ["https://replit.com/@tiago1982santos/GestOnGo-App"],
    "windows": {
        "command": "start",
        "args": ["https://replit.com/@tiago1982santos/GestOnGo-App"]
    },
    "group": "build"
}
```

### **3. Debug Configuration para Replit**

Adicionar ao `.vscode/launch.json`:
```json
{
    "name": "🔗 Debug via Replit API",
    "type": "python",
    "request": "attach",
    "connect": {
        "host": "gestongo-app.tiago1982santos.repl.co",
        "port": 443
    },
    "pathMappings": [
        {
            "localRoot": "${workspaceFolder}/backend",
            "remoteRoot": "/home/runner/GestOnGo-App/backend"
        }
    ]
}
```

## 🚀 **Workflow Recomendado**

### **Desenvolvimento Local → Deploy Replit:**

1. **Desenvolvimento no VS Code** (local)
2. **Commit & Push** para GitHub
3. **Replit puxa automaticamente** do GitHub
4. **Teste via API** no Replit

### **Comandos VS Code:**

#### **Via Command Palette (Ctrl+Shift+P):**
- `Tasks: Run Task` → `🔄 Sync to Replit (Git Push)`
- `Tasks: Run Task` → `🧪 Test Replit API`
- `Tasks: Run Task` → `🌐 Open Replit in Browser`

#### **Via Terminal Integrado:**
```bash
# Push para Replit
git push origin main

# Testar API Replit
python verify_replit_status.py

# Abrir Replit
start https://replit.com/@tiago1982santos/GestOnGo-App
```

## 📡 **Extensões Recomendadas para Replit**

### **REST Client Extension:**
Para testar API diretamente do VS Code:

```http
### Variáveis
@replit_url = https://gestongo-app.tiago1982santos.repl.co
@local_url = http://localhost:8000

### Test Replit API Root
GET {{replit_url}}/

### Test Replit Health
GET {{replit_url}}/health

### Test Replit Modules  
GET {{replit_url}}/modules

### Test Replit Docs
GET {{replit_url}}/docs
```

### **GitLens Extension:**
Para acompanhar deploys:
- **Timeline**: Ver quando código foi pushed
- **File History**: Rastrear mudanças
- **Remote Repositories**: Ver estado do GitHub

## 🔄 **Sincronização Automática**

### **GitHub Actions → Replit:**
O Replit pode ser configurado para auto-deploy via webhook:

1. **Replit Settings** → **Version Control**
2. **Auto-Deploy**: Ativar 
3. **Branch**: `main`
4. **Run Command**: `python backend/main_modular.py`

### **VS Code → GitHub → Replit:**
```
Local Development (VS Code)
         ↓ git push
    GitHub Repository
         ↓ webhook/auto-deploy
      Replit Production
```

## 🐛 **Debug Remoto (Avançado)**

### **Configurar Debug Remoto no Replit:**

1. **Instalar debugpy no Replit:**
```bash
pip install debugpy
```

2. **Modificar main_modular.py:**
```python
# No início do arquivo (só para debug)
import debugpy
debugpy.listen(("0.0.0.0", 5678))
print("Waiting for debugger attach...")
# debugpy.wait_for_client()  # Descomente para aguardar
```

3. **VS Code launch.json:**
```json
{
    "name": "🔗 Remote Debug Replit",
    "type": "python", 
    "request": "attach",
    "connect": {
        "host": "gestongo-app.tiago1982santos.repl.co",
        "port": 5678
    },
    "pathMappings": [
        {
            "localRoot": "${workspaceFolder}/backend",
            "remoteRoot": "/home/runner/GestOnGo-App/backend"
        }
    ]
}
```

## ⚡ **Quick Actions**

### **Snippets para VS Code:**

`.vscode/snippets/replit.json`:
```json
{
    "Push to Replit": {
        "prefix": "replit-push",
        "body": [
            "git add .",
            "git commit -m \"${1:feat: update for replit deploy}\"",
            "git push origin main"
        ],
        "description": "Push changes to Replit via GitHub"
    },
    
    "Test Replit API": {
        "prefix": "replit-test", 
        "body": [
            "python verify_replit_status.py"
        ],
        "description": "Test Replit API status"
    }
}
```

## 🔍 **Monitorização**

### **Status Dashboard no VS Code:**

Extensão **REST Client** com arquivo `replit-monitor.http`:
```http
### REPLIT STATUS DASHBOARD
### Execute cada request para monitorizar

### 1. API Health
GET https://gestongo-app.tiago1982santos.repl.co/health

### 2. Modules Status  
GET https://gestongo-app.tiago1982santos.repl.co/modules

### 3. API Documentation
GET https://gestongo-app.tiago1982santos.repl.co/docs

### 4. OpenAPI Schema
GET https://gestongo-app.tiago1982santos.repl.co/openapi.json
```

## 📋 **Checklist de Setup**

### ✅ **Configuração Inicial:**
- [ ] `.vscode/settings.json` com URLs Replit
- [ ] `.vscode/tasks.json` com comandos Replit
- [ ] `.vscode/launch.json` com debug remoto
- [ ] Extensão REST Client instalada
- [ ] Snippets de Replit criados

### ✅ **Workflow Testado:**
- [ ] `Ctrl+Shift+P` → `Tasks: Run Task` → `🔄 Sync to Replit`
- [ ] `Ctrl+Shift+P` → `Tasks: Run Task` → `🧪 Test Replit API`
- [ ] REST Client a funcionar com API Replit
- [ ] Git push → Replit auto-deploy a funcionar

### ✅ **Monitorização:**
- [ ] Dashboard de status da API
- [ ] Logs de deploy visíveis
- [ ] Alerts de downtime configurados

---

**🎯 Resultado:** VS Code totalmente integrado com Replit para desenvolvimento híbrido local+cloud!
