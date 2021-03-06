import os

import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "7rf22yx3#lm(+d25m-_2kl(%wtvm=(%j7%m0&!20%e2r2283+p"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'grappelli.dashboard',
    "grappelli",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django_extensions',
    'home',
    'team',
    'tournament',
]

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

ROOT_URLCONF = 'martial.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'martial.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        # The default database that "ships with" Django is sqliteself.
        # Two lines under this defines the database. If your group uses
        # PostgreSQL, comment these lines out.
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        # If your group uses PostgreSQL comment out two lines under this,
        # and add other needed settings.
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': 'martial',
        # if you want to define user, password etc.
        # do it here
        # 'USER': 'postgres',
        # 'PASSWORD': 'root'
        # "NAME": "mart_db",
        # "USER": "mart_user",
        # "HOST": "martial_db",
        # "PASSWORD": "mart_password",
        # "PORT": 5432
    }
}

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Tunis'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500, ssl_require=True))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Using Django Email backends to simulate Email sending
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Cusomized User Model
# AUTH_USER_MODEL = 'users.CustomUser'

# Login and Logout Redirect URL
# LOGIN_REDIRECT_URL = 'profiles:my_home'
# LOGIN_URL = '/users/login'
# LOGOUT_REDIRECT_URL = '/users/login'
JET_SIDE_MENU_COMPACT = True

GRAPPELLI_ADMIN_TITLE="Martial Art"
GRAPPELLI_INDEX_DASHBOARD = 'martial.dashboard.CustomIndexDashboard'

try:
    # Configure Django App for Heroku.
    # doing this to avoid running the heroku test runner on github ci which make extra stuff with test db and crash the ci
    # should be after the BASE_DIR config
    # there is this option but it dosn't work : django_heroku.settings(locals(), test_runner=False)
    import django_heroku
    django_heroku.settings(locals())
except ImportError:
    found = False
