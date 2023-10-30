import os.path
from pathlib import Path

OLD_PASSWORD_FIELD_ENABLED = True

REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER':
        'account.custom_views.CustomPasswordResetSerializer',
}

ACCOUNT_ADAPTER = 'account.custom_views.CustomAccountAdapter'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%wxy(+1&*(&kvrr0kq)-7milozi_%b3mm!hy952dmltq44ow02'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'surveybuilder.apps.SurveybuilderConfig',
    'surveytaker.apps.SurveyTakerConfig',
    'crontab',
    'django_apscheduler',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_nose',
    'drf_yasg2'
]

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=account,survey,surveybuilder,surveytaker',
]

MIDDLEWARE = [
    'django_core.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': ['templates', 'dist'],
        'DIRS': [os.path.join(BASE_DIR,'templates'), 'dist'],
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

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/static")]

WSGI_APPLICATION = 'django_core.wsgi.application'

# DATABASES = {
#     'default': {
# 		    'ENGINE': 'django.db.backends.postgresql',
# 				'NAME': 'cp13',
# 				'USER': 'postgres',
# 				'PASSWORD': '^bk!FH##W%4ax!FF',
# 		    'HOST': 'cp13dev.piran.xyz',
#         'PORT': '5432',
#     }
# }

# Group One Testing Server
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'cs63',
#         'USER': 'postgres',
#         'PASSWORD': 'cs63-1-db',
#         'HOST': '140.238.197.173',
#         'PORT': '5432',
#     }
# }

# group cs74-1 cloud database from digitalocean
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'defaultdb',
        'USER': 'doadmin',
        'PASSWORD': 'AVNS_MBtr0wHW5PKuFDtGNWq',
        'HOST': 'db-postgresql-syd1-21565-do-user-13667376-0.b.db.ondigitalocean.com',
        'PORT': '25060',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

APPEND_SLASH = False

SITE_ID = 1
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'smtp.qiye.aliyun.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = 'cs74-1@mineserver.top'
EMAIL_HOST_PASSWORD = 'CS74-1-mail'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True