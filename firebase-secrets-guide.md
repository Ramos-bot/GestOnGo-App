# Firebase Functions Environment Variables

# Instalar Firebase CLI com suporte a secrets
# npm install -g firebase-tools

# Para configurar secrets no Firebase Functions:

# 1. Definir secrets para Cloud Functions
firebase functions:secrets:set SECRET_NAME

# 2. Usar secrets nas Cloud Functions
# functions/index.js:
# const { defineSecret } = require("firebase-functions/params");
# const mySecret = defineSecret("SECRET_NAME");

# 3. Configurar secrets via CLI
# firebase functions:secrets:set JWT_SECRET_KEY
# firebase functions:secrets:set DATABASE_URL
# firebase functions:secrets:set EMAIL_API_KEY

# 4. Para usar no código:
# const { onRequest } = require("firebase-functions/v2/https");
# const { defineSecret } = require("firebase-functions/params");
# 
# const jwtSecret = defineSecret("JWT_SECRET_KEY");
# 
# exports.api = onRequest(
#   { secrets: [jwtSecret] },
#   (req, res) => {
#     const secret = jwtSecret.value();
#     // Use o secret aqui
#   }
# );

# Exemplos de secrets comuns para GestOnGo:
# firebase functions:secrets:set JWT_SECRET_KEY
# firebase functions:secrets:set DB_CONNECTION_STRING  
# firebase functions:secrets:set EMAIL_SERVICE_KEY
# firebase functions:secrets:set STRIPE_SECRET_KEY
