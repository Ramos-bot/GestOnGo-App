# 📚 Documentação GestOnGo

Esta pasta contém a documentação técnica e funcional da aplicação para referência de developers e stakeholders.

## 📖 Conteúdo

### **🎯 Diagramas Técnicos**
- **[Fluxo da App](./fluxo-app.md)**  
  Diagrama completo em **Mermaid** mostrando arquitetura, autenticação, fluxo de dados e deployment.

### **📋 Roadmap de Features**
- **[Issues Pré-configuradas](../issues/)**  
  Lista das primeiras 5 funcionalidades com objetivos detalhados e critérios de aceitação:
  - `01-clientes-crud.md` - Gestão completa de clientes
  - `02-tarefas-agendamento.md` - Sistema de agendamento
  - `03-servicos-prestados.md` - Registo de serviços + fotos
  - `04-auth-firebase.md` - Autenticação Firebase
  - `05-dashboard-estatisticas.md` - Dashboard com métricas

---

## 🎨 Visualização de Diagramas

### **No GitHub:**
Ficheiros `.md` com código Mermaid são **renderizados automaticamente** no browser.

### **Localmente:**
```bash
# Instalar Mermaid CLI globalmente
npm install -g @mermaid-js/mermaid-cli

# Gerar imagem do diagrama
mmdc -i docs/fluxo-app.md -o docs/fluxo-app.svg

# Para PNG com alta qualidade
mmdc -i docs/fluxo-app.md -o docs/fluxo-app.png -w 1920 -H 1080
```

### **VS Code:**
```bash
# Instalar extensão para preview
code --install-extension bierner.markdown-mermaid
```

---

## 🗂️ Organização

```
📁 gestongo/
├── 📂 docs/                    ← Documentação central
│   ├── 📄 README.md           ← Este ficheiro
│   ├── 📄 fluxo-app.md        ← Diagramas arquiteturais
│   ├── 📄 api-reference.md    ← Documentação da API (futuro)
│   └── 📄 deployment.md       ← Guia de deploy (futuro)
├── 📂 issues/                  ← Issues pré-configuradas
│   ├── 📄 01-clientes-crud.md
│   ├── 📄 02-tarefas-agendamento.md
│   ├── 📄 03-servicos-prestados.md
│   ├── 📄 04-auth-firebase.md
│   └── 📄 05-dashboard-estatisticas.md
├── 📂 backend/                 ← API Express.js
├── 📂 frontend/                ← App React
└── 📂 e2e/                     ← Testes Playwright
```

---

## 📋 Convenções

### **📝 Issues:**
- **Formato:** `[Módulo] Descrição curta`
- **Labels:** `enhancement`, `bug`, `documentation`
- **Estimativas:** Complexidade (Baixa/Média/Alta) + Tempo (dias)
- **Dependências:** Links para issues relacionadas

### **🔄 Diagramas:**
- **Sempre atualizar** quando arquitetura muda
- **Usar cores consistentes** nos diagramas Mermaid
- **Incluir legendas** para componentes complexos

### **📖 Documentação:**
- **Markdown** para compatibilidade GitHub
- **Emojis** para navegação visual
- **Code blocks** com syntax highlighting
- **Links internos** entre documentos

---

## 🚀 Próximos Passos

### **📋 Para GitHub Issues:**
1. Copiar conteúdo dos ficheiros `issues/*.md`
2. Criar issues no GitHub com os mesmos títulos
3. Aplicar labels apropriadas (`enhancement`, `frontend`, `backend`)
4. Definir milestones para organizar sprints

### **🎨 Para Diagramas:**
1. Gerar versões PNG dos diagramas Mermaid
2. Adicionar às wikis ou README principal
3. Criar diagramas específicos por módulo
4. Documentar APIs com OpenAPI/Swagger

### **📚 Documentação Adicional:**
- [ ] API Reference com exemplos
- [ ] Guia de Setup para novos developers
- [ ] Troubleshooting guide
- [ ] Performance benchmarks
- [ ] Security guidelines

---

## 💡 Notas

✨ **GitHub Copilot** pode usar estas issues e diagramas como contexto para gerar código mais preciso.

🔄 **Issues são templates** - ajuste conforme necessário durante o desenvolvimento.

📊 **Diagramas são vivos** - mantenha-os atualizados com mudanças na arquitetura.

🎯 **Foco na clareza** - documentação deve ser útil tanto para developers quanto para stakeholders.
