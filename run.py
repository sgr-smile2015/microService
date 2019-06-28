# -*- coding: utf-8 -*-
# Copyright © sgr
# CreateTime: 2019-06-27 15:01:11

from flask_script import Manager
from app import create_app, db
import unittest
api = create_app()
manager = Manager(api)


@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("db init successful..")

@manager.command
def test():
    tests = unittest.TestLoader().discover('app/test', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
