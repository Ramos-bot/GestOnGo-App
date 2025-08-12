# 🔧 CONFIGURAÇÃO VS CODE + GITHUB - GestOnGo

## ✅ Status Atual
- ✅ Repositório Git configurado
- ✅ Arquivos `.vscode` criados
- ✅ `.gitignore` otimizado
- ✅ Extensions recomendadas definidas

## 🚀 Configuração Completa do VS Code

### 1. **Extensões Essenciais** 📦

#### Instalação Automática (Recomendado):
```bash
# O VS Code vai sugerir automaticamente as extensões
# Abrir Command Palette (Ctrl+Shift+P) e executar:
Extensions: Show Recommended Extensions
```

#### Extensões Principais:
- **Python**: `ms-python.python`
- **GitHub Copilot**: `github.copilot`
- **GitHub PR**: `github.vscode-pull-request-github`
- **GitLens**: `eamodio.gitlens`
- **Prettier**: `esbenp.prettier-vscode`
- **Tailwind CSS**: `bradlc.vscode-tailwindcss`

### 2. **Configurações Git no VS Code** 🔀

#### Configurar Credenciais Git:
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@gmail.com"
```

#### Configurar Token GitHub:
1. **GitHub** → **Settings** → **Developer Settings** → **Personal Access Tokens**
2. **Generate New Token** (classic)
3. Permissões: `repo`, `workflow`, `write:packages`
4. **Copiar o token**

#### Autenticar no VS Code:
1. **Command Palette** (`Ctrl+Shift+P`)
2. **GitHub: Sign In**
3. Colar o token

### 3. **Funcionalidades GitHub no VS Code** 🐙

#### Source Control (Git):
- **Lado esquerdo**: Ícone do Git (Ctrl+Shift+G)
- **Stage Changes**: Clicar no `+`
- **Commit**: Escrever mensagem e `Ctrl+Enter`
- **Push**: Clicar no ícone de sync/push

#### GitHub Pull Requests:
- **Command Palette**: `GitHub Pull Requests: Create Pull Request`
- **Review**: Comentários inline no código
- **Merge**: Direto do VS Code

#### GitHub Copilot:
- **Autocompletions**: Automático enquanto digita
- **Chat**: `Ctrl+Shift+I` para chat
- **Explain**: Selecionar código + `Ctrl+Shift+P` → `Copilot: Explain`

### 4. **Atalhos Úteis** ⌨️

```bash
# Git & GitHub
Ctrl+Shift+G     # Abrir Source Control
Ctrl+Shift+P     # Command Palette
Ctrl+`           # Terminal integrado

# Copilot
Tab              # Aceitar sugestão
Ctrl+Shift+I     # Chat do Copilot
Ctrl+/           # Toggle comment (para prompts)

# Navegação
Ctrl+P           # Quick Open (arquivos)
Ctrl+Shift+E     # Explorer
Ctrl+Shift+F     # Search
Ctrl+Shift+D     # Debug
```

### 5. **Workflows Recomendados** 🔄

#### Desenvolvimento Diário:
1. **Sincronizar**: `Git: Pull` no Command Palette
2. **Criar Branch**: `Git: Create Branch`
3. **Desenvolver**: Usar Copilot para autocompletions
4. **Commit**: Staged changes + mensagem descritiva
5. **Push**: `Git: Push`
6. **PR**: `GitHub Pull Requests: Create`

#### Para Features Grandes:
1. **Issue**: Criar no GitHub
2. **Branch**: `feature/nome-da-feature`
3. **Draft PR**: Marcar como draft initially
4. **Commits pequenos**: Committar incrementalmente
5. **Ready for Review**: Remover draft status

### 6. **Configurações Específicas GestOnGo** 🎯

#### Backend (Python):
- **Interpreter**: Configurado para `./backend/venv/Scripts/python.exe`
- **Linting**: Flake8 ativo
- **Formatting**: Black automático
- **Debug**: Configuração para FastAPI

#### Frontend (React):
- **Node**: NPM scripts integrados
- **Prettier**: Format on save
- **TypeScript**: IntelliSense completo
- **Tailwind**: Autocomplete de classes

#### Tasks Disponíveis:
- `🚀 Iniciar Backend (FastAPI)`
- `🌐 Iniciar Frontend (React)`
- `🔧 Verificar Status Replit`
- `🚀 Iniciar Sistema Completo`

### 7. **Troubleshooting** 🔧

#### Problema: Git não reconhece credenciais
```bash
git config --global credential.helper manager
```

#### Problema: Copilot não funciona
1. **Command Palette** → `GitHub Copilot: Check Status`
2. Verificar login GitHub
3. Verificar subscription ativa

#### Problema: Extensions não carregam
1. **Reload Window**: `Ctrl+Shift+P` → `Reload Window`
2. Verificar updates do VS Code
3. Reinstalar extensão específica

#### Problema: Python interpreter não encontrado
1. **Command Palette** → `Python: Select Interpreter`
2. Selecionar `./backend/venv/Scripts/python.exe`
3. Ou criar virtual environment: `python -m venv backend/venv`

### 8. **Comandos Úteis no Terminal Integrado** 💻

```bash
# Backend
cd backend
python main_modular.py
pip install -r requirements.txt

# Frontend  
cd frontend
npm install
npm run dev
npm run build

# Git
git status
git add .
git commit -m "feat: nova funcionalidade"
git push origin main

# Testes
python verify_replit_status.py
```

### 9. **Integração com GitHub Actions** 🤖

O projeto está preparado para CI/CD:
- **Testes automáticos** ao fazer push
- **Deploy automático** para Replit/Firebase
- **Code quality checks** com linting

### 10. **Recursos Avançados** 🚀

#### GitHub Codespaces:
- **Online Development**: Desenvolver direto no browser
- **Same VS Code**: Mesmo ambiente, na nuvem
- **Access**: GitHub.com → Code → Open with Codespaces

#### Live Share:
- **Collaborative coding**: Programar em equipa
- **Real-time**: Edição simultânea
- **Command**: `Live Share: Start Collaboration Session`

---

## 📋 Checklist Final

- [ ] Extensões instaladas
- [ ] Git configurado com credenciais
- [ ] GitHub autenticado no VS Code
- [ ] Copilot funcionando
- [ ] Tasks testadas
- [ ] Backend executando localmente
- [ ] Frontend executando localmente
- [ ] Primeiro commit realizado
- [ ] Push para GitHub ok

## 🎉 Resultado Esperado

Com essa configuração, você terá:
- **Ambiente completo** de desenvolvimento
- **Integração total** VS Code + GitHub
- **Produtividade máxima** com Copilot
- **Workflow otimizado** para desenvolvimento
- **Deploy automatizado** para produção

---
**📞 Suporte**: Em caso de problemas, verificar logs no Output panel do VS Code
