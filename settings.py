# settings.py

# Import necessary modules
import os
from pathlib import Path
from django.contrib.auth.models import User

# Define base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-here'  # Change this to a secret key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Define allowed hosts (domain names)
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin panel
    'django.contrib.auth',   # Auth system
    'django.contrib.contenttypes',  # Content types framework
    'django.contrib.sessions',  # Session management
    'django.contrib.messages',  # Messaging framework
    'django.contrib.staticfiles',  # Static files (CSS, JavaScript, images)
    'file_app',  # Your custom app
]

# Middleware settings for request handling
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security settings
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session management
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # Messages framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # X-Frame Options
]

# Root URL configuration
ROOT_URLCONF = 'secure_file_sharing.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Django's template engine
        'DIRS': [BASE_DIR / 'templates'],  # Directory for templates
        'APP_DIRS': True,  # Enable app-specific templates
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',  # Authentication context processor
                'django.contrib.messages.context_processors.messages',  # Messages context processor
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'secure_file_sharing.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite database
        'NAME': BASE_DIR / 'db.sqlite3',  # Path to SQLite database file
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Similarity validation
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Minimum length validation
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Common password validation
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Numeric password validation
    },
]

# Static files (CSS, JavaScript, images) configuration
STATIC_URL = '/static/'  # URL for static files
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Directory for static files
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directory where collected static files will be stored

# Media files configuration
MEDIA_URL = '/media/'  # URL for media files (uploaded files)
MEDIA_ROOT = BASE_DIR / 'media'  # Directory for uploaded files

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
]

# Set login URL for authentication
LOGIN_URL = 'login'  # URL to redirect unauthenticated users

