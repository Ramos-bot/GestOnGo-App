# 🤖 **PROMPTS GITHUB COPILOT - GestOnGo**

## 🎯 **Backend (Express + Node.js)**

### **CRUD Completo**
```
Cria endpoints REST em Express para um recurso 'clientes' com CRUD completo, usando async/await, validação simples, e responde em JSON. Incluir testes Jest com Supertest para todos os endpoints.
```

### **Middleware de Validação**
```
Cria middleware Express para validar dados de entrada usando joi ou express-validator. Deve retornar erro 400 com detalhes da validação se os dados estiverem inválidos.
```

### **Autenticação JWT**
```
Implementa middleware de autenticação JWT para Express. Deve verificar o token no header Authorization, decodificar o payload e adicionar o usuário ao req.user.
```

### **Conexão Database**
```
Cria conexão com MongoDB usando mongoose ou PostgreSQL usando pg. Inclui pool de conexões, tratamento de erros e função de health check.
```

## ⚛️ **Frontend (React + CRA)**

### **Lista com CRUD**
```
Cria um componente React funcional chamado ClientesList que carrega clientes de /api/clientes com useEffect, mostra numa tabela, e permite apagar um cliente com botão 'Remover'. Usar fetch e atualizar estado local.
```

### **Formulário Controlado**
```
Cria componente React de formulário para adicionar/editar cliente com campos nome, email, telefone. Usar useState para controlar inputs, validação básica e submit para API.
```

### **Hook Customizado**
```
Implementa hook customizado useClientes que consome API /api/clientes. O hook deve devolver loading, erro, dados e funções para create, update, delete.
```

### **Context Provider**
```
Cria AuthContext e AuthProvider para React que gerencia estado de autenticação, login/logout e proteção de rotas. Usar localStorage para persistir token.
```

## 🔗 **Integração Full Stack**

### **API + Hook**
```
Implementa no backend a rota GET /clientes que devolve JSON e no frontend um hook useClientes que consome essa API. O hook deve devolver loading, erro e dados.
```

### **Upload de Arquivos**
```
Cria endpoint Express para upload de arquivos usando multer e componente React com input file e preview de imagem. Incluir validação de tipo e tamanho.
```

### **Pesquisa e Filtros**
```
Implementa sistema de pesquisa: backend com query params para filtrar dados e frontend com input de pesquisa que atualiza resultados em tempo real.
```

## 🧪 **Testes**

### **Testes Backend**
```
Cria testes Jest + Supertest para API REST completa: teste todos os endpoints, status codes, formatos de resposta e cenários de erro.
```

### **Testes Frontend**
```
Cria testes React Testing Library para componente de lista: renderização, interação com botões, chamadas de API mockadas e atualização de estado.
```

### **Testes E2E**
```
Cria teste Playwright que: abre a aplicação, faz login, navega para lista de clientes, adiciona novo cliente, verifica se aparece na lista.
```

## 🐳 **DevOps**

### **Dockerfile Otimizado**
```
Cria Dockerfile multi-stage para app React: stage de build com Node.js, stage de produção com Nginx, copy apenas arquivos necessários, otimizar para cache de layers.
```

### **Docker Compose**
```
Cria docker-compose.yml com serviços: frontend (React), backend (Express), database (PostgreSQL), volumes para persistência e network entre containers.
```

### **GitHub Actions**
```
Cria workflow GitHub Actions que: instala dependencies, roda testes, builda Docker images, publica no GHCR e faz deploy automático em push para main.
```

## 📱 **UI/UX**

### **Loading States**
```
Cria componente LoadingSpinner reutilizável e hook useLoading para gerenciar estados de carregamento em toda aplicação React.
```

### **Error Boundaries**
```
Implementa Error Boundary React para capturar erros de componentes, mostrar UI de fallback e logs estruturados para debugging.
```

### **Responsive Design**
```
Cria layout responsivo com CSS Grid/Flexbox: sidebar fixa desktop, menu hambúrguer mobile, tabelas scrolláveis, buttons touch-friendly.
```

## 🔧 **Utilitários**

### **Validação de Schema**
```
Cria schema de validação com Joi ou Zod para entidade Cliente: campos obrigatórios, formatos de email/telefone, mensagens personalizadas.
```

### **Formatação de Dados**
```
Cria funções utilitárias para formatar: datas (pt-BR), moeda (EUR), telefone, CPF/CNPJ. Funcionar tanto no frontend quanto backend.
```

### **Logger Estruturado**
```
Implementa sistema de logs com Winston ou Pino: diferentes níveis, formato JSON, correlationId para rastrear requests, integração com Express.
```

---

## 💡 **Dicas de Uso:**

1. **Seja Específico**: Mencione tecnologias exatas (Express, React, Jest)
2. **Inclua Contexto**: "para aplicação de gestão de clientes"
3. **Defina Escopo**: "CRUD completo" vs "apenas listar"
4. **Peça Testes**: Sempre incluir "com testes"
5. **Estrutura Clara**: "usando async/await", "responder JSON"

## 🎯 **Templates Rápidos:**

```bash
# Backend Express endpoint
"Cria endpoint POST /api/[recurso] que [ação] usando [tecnologia] e retorna [formato]"

# Frontend React component  
"Cria componente React [nome] que [funcionalidade] usando [hooks] e [estilo]"

# Integração completa
"Implementa [feature] completa: backend [tecnologia] + frontend [tecnologia] + testes"
```
