# -*- coding: utf-8 -*-
# Copyright © sgr
# CreateTime: 2019-06-27 15:32:00
import os

# APP_ENV = os.environ.get('APP_ENV')
APP_ENV = 'dev'

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'CazzEqyQDBjm'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.7.25:3307/users_dev'


class TestConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123@users-db:3306/users_test'


class ProdConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123@users-db:3306/users_prod'


configs = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}
