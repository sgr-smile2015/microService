# -*- coding: utf-8 -*-
# CreateTime: 2019-06-27 20:43:27


from flask import current_app
from flask_testing import TestCase
from app import create_app

api = create_app()

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        api.config.from_object('config.DevConfig')
        return api

    def test_app_is_development(self):
        self.assertTrue(api.config['SECRET_KEY'] == 'CazzEqyQDBjm')
        self.assertTrue(api.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            api.config['SQLALCHEMY_DATABASE_URI'] ==
            'mysql+pymysql://root:admin123@users-db:3306/users_dev'
        )