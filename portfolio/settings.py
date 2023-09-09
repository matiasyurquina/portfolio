import os
from pathlib import Path
#from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eugp8gj1f#a)g3nfb#w_)!eqb_3b&_207_p8q!z_1)i6snt%%@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contact_app',
    'captcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'portfolio',
        'USER' : 'matias',
        'PASSWORD' : '123456',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.mysql',
#      'NAME': 'matiasyurquina$portfolio',       # Cambia esto al nombre de tu base de datos
#      'USER': 'matiasyurquina',      # Cambia esto al nombre de usuario de MySQL
#      'PASSWORD': 'G2220HDA',      # Cambia esto a la contraseña de MySQL
#      'HOST': 'matiasyurquina.mysql.pythonanywhere-services.com',                # Puedes cambiar esto si tu base de datos está en otro servidor
#      'PORT': '',                      # Puerto de MySQL (por defecto es 3306)
#  }
# }


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


RECAPTCHA_PUBLIC_KEY = '6LefdUcnAAAAAH6PGcpeH12PH7_FaUHyEXgJdOhD'
RECAPTCHA_PRIVATE_KEY = '6LefdUcnAAAAADkEtR-vvEaFnJe_9NEo1aTFwfgp'
RECAPTCHA_REQUIRED = True
RECAPTCHA_USE_SSL = False
