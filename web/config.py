import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@mysql/poker'


class DevelopmentConfig(Config):
    DEBUG = True
