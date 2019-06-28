# -*- coding: utf-8 -*-
# CreateTime: 2019-06-27 20:38:30

from flask_testing import TestCase
from app import create_app, db


class BaseTestCase(TestCase):
    
    def create_app(self):
        create_app.config.from_object('config.DevConfig')
        return create_app


    def setUp(self):
        db.create_all()
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
