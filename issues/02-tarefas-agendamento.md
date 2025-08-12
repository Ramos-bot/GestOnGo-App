# [Tarefas] CRUD + Agendamento

## 📋 Descrição
Gestão de tarefas ligadas a clientes, com datas de execução e possibilidade de reagendar.

## 🎯 Objetivo
Organizar a agenda de serviços da empresa com sistema de agendamento inteligente.

## 🔧 Escopo Técnico
- [ ] **Backend:** API REST para tarefas (CRUD + lógica de datas)
  - [ ] `POST /api/tarefas` - Criar tarefa
  - [ ] `GET /api/tarefas` - Listar tarefas (filtros por data/cliente)
  - [ ] `PUT /api/tarefas/:id` - Atualizar tarefa
  - [ ] `PATCH /api/tarefas/:id/reagendar` - Reagendar tarefa
  - [ ] `DELETE /api/tarefas/:id` - Eliminar tarefa
  
- [ ] **Frontend:** Interface de agendamento
  - [ ] Vista de calendário semanal/mensal
  - [ ] Vista de lista diária
  - [ ] Drag & drop para reagendamento
  - [ ] Filtros por cliente/estado/tipo
  
- [ ] **Funcionalidades Avançadas:**
  - [ ] Notificações de tarefas próximas
  - [ ] Conflitos de agendamento (avisos)
  - [ ] Tarefas recorrentes (semanal/mensal)
  - [ ] Estados: Agendada, Em curso, Concluída, Cancelada
  
- [ ] **Testes:** Cobertura completa
  - [ ] Testes de lógica de agendamento
  - [ ] Testes de conflitos de data
  - [ ] Testes de recorrência

## ✅ Critérios de Aceitação
- [ ] Todos os testes passam no CI/CD
- [ ] Funciona no ambiente Docker de produção
- [ ] Deploy realizado no servidor
- [ ] Calendário responsivo e intuitivo
- [ ] Reagendamento funciona corretamente
- [ ] Notificações aparecem no momento certo

## 📊 Estimativa
**Complexidade:** Alta  
**Tempo estimado:** 4-5 dias  
**Dependências:** Módulo de Clientes concluído

## 🔗 Links Relacionados
- Issue de Clientes: `#01-clientes-crud`
- Biblioteca de calendário: React Big Calendar
- Documentação de notificações: `/docs/notifications.md`
