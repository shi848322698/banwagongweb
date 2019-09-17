"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q5iptt22fv&$75#3t40t8yce&%m5s-fw6-a+_ehvcwz@p*82dj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'account',
    'article',
    'image',
    'sorl.thumbnail',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases



# 使用本身sqllite的配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 使用mysql的配置
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', #选择mysql引擎
#         'NAME': 'my_mysql', #数据库名
#         'USER': 'root', #用户
#         'PASSWORD': 'qwe654123', #密码
#         'HOST': 'localhost', #连接IP地址，默认本地
#         'PORT': '3306', #端口，默认3306
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


LOGIN_REDIRECT_URL = '/home/'

LOGIN_URL = '/account/login/'


# 上传github时候一定记得把授权码取消了 *************** 重要# 上传github时候一定记得把授权码取消了 *************** 重要
# 上传github时候一定记得把授权码取消了 *************** 重要# 上传github时候一定记得把授权码取消了 *************** 重要
# 上传github时候一定记得把授权码取消了 *************** 重要# 上传github时候一定记得把授权码取消了 *************** 重要
# 上传github时候一定记得把授权码取消了 *************** 重要# 上传github时候一定记得把授权码取消了 *************** 重要
# 上传github时候一定记得把授权码取消了 *************** 重要# 上传github时候一定记得把授权码取消了 *************** 重要
# 上传github时候一定记得把授权码取消了 *************** 重要# 上传github时候一定记得把授权码取消了 *************** 重要
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 25
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "wo.aitangtang@163.com"
# 上传github时候一定记得把授权码取消了 *************** 重要# 上传github时候一定记得把授权码取消了 *************** 重要
# 上传github时候一定记得把授权码取消了 *************** 重要# 上传github时候一定记得把授权码取消了 *************** 重要
# 上传github时候一定记得把授权码取消了 *************** 重要# 上传github时候一定记得把授权码取消了 *************** 重要
# 上传github时候一定记得把授权码取消了 *************** 重要# 上传github时候一定记得把授权码取消了 *************** 重要
# 上传github时候一定记得把授权码取消了 *************** 重要# 上传github时候一定记得把授权码取消了 *************** 重要
# 上传github时候一定记得把授权码取消了 *************** 重要# 上传github时候一定记得把授权码取消了 *************** 重要


# 右键发送将直接显示在控制台
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
