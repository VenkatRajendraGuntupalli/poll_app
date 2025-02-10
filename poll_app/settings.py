import os
from pathlib import Path

DEBUG = True  # ✅ Keep this True for development

# ✅ BASE_DIR should be set at the beginning of settings.py
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-6crqbgs5f6ze17nrg0v!bn^cw5e79#3cw49#&1g1wayoz9radu'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # ✅ This must be included
    'polls',
    'widget_tweaks',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # ✅ Leave this empty or set a custom templates directory
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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # ✅ Ensure this line is included
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ✅ Ensure this line is included
    'django.contrib.messages.middleware.MessageMiddleware',  # ✅ Ensure this line is included
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'poll_app.urls'  # ✅ Ensure this line exists

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # ✅ Make sure this is correct
        'NAME': BASE_DIR / 'db.sqlite3',  # ✅ Ensure this is correct
    }
}



ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # ✅ Add this line


BASE_DIR = Path(__file__).resolve().parent.parent

# Static files settings
STATIC_URL = '/static/'

# Where collectstatic will store static files (for production)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Where Django should look for additional static files (for development)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'polls/static/polls/'),  # ✅ Ensure this exists
]
