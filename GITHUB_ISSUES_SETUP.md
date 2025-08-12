# 📋 **GUIA: Como Criar Issues no GitHub**

## 🚀 **Passo a Passo**

### **1. Acessar o Repositório**
```
https://github.com/Ramos-bot/GestOnGo-App/issues
```

### **2. Criar Nova Issue**
- Clicar em **"New Issue"**
- Copiar o conteúdo de cada ficheiro `issues/*.md`
- Usar o título do ficheiro como título da issue

### **3. Labels Recomendadas**
Para cada issue, aplicar estas labels:

**01-clientes-crud.md:**
- `enhancement`
- `backend`
- `frontend`
- `good first issue`

**02-tarefas-agendamento.md:**
- `enhancement`
- `backend`
- `frontend`
- `complex`

**03-servicos-prestados.md:**
- `enhancement`
- `backend`
- `frontend`
- `file-upload`

**04-auth-firebase.md:**
- `enhancement`
- `security`
- `authentication`
- `firebase`

**05-dashboard-estatisticas.md:**
- `enhancement`
- `frontend`
- `analytics`
- `ui/ux`

### **4. Assignees e Milestones**
- **Assignee:** Atribuir a si próprio ou equipa
- **Milestone:** Criar milestone "MVP v1.0"
- **Projects:** Adicionar ao projeto "GestOnGo Development"

---

## 📊 **Template de Issue GitHub**

```markdown
<!-- Copiar este template para cada issue -->

## 📋 Descrição
[Descrição da funcionalidade]

## 🎯 Objetivo
[Objetivo de negócio]

## 🔧 Escopo Técnico
[Lista de tarefas técnicas]

## ✅ Critérios de Aceitação
[Critérios de aceitação]

## 📊 Estimativa
**Complexidade:** [Baixa/Média/Alta]
**Tempo estimado:** [X dias]
**Dependências:** [Links para outras issues]

## 🔗 Links Relacionados
[Links para documentação/recursos]
```

---

## 🎯 **Ordem de Implementação Recomendada**

### **Sprint 1 (Semana 1-2):**
1. **#04 Auth Firebase** - Base para tudo
2. **#01 Clientes CRUD** - Funcionalidade fundamental

### **Sprint 2 (Semana 3-4):**
3. **#02 Tarefas Agendamento** - Depende de Clientes
4. **#05 Dashboard** - Depende de dados existirem

### **Sprint 3 (Semana 5-6):**
5. **#03 Serviços + Upload** - Funcionalidade mais complexa

---

## 🤖 **Automações Sugeridas**

### **GitHub Actions para Issues:**
```yaml
# .github/workflows/issue-automation.yml
name: Issue Automation
on:
  issues:
    types: [opened, labeled]

jobs:
  auto-assign:
    runs-on: ubuntu-latest
    steps:
      - name: Auto-assign to project
        uses: alex-page/github-project-automation-plus@v0.8.1
        with:
          project: GestOnGo Development
          column: To Do
```

### **Template Automático:**
```yaml
# .github/ISSUE_TEMPLATE/feature.yml
name: 🚀 Feature Request
description: Propor nova funcionalidade
body:
  - type: markdown
    attributes:
      value: "Obrigado por contribuir para o GestOnGo!"
  - type: textarea
    id: description
    attributes:
      label: "📋 Descrição"
      placeholder: "Descreva a funcionalidade..."
    validations:
      required: true
```

---

## 📈 **Tracking Progress**

### **Usar GitHub Projects:**
1. Criar projeto "GestOnGo MVP"
2. Colunas: `Backlog` → `In Progress` → `Review` → `Done`
3. Adicionar todas as 5 issues ao projeto
4. Mover conforme progresso

### **Métricas a Acompanhar:**
- ✅ **Velocity:** Issues concluídas por sprint
- 📊 **Burn-down:** Progresso ao longo do tempo  
- 🐛 **Bug ratio:** Issues vs bugs encontrados
- ⏱️ **Lead time:** Tempo médio de conclusão

---

## 💡 **Dicas de Produtividade**

### **Para o GitHub Copilot:**
- Mencionar número da issue nos commits: `feat: implement client CRUD (#1)`
- Referenciar issues em PRs: `Closes #1`
- Usar labels para contexto: `backend`, `frontend`, etc.

### **Para a Equipa:**
- **Daily standups:** Qual issue está a trabalhar?
- **Code reviews:** Verificar se cumpre critérios de aceitação
- **Demo sessions:** Mostrar funcionalidades concluídas

---

**🎉 Com esta organização, terá um workflow profissional e escalável!**
