"""
Configurações para produção no Replit
Carrega secrets do ambiente Replit
"""
import os
from typing import List

class ReplitConfig:
    """Configurações específicas para deploy no Replit"""
    
    # Autenticação JWT
    JWT_SECRET_KEY: str = os.environ.get("JWT_SECRET_KEY", "dev-secret-key-change-in-production")
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION_MINUTES: int = int(os.environ.get("JWT_EXPIRATION_MINUTES", "30"))
    
    # Base de dados
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "sqlite:///./gestongo.db")
    DATABASE_TYPE: str = os.environ.get("DATABASE_TYPE", "sqlite")
    
    # Aplicação
    APP_NAME: str = os.environ.get("APP_NAME", "GestOnGo")
    APP_VERSION: str = os.environ.get("APP_VERSION", "2.0.0")
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT", "production")
    DEBUG: bool = os.environ.get("DEBUG", "false").lower() == "true"
    
    # Módulos
    MODULO_VERDE_ATIVO: bool = os.environ.get("MODULO_VERDE_ATIVO", "true").lower() == "true"
    MODULO_AQUA_ATIVO: bool = os.environ.get("MODULO_AQUA_ATIVO", "true").lower() == "true"
    ENABLE_ADMIN_ROUTES: bool = os.environ.get("ENABLE_ADMIN_ROUTES", "true").lower() == "true"
    
    # CORS - Origins permitidas
    ALLOWED_ORIGINS: List[str] = os.environ.get(
        "ALLOWED_ORIGINS", 
        "https://gestongo-app.web.app,https://gestongo-app.firebaseapp.com,http://localhost:5173"
    ).split(",")
    CORS_ALLOW_CREDENTIALS: bool = os.environ.get("CORS_ALLOW_CREDENTIALS", "true").lower() == "true"
    
    # Email (opcional)
    EMAIL_HOST: str = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_PORT: int = int(os.environ.get("EMAIL_PORT", "587"))
    EMAIL_USERNAME: str = os.environ.get("EMAIL_USERNAME", "")
    EMAIL_PASSWORD: str = os.environ.get("EMAIL_PASSWORD", "")
    EMAIL_FROM: str = os.environ.get("EMAIL_FROM", "noreply@gestongo.com")
    
    # Configurações do servidor
    HOST: str = os.environ.get("HOST", "0.0.0.0")
    PORT: int = int(os.environ.get("PORT", "8000"))
    
    @classmethod
    def verify_secrets(cls) -> dict:
        """Verifica se todos os secrets necessários estão configurados"""
        required_secrets = [
            "JWT_SECRET_KEY",
            "DATABASE_URL",
            "APP_NAME"
        ]
        
        status = {}
        for secret in required_secrets:
            value = os.environ.get(secret)
            status[secret] = {
                "configured": bool(value),
                "value_length": len(value) if value else 0
            }
        
        return status
    
    @classmethod
    def get_database_url(cls) -> str:
        """Retorna URL da base de dados configurada"""
        return cls.DATABASE_URL
    
    @classmethod
    def get_cors_settings(cls) -> dict:
        """Retorna configurações CORS"""
        return {
            "allow_origins": cls.ALLOWED_ORIGINS,
            "allow_credentials": cls.CORS_ALLOW_CREDENTIALS,
            "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["*"]
        }
    
    @classmethod
    def is_development(cls) -> bool:
        """Verifica se está em modo desenvolvimento"""
        return cls.ENVIRONMENT == "development" or cls.DEBUG
    
    @classmethod
    def print_config_status(cls):
        """Imprime status da configuração (sem mostrar valores sensíveis)"""
        print(f"🚀 {cls.APP_NAME} v{cls.APP_VERSION}")
        print(f"🌍 Environment: {cls.ENVIRONMENT}")
        print(f"🔧 Debug: {cls.DEBUG}")
        print(f"📊 Database: {cls.DATABASE_TYPE}")
        print(f"🔐 JWT Algorithm: {cls.JWT_ALGORITHM}")
        print(f"⏰ JWT Expiration: {cls.JWT_EXPIRATION_MINUTES} minutes")
        print(f"🌐 CORS Origins: {len(cls.ALLOWED_ORIGINS)} configured")
        print(f"📧 Email configured: {bool(cls.EMAIL_USERNAME)}")
        print(f"🟢 Verde Module: {cls.MODULO_VERDE_ATIVO}")
        print(f"🔵 Aqua Module: {cls.MODULO_AQUA_ATIVO}")
        
        # Verificar secrets
        secrets_status = cls.verify_secrets()
        print("\n🔑 Secrets Status:")
        for secret, info in secrets_status.items():
            status = "✅" if info["configured"] else "❌"
            length = f"({info['value_length']} chars)" if info["configured"] else "(not set)"
            print(f"   {status} {secret} {length}")

# Instância da configuração
config = ReplitConfig()
