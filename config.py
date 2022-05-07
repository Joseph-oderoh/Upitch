import os

from flask_sqlalchemy import SQLAlchemy

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jkblvck@localhost/upitch'
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}