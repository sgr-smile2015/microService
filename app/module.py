# -*- coding: utf-8 -*-
# CreateTime: 2019-06-27 20:03:02
import os
import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    active = Column(Boolean(), default=False, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.utcnow
