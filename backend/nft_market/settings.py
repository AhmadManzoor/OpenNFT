"""
Django settings for nft_market project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from google.oauth2 import service_account
import mimetypes
mimetypes.add_type("text/css", ".css", True)

GS_CREDENTIALS = service_account.Credentials.from_service_account_file( "./nft_market/credentials.json" )
USE_TESTNET = os.environ.get("USE_TESTNET", "1") == "1"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "#4vw_a2_1w&*=_(*3wm(3=650hi_!m#zxc_r4f4c$texam7rk+"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "0") != "0"

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "django_filters",
    "nft_market.api",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "corsheaders.middleware.CorsPostCsrfMiddleware",
]

ROOT_URLCONF = "nft_market.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "nft_market.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DATABASES["default"]={'NAME': 'opennft', 'USER': 'root', 'PASSWORD': 'bamboo123', 'HOST': '127.0.0.1', 'PORT': 5432, 'CONN_MAX_AGE': 0, 'ENGINE': 'django.db.backends.mysql'}

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
    import dj_database_url

    DATABASES["default"] = dj_database_url.parse(DATABASE_URL)
    if "mysql" in DATABASE_URL:
        DATABASES["default"]["OPTIONS"] = {"charset": "utf8mb4"}
        DATABASES["default"]["TEST"] = {
            "CHARSET": "utf8mb4",
            "COLLATION": "utf8mb4_unicode_ci",
        }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/nft_market/static/"

#PURESTAKE_API_KEY = os.environ.get("PURESTAKE_API_KEY")
PURESTAKE_API_KEY = '1LFn3w2vuV7ZNpOgwCs1d1jKTzLXLEa6DAL8xYf0'
PURESTAKE_ALGOD_URL = "https://testnet-algorand.api.purestake.io/ps2"
PURESTAKE_INDEXER_URL = "https://testnet-algorand.api.purestake.io/idx2"

CORS_ALLOWED_ORIGINS = [
    "https://cifinetwork.com",
    "http://cifinetwork.com",
    "https://open-nft-gilt.vercel.app",
    "http://open-nft-gilt.vercel.app",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https:\/\/.+\.ulam\.io$",
    r"^https:\/\/.+\.ulam\.pro$",
]

CSRF_TRUSTED_ORIGINS = [
    "*.ulam.io",
    "*.ulam.pro",
    "https://nft-market-azure.vercel.app",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
}

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "x-view-as",
    "access-control-allow-origin",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_BUCKET_NAME = os.environ.get("GS_BUCKET_NAME", "opennft-bamboo")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": None,
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}

CELERY_BROKER_URL = "amqp://guest:guest@0.0.0.0:5672//"
# os.getenv(
#    "CELERY_CONFIG_MODULE", "amqp://guest:guest@0.0.0.0:5672//"
#)
