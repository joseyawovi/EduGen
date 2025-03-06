from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$00ijy(q1qjcuja+43wsl3(hh3d#125^r8l43s)6=zx@w_(2tx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [
    "https://*.gitpod.io"
]
# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # user define apps
    'core',
    'allauth',  # Allauth core
    'allauth.account',  # Email/password authentication
]

SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default auth backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth backend
]

# ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Use email instead of username
ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Enforce email verification
# ACCOUNT_SIGNUP_REDIRECT_URL = '/logout'  # Redirect after signup
# ACCOUNT_LOGIN_REDIRECT_URL = '/'  # Redirect after login
# ACCOUNT_LOGOUT_REDIRECT_URL = '/'  # Redirect after logout

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'edugen.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'edugen.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

MEDIA_URL = '/media/'  
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'neoformation14@gmail.com'
EMAIL_HOST_PASSWORD = 'bdqy cpvt jmet uxvg'

# JAZZMIN

JAZZMIN_SETTINGS = {
    # Branding & Identity
    "site_title": "EduGen Admin",
    "site_header": "EduGen",
    "site_brand": "EduGen Admin",
    "welcome_sign": "Welcome to EduGen Admin Panel",
    "copyright": "EduGen - All Rights Reserved © 2025",
    
    # (Optional) Add a site logo if available
    "site_logo": "../static/assets/img/favicon.png",  

    # Sidebar and Menu Enhancements
    "order_with_respect_to": ["core", "userauths", "transactions", "addon", "blog"],

    # Allauth Integration (for managing users)
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "User Accounts", "url": "/admin/auth/user/", "permissions": ["auth.view_user"]},
        {"name": "Manage Users (Allauth)", "url": "/accounts/", "new_window": True},
        {"name": "Website", "url": "/", "new_window": True},
    ],

    # User Menu Enhancements
    "usermenu_links": [
        {"name": "Profile", "url": "/accounts/profile/", "new_window": False},
        {"name": "Logout", "url": "/accounts/logout/", "new_window": False},
    ],

    # UI Customizations for better usability
    "navigation_expanded": False,  # Keep sidebar collapsed by default
    "show_ui_builder": False,  # Hide UI Builder in Jazzmin
    "changeform_format": "collapsible",  # Use collapsible form layout

    # Theme Customization (change colors)
    "theme": "darkly",  # Available themes: cerulean, cosmo, darkly, flatly, journal, lumen, lux, materia, minty, pulse, sandstone, simplex, slate, solar, spacelab, superhero, united, yeti
}
