"""
Django settings for MisperrisCRUD project.

Generated by 'django-admin startproject' using Django 2.2.dev20180621213648.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'registro/static/js', 'serviceworker.js')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6=+@u80r+ze$w=sltv0$50!rf0nrey9=n&1p#^hibs=s6tg+^$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registro',
    'rest_framework',
    'social_django',
    'pwa',
    'post',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MisperrisCRUD.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'MisperrisCRUD.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xcmmlpfx',
        'USER': 'xcmmlpfx',
        'PASSWORD': 'HTzy0ReS3BKqw9rhg2neFuggsNEAz9-Q',
        'HOST': 'elmer.db.elephantsql.com',
        'PORT': '5432',
    }
}

AUTHENTICATION_BACKENDS = (
 'social_core.backends.open_id.OpenIdAuth', 
 'social_core.backends.google.GoogleOpenId',  
 'social_core.backends.google.GoogleOAuth2',  
 'django.contrib.auth.backends.ModelBackend',
)


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
LOGIN_URL = 'inicio'
LOGIN_REDIRECT_URL = 'index'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ebarreraespinoza@gmail.com'
EMAIL_HOST_PASSWORD = '*redrevolver12'
DEFAULT_FROM_EMAIL = 'django.core.mail.backends.smtp.EmailBackend>'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '850889740377-6s5kbctr7f296c62ce61o47hhlau01ei.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'nrh_OP4EFmdk_VDJDVg1XLTI'