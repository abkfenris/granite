import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY',
        'it7cF8RRo,sJMFcDna]wheyLLc2K>[7{ifRn,epLn^pXe/nx^AZbXpxePTWaT=fU')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAPBOX_MAP_ID = os.environ.get('MAPBOX_MAP_ID')
    MAPBOX_ACCESS_TOKEN = os.environ.get('MAPBOX_ACCESS_TOKEN')


class ProdConfig(Config):
    ENV = 'prod'

    CACHE_TYPE = 'simple'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    CACHE_TYPE = 'null'
    ASSETS_DEBUG = True


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False
