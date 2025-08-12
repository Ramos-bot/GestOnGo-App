# [Serviços Prestados] CRUD + Upload de fotos

## 📋 Descrição
Registar serviços prestados a clientes, com descrição, data, duração, valor e documentação fotográfica.

## 🎯 Objetivo
Gerar histórico detalhado de serviços com documentação visual e geração automática de documentos.

## 🔧 Escopo Técnico
- [ ] **Backend:** API REST com upload de ficheiros
  - [ ] `POST /api/servicos` - Registar serviço
  - [ ] `POST /api/servicos/:id/fotos` - Upload de fotos
  - [ ] `GET /api/servicos` - Listar serviços (filtros)
  - [ ] `GET /api/servicos/:id/pdf` - Gerar PDF do serviço
  - [ ] `DELETE /api/servicos/:id` - Eliminar serviço
  
- [ ] **Storage:** Firebase Storage ou AWS S3
  - [ ] Upload múltiplo de imagens
  - [ ] Compressão automática de imagens
  - [ ] Organização por pastas (cliente/data)
  - [ ] URLs seguras para acesso
  
- [ ] **Frontend:** Interface de registo
  - [ ] Formulário de registo de serviço
  - [ ] Upload drag & drop de fotos
  - [ ] Preview das imagens antes do upload
  - [ ] Galeria de fotos do serviço
  
- [ ] **Geração de PDF:**
  - [ ] Template profissional para notas de despesa
  - [ ] Dados do serviço + fotos
  - [ ] Logo da empresa
  - [ ] Assinatura digital (opcional)
  
- [ ] **Testes:** Upload e geração de documentos
  - [ ] Testes de upload de ficheiros
  - [ ] Testes de geração de PDF
  - [ ] Testes de validação de formatos

## ✅ Critérios de Aceitação
- [ ] Todos os testes passam no CI/CD
- [ ] Funciona no ambiente Docker de produção
- [ ] Deploy realizado no servidor
- [ ] Upload funciona em mobile e desktop
- [ ] PDFs gerados com qualidade profissional
- [ ] Fotos são comprimidas automaticamente
- [ ] Suporte a formatos: JPG, PNG, WebP

## 📊 Estimativa
**Complexidade:** Alta  
**Tempo estimado:** 5-6 dias  
**Dependências:** Firebase Storage configurado, Módulo de Clientes

## 🔗 Links Relacionados
- Issue de Clientes: `#01-clientes-crud`
- Issue de Tarefas: `#02-tarefas-agendamento`
- Firebase Storage docs: [Link](https://firebase.google.com/docs/storage)
- PDF.js para geração: [Link](https://pdfkit.org/)
