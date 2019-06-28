# -*- coding: utf-8 -*-
# CreateTime: 2019-06-27 15:04:49

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import configs, APP_ENV

db = SQLAlchemy()


def create_app():
  api = Flask(__name__)
  api_settings = configs[APP_ENV]
  api.config.from_object(api_settings)
  import sys
  print("[----]", api.config, sys.stderr)

  db.init_app(api)
  from .views import users_blueprint
  api.register_blueprint(users_blueprint)
  return api