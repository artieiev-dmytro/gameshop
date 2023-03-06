from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-f@x8p&h*xj3q+p=67+=ssx5un*2b3xatb!h!1-780teeizfp%"

ALLOWED_HOSTS = []

DOMAIN_NAME = "http://127.0.0.1:8000"

# Debug
DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "debug_toolbar",
    "captcha",
    "common",
    "games",
    "users",
    "orders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

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
                "orders.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

# DataBase
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "gameshop",
        "USER": "gameshop_admin",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Media
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

CART_SESSION_ID = "cart"

LOGIN_REDIRECT_URL = "games:games"
LOGOUT_REDIRECT_URL = "games:games"

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "gameshopdjango@gmail.com"
EMAIL_HOST_PASSWORD = "dumzhhmehakegydv"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# OAuth
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "SCOPE": [
            "user",
            "repo",
            "read:org",
        ],
    }
}

# Celery
CELERY_BROKER_URL = "redis://127.0.0.1:6379"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379"

# Stripe
STRIPE_PUBLIC_KEY = "pk_test_51Mdi3BEnMwlpFVdZ1ripm1Ewyrgte0tnIF8n9KszKK9OfnWEdD6FIERV7wlp7eOEjYuBuZVdQQ8qPARMYbeMUBiN004l53PKIF"
STRIPE_SECRET_KEY = "sk_test_51Mdi3BEnMwlpFVdZxIHqTNaovSYJWhLvSaLzKHW2FmufLbtouIsWc3gvJ9Pi7WcpLdcV2IMx9aMVZKuMMmJ1JAPl00BC8fS82N"
STRIPE_WEBHOOK_SECRET = "whsec_2bd0ccdc9bb436b80a0197a6f9cff9ab8d53f8a5aaa28d0ace7b474e824858e7"
APPEND_SLASH = False

# Captcha
CAPTCHA_CHALLENGE_FUNCT = "captcha.helpers.math_challenge"
