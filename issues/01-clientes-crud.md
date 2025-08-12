# [Clientes] CRUD completo

## 📋 Descrição
Implementar no backend e frontend a gestão de clientes com Create, Read, Update e Delete.

## 🎯 Objetivo
Permitir que o utilizador crie e edite clientes, consulte a lista e elimine clientes existentes.

## 🔧 Escopo Técnico
- [ ] **Backend:** API REST para clientes (Express + BD)
  - [ ] `POST /api/clientes` - Criar cliente
  - [ ] `GET /api/clientes` - Listar clientes
  - [ ] `GET /api/clientes/:id` - Obter cliente
  - [ ] `PUT /api/clientes/:id` - Atualizar cliente
  - [ ] `DELETE /api/clientes/:id` - Eliminar cliente
  
- [ ] **Frontend:** Lista de clientes e formulários
  - [ ] Componente `ClientesList` com tabela responsiva
  - [ ] Componente `ClienteForm` para criar/editar
  - [ ] Hook `useClientes` para gestão de estado
  - [ ] Validação de campos obrigatórios
  
- [ ] **Validação:** Campos obrigatórios no servidor
  - [ ] Nome (min 3 caracteres)
  - [ ] Email (formato válido)
  - [ ] Telefone (formato português)
  
- [ ] **Testes:** Jest + Supertest + React Testing Library
  - [ ] Testes unitários dos endpoints
  - [ ] Testes de integração da API
  - [ ] Testes dos componentes React

## ✅ Critérios de Aceitação
- [ ] Todos os testes passam no CI/CD
- [ ] Funciona no ambiente Docker de produção
- [ ] Deploy realizado no servidor
- [ ] Interface responsiva (mobile + desktop)
- [ ] Mensagens de erro claras para o utilizador
- [ ] Confirmação antes de eliminar cliente

## 📊 Estimativa
**Complexidade:** Média  
**Tempo estimado:** 2-3 dias  
**Dependências:** Base de dados configurada

## 🔗 Links Relacionados
- Issue de configuração da BD: #TBD
- Documentação da API: `/docs/api.md`
