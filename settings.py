# Django settings for checkit project.
import os
import djcelery

djcelery.setup_loader()

# a setting to determine whether we are running on OpenShift
ON_OPENSHIFT = False
if ON_OPENSHIFT:
    DEBUG = False
else:
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

if ON_OPENSHIFT:
    # os.environ['OPENSHIFT_MYSQL_DB_*'] variables can be used with databases created
    # with rhc cartridge add (see /README in this git repo)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'checkit',                      # Or path to database file if using sqlite3.
            'USER': 'adminWCXQBQr',                      # Not used with sqlite3.
            'PASSWORD': 'tuQuevXIpyV3',                  # Not used with sqlite3.
            'HOST': '51cc2b3e4382ec1c3d0000cf-icheckgames.rhcloud.com',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '44771',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'chat',                      # Or path to database file if using sqlite3.
            'USER': 'root',                      # Not used with sqlite3.
            'PASSWORD': 'root',                  # Not used with sqlite3.
            'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static/'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3h#32!o8zn@!h&amp;igdj7928*fple%mn%sb@0j5+c+*r2oaftwr('

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.shortcuts',
    'south',
    'djcelery',
    'icheckgames',
    'gamesearch',
    'captcha',
    'analytical',
    'fluent_comments',
    'crispy_forms',
    'django.contrib.comments',
    'chat',
)

AUTHENTICATION_BACKENDS = ('icheckgames.backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s [%(levelname)s] %(name)s(line %(lineno)d): %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        }      
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'icheckgames': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'gamesearch': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

# Celery
BROKER_URL = 'amqp://guest:guest@localhost:5672/'
CELERY_DEFAULT_RATE_LIMIT = '60/m'
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_IMPORTS = ("icheckgames.crawler", "gamesearch.indexbuilder", "gamesearch.recommender")

CELERY_QUEUES = {
    "default": {
        "exchange": "default",
        "binding_key": "default"
    },
    "game": {
        "exchange": "game",
        "binding_keys": "game",
    },
    "word": {
        "exchange": "word",
        "binding_keys": "word",
    },
    "recommender": {
        "exchange": "recommender",
        "binding_keys": "recommender",
    }
}

CELERY_DEFAULT_QUEUE = "default"
CELERY_ENABLE_UTC = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-42288126-1'

FLUENT_COMMENTS_EXCLUDE_FIELDS = ('name', 'email', 'url')
COMMENTS_APP = 'fluent_comments'

FACEBOOK_APP_ID = '414492542003134'
FACEBOOK_APP_SECRET = 'aa6f48ffab87414538a1ea12105af99d'
FACEBOOK_REDIRECT_URI = 'http://localhost:8000/facebook/'
FACEBOOK_APP_SCOPE = 'email'
FACEBOOK_AUTH_URL = 'https://www.facebook.com/dialog/oauth?client_id='+ FACEBOOK_APP_ID + '&redirect_uri=' + FACEBOOK_REDIRECT_URI + '&response_type=code&scope=' + FACEBOOK_APP_SCOPE

#Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'gamescheckers@gmail.com'
EMAIL_HOST_PASSWORD = 'gamesCheckers2013'
DEFAULT_FROM_EMAIL = 'help@icheckgames.net'