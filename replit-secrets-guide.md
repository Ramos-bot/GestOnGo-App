# Configuração de Secrets no Replit para GestOnGo Backend

## 1. Secrets no Replit Console

No painel do Replit, acesse a aba "Secrets" (ícone de chave) e adicione:

### Secrets de Autenticação:
```
JWT_SECRET_KEY = your-super-secret-jwt-key-here-min-32-chars
JWT_ALGORITHM = HS256
JWT_EXPIRATION_MINUTES = 30
```

### Secrets de Base de Dados:
```
DATABASE_URL = sqlite:///./gestongo.db
DATABASE_TYPE = sqlite
```

### Secrets da Aplicação:
```
APP_NAME = GestOnGo
APP_VERSION = 2.0.0
ENVIRONMENT = production
DEBUG = false
```

### Secrets de Email (se usar):
```
EMAIL_HOST = smtp.gmail.com
EMAIL_PORT = 587
EMAIL_USERNAME = your-email@gmail.com
EMAIL_PASSWORD = your-app-password
EMAIL_FROM = noreply@gestongo.com
```

### Secrets de Módulos:
```
MODULO_VERDE_ATIVO = true
MODULO_AQUA_ATIVO = true
ENABLE_ADMIN_ROUTES = true
```

### Secrets de CORS (para permitir frontend):
```
ALLOWED_ORIGINS = https://gestongo-app.web.app,https://gestongo-app.firebaseapp.com,http://localhost:5173
CORS_ALLOW_CREDENTIALS = true
```

## 2. Como adicionar secrets:

1. No Replit, abra o projeto GestOnGo
2. Clique na aba "Secrets" (🔑) no painel lateral
3. Clique em "Add new secret"
4. Nome: JWT_SECRET_KEY
5. Valor: (gere uma chave segura)
6. Clique "Add secret"
7. Repita para todos os secrets acima

## 3. Gerar JWT Secret Key segura:

```python
import secrets
import string

def generate_jwt_secret():
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for i in range(64))

print(generate_jwt_secret())
```

## 4. Verificar secrets no código:

```python
import os

# Verificar se secrets estão carregados
required_secrets = [
    "JWT_SECRET_KEY",
    "DATABASE_URL", 
    "APP_NAME"
]

for secret in required_secrets:
    value = os.environ.get(secret)
    if value:
        print(f"✅ {secret}: {'*' * len(value)}")
    else:
        print(f"❌ {secret}: NOT SET")
```
