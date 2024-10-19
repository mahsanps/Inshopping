from pathlib import Path
import os
from decouple import config, Csv
import pymysql



pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
IS_LOCAL = config("IS_LOCAL", default=False, cast=bool)

# Authentication model
LOGIN_URL = "/login/"
AUTH_USER_MODEL = "authuser.Account"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Application definition
PROJECT_APPS = [
    'authuser',
    'store',
    'ui',
]

INSTALLED_APPS = [
    *PROJECT_APPS,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dal',
    'dal_select2',
    "django_htmx",
    'django_jalali',
    'django.contrib.humanize',
    'sslserver',
    'unidecode',
 

]

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'inshopping.urls'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'inshopping.wsgi.application'

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/django.log',
        },        
        
    },
    "root": {
        "handlers": ["console", 'file'],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console", 'file'],
            "level": "INFO",
            "propagate": False,
        },
    },
    "formatters": {
        "verbose": {
            "format": "[{levelname}] {asctime} {module} {filename} {funcName} {lineno} {message}",
            "style": "{",
        },
    },
}

# Database settings
if IS_LOCAL :
    DATABASES = {
        'default': {
            
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / config('DATABASE_URL', default='db.sqlite3'),

        }
    }

else :
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':config('DATABASE_NAME'), 
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),  
        'PORT': config('DATABASE_PORT'),  
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET SESSION sql_mode='STRICT_TRANS_TABLES'"
        },
        

    }
}
# Password validation
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

# Internationalization
LANGUAGE_CODE = 'fa'
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
LANGUAGES = [
    ('fa', 'Persian'),
]
TIME_ZONE = 'Asia/Tehran'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "statics"),
    os.path.join(BASE_DIR, "staticfiles"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "collected_static")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT =465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Instagram API settings
INSTAGRAM_CLIENT_ID = config('INSTAGRAM_CLIENT_ID')
INSTAGRAM_CLIENT_SECRET = config('INSTAGRAM_CLIENT_SECRET')
INSTAGRAM_REDIRECT_URI = config('INSTAGRAM_REDIRECT_URI')

# Zarinpal settings
ZARINPAL_MERCHANT_ID = config('ZARINPAL_MERCHANT_ID')
ZARINPAL_CALLBACK_URL = config('ZARINPAL_CALLBACK_URL')
ZARINPAL_WEBSERVICE = config('ZARINPAL_WEBSERVICE')
ZARINPAL_PAYMENT_VERIFICATION = config('ZARINPAL_PAYMENT_VERIFICATION')
