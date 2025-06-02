from pathlib import Path
from datetime import timedelta
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default="insecure.dev.application")

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

MIDDLEWARE = [
    # 'tenant_schemas.middleware.TenantMiddleware', # Eliminado
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8081', # Or whatever port your Expo app runs on
    'exp://192.168.1.11:8081', # For Expo Go / Dev Client
]

# Configuraciones de tenant_schemas eliminadas
# TENANT_MODEL = "tenants.Client"
# PUBLIC_SCHEMA_NAME = config('PUBLIC_SCHEMA_NAME', default='public')
# DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'

# SHARED_APPS y TENANT_APPS eliminadas

INSTALLED_APPS = [
    # 'tenant_schemas', # Eliminado
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    'core',
    # 'tenants', # Eliminado/Comentado
    
    'authentication',
    'winning_record',
    'structure',
    'origin',
    'draw',
    'financial_statement',
    'game_type',
    'number_limit_rule',
    'payout_rule',
    'bet',
    'roles',
    'user_structure',
]

# DATABASE_ROUTERS eliminados
# DATABASE_ROUTERS = ['tenant_schemas.routers.TenantSyncRouter']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Correcto
        'NAME': config('DB_NAME', default='gamereset'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default='postgres'),
        'HOST': config('DB_HOST', default='db'),
        'PORT': config('DB_PORT', default='5432', cast=int),
    }
}

# Redis Configuration
REDIS_HOST = config('REDIS_HOST', default='redis')
REDIS_PORT = config('REDIS_PORT', default='6379', cast=int)

# RabbitMQ Configuration
RABBITMQ_CONNECTION = {
    'host': config('RABBITMQ_HOST', default='rabbitmq'),
    'port': config('RABBITMQ_PORT', default='5672', cast=int),
    'username': config('RABBITMQ_USER', default='guest'),
    'password': config('RABBITMQ_PASSWORD', default='guest')
}

# Cache Configuration
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Asegúrate de que DEFAULT_FILE_STORAGE se ajuste si es necesario, o elimínalo si el default de Django es suficiente.
# Por ejemplo, para almacenamiento local estándar:
# DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Root URL Configuration
ROOT_URLCONF = 'config.urls'

# TENANT_DOMAIN = 'localhost' # Eliminado
SITE_ID = 1