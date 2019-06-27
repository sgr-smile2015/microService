# -*- coding: utf-8 -*-
# Copyright © sgr
# CreateTime: 2019-06-27 15:32:00


class BaseConfig(object):
    DEBUG = False
    TESTING = False


class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProConfig(BaseConfig):
    TESTING = True

