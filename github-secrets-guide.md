# GitHub Actions Secrets para Firebase Deploy

# No repositório GitHub: Settings → Secrets and variables → Actions

# Secrets necessários para CI/CD:

# 1. Firebase Token para deploy automático
FIREBASE_TOKEN=<token-do-firebase-cli>
# Para obter: firebase login:ci

# 2. Firebase Service Account (mais seguro)
FIREBASE_SERVICE_ACCOUNT_GESTONGO_APP=<json-da-service-account>

# 3. Configurações Firebase para build
VITE_FIREBASE_API_KEY=AIzaSyB0PxRHDzPPq6EcSpiMMwirWWfwUhBmamQ
VITE_FIREBASE_AUTH_DOMAIN=gestongo-app.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=gestongo-app
VITE_FIREBASE_STORAGE_BUCKET=gestongo-app.firebasestorage.app
VITE_FIREBASE_MESSAGING_SENDER_ID=49732729437
VITE_FIREBASE_APP_ID=1:49732729437:web:4f20a0600cbe8a66472bb4
VITE_FIREBASE_MEASUREMENT_ID=G-E2N9HME0FQ

# 4. Backend secrets para deploy
JWT_SECRET_KEY=<sua-chave-jwt-secreta>
DATABASE_URL=<url-da-base-de-dados>

# 5. Docker secrets (se usar)
DOCKER_USERNAME=<username>
DOCKER_PASSWORD=<password>
