import os
from datetime import timedelta
import environ
from pathlib import Path
import dj_database_url
env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']
# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.sitemaps',

    'whitenoise',
    'rest_framework',
    'django.contrib.staticfiles',

    'apps.api',
    'apps.accounts',
    'apps.finance',
    'apps.paystack',
    'apps.binx_crypto',
    'apps.crypto_world',
]

# HEALTH CHECK
INSTALLED_APPS += [
    # HEALTH CHECK SETTINGS
    'health_check',
    'health_check.contrib.psutil',
    'health_check.db',  
    # stock Django health checkers
    'health_check.cache',
    'health_check.storage',
    'health_check.contrib.migrations',
]

HEALTH_CHECK = {
    'DISK_USAGE_MAX': 90, #Percent
    'MEMORY_MIN': 100, # in MB
}

HEALTH_CHECK['DISK_USAGE_MAX'] = 5 * (1 << 30)   # 5GB in bytes

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



PAYSTACK_API_URL    = env("PAYSTACK_URL")
PAYSTACK_PUBLIC_KEY = env("PAYSTACK_TEST_KEY")
PAYSTACK_SECRET_KEY = env("PAYSTACK_LIVE_KEY")

PAYSTACK_SUCCESS_URL = "/payment/payment_successful"
# PAYSTACK_FAILED_URL = "/google/api"
# PAYSTACK_SUCCESS_URL = "/google/api"
PAYSTACK_WEBHOOK_DOMAIN = 'tuteria.ngrok.io'


KUDA_LIVE_URL   = env("KUDA_LIVE_URL")
KUDA_TEST_URL   = env("KUDA_TEST_URL")
KUDA_API_KEY    = env("KUDA_API_KEY")

SME_TOKEN       = env("SME_TOKEN")

# GMAIL CONFIGURATIONS
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          = 587  # For TLS
EMAIL_USE_TLS       = True
EMAIL_USE_SSL       = False  # Set to False for TLS
EMAIL_HOST_USER     = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'plugins/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'plugins/assets')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000"
    "http://localhost:3000",
]

CORS_ALLOW_ALL_ORIGINS: True
CORS_ALLOW_METHODS = (
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
)

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    
    'USER_ID_FIELD': 'user_id',
        
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,

    "JTI_CLAIM": "jti",
    
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
}

DJOSER = {
    "USER_CREATE_PASSWORD_RETYPE"           : True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION"   : True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION"   : True,
    "SEND_CONFIRMATION_EMAIL"               : True,
    "SET_USERNAME_RETYPE"                   : True,
    "SET_PASSWORD_RETYPE"                   : True,
    "SEND_ACTIVATION_EMAIL"                 : True,

    # "LOGIN_FIELD"                           : "email",
    # "USER_ID_FIELD"                         : "id,",
    # "PASSWORD_RESET_CONFIRM_URL"            : "password/reset/confirm/{uid}/{token}",
    # "USERNAME_RESET_CONFIRM_URL"            : "email/reset/confirm/{uid}/{token}",
    # "ACTIVATION_URL"                        : "activate/{uid}/{token}",
    
    # "SERIALIZERS": {
    #     'user_create'   : 'apps.accounts.api.serializers.UserRegistrationSerializer',
    #     'user'          : 'apps.accounts.api.serializers.UserProfileSerializer',
    #     'user_delete'   : 'djoser.serializers.UserDeleteSerializer',
    # },
}