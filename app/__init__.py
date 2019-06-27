# -*- coding: utf-8 -*-
# CreateTime: 2019-06-27 15:04:49

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
  api = Flask(__name__)
  api_settings = os.getenv('APP_SETTING')
  api.config.from_object(api_settings)

  db.init_app(api)
  from .views import users_blueprint
  api.register_blueprint(users_blueprint)
  return api