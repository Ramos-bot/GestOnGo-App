# 🚀 Deploy GestOnGo no Replit - Guia Passo a Passo

## Status Atual: ❌ Projeto não encontrado no Replit

## 📋 Passos para Deploy Manual:

### 1. **Criar Novo Repl no Replit**
1. Vá para: https://replit.com
2. Clique "Create Repl"
3. Selecione "Import from GitHub"
4. Cole a URL: `https://github.com/Ramos-bot/GestOnGo-App`
5. Nome do Repl: `GestOnGo-App`
6. Clique "Import from GitHub"

### 2. **Configurar Secrets (CRÍTICO)**
Na aba "Secrets" (🔑) do Replit, adicione:

```
JWT_SECRET_KEY = !%59v0vP#:xKWsr$pJm1UeTUO@=afLW){!n}vL)(cMKC:P!9GTnapMyV{#;E}M<,
JWT_ALGORITHM = HS256
JWT_EXPIRATION_MINUTES = 30
DATABASE_URL = sqlite:///./gestongo.db
DATABASE_TYPE = sqlite
APP_NAME = GestOnGo
APP_VERSION = 2.0.0
ENVIRONMENT = production
DEBUG = false
MODULO_VERDE_ATIVO = true
MODULO_AQUA_ATIVO = true
ENABLE_ADMIN_ROUTES = true
ALLOWED_ORIGINS = https://gestongo-app.web.app,https://gestongo-app.firebaseapp.com,http://localhost:5173
CORS_ALLOW_CREDENTIALS = true
HOST = 0.0.0.0
PORT = 8000
```

### 3. **Verificar Configuração**
O Replit deve automaticamente:
- ✅ Ler o arquivo `.replit`
- ✅ Instalar dependências do `requirements.txt`
- ✅ Configurar Python 3.11
- ✅ Expor porta 8000

### 4. **Executar o Projeto**
1. Clique o botão "Run" ▶️
2. Aguarde instalação das dependências
3. O servidor deve iniciar na porta 8000

### 5. **URLs Esperadas Após Deploy**
- **API Principal**: `https://gestongo-app.ramos-bot.repl.co`
- **Documentação**: `https://gestongo-app.ramos-bot.repl.co/docs`
- **Health Check**: `https://gestongo-app.ramos-bot.repl.co/health`
- **Config Status**: `https://gestongo-app.ramos-bot.repl.co/config`

### 6. **Verificar Funcionamento**
Execute o endpoint `/config` para verificar:
```json
{
  "app_name": "GestOnGo",
  "version": "2.0.0",
  "environment": "production",
  "secrets_configured": {
    "JWT_SECRET_KEY": true,
    "DATABASE_URL": true,
    "APP_NAME": true
  }
}
```

## 🔧 Troubleshooting

### Se o projeto não iniciar:
1. **Verificar Console**: Aba "Console" para logs de erro
2. **Verificar Secrets**: Todos os secrets configurados?
3. **Verificar .replit**: Comando de run correto?
4. **Reinstalar**: Delete e reimporte do GitHub

### Se der erro de imports:
1. Verificar se `requirements.txt` foi lido
2. Executar manualmente: `pip install -r requirements.txt`
3. Verificar estrutura de pastas

### Se der erro de database:
1. O SQLite será criado automaticamente
2. Verificar permissões de escrita
3. Verificar path do DATABASE_URL

## ✅ Checklist de Deploy

- [ ] Projeto importado do GitHub
- [ ] Secrets configurados
- [ ] Servidor a executar
- [ ] URL principal acessível
- [ ] Endpoint `/docs` funcionando
- [ ] Endpoint `/config` mostra secrets configurados
- [ ] CORS configurado para Firebase
- [ ] Autenticação JWT funcionando

## 🎯 Resultado Esperado

Após configuração completa:
- **Backend**: Disponível publicamente no Replit
- **Frontend**: Deploy no Firebase apontando para o backend
- **Sistema**: Totalmente funcional em produção

---

**Última verificação**: 2025-08-12 00:33:13  
**Status**: ❌ Aguarda import manual no Replit
