# -*- coding: utf-8 -*-
# CreateTime: 2019-06-27 15:04:49

import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)
api_settings = os.getenv('APP_SETTING')
api.config.from_object(api_settings)

import sys 
print(api.config, sys.stderr)

db = SQLAlchemy(api)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.utcnow

@api.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify({
    'status': 'success',
    'message': 'pong!'
  })
