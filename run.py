# -*- coding: utf-8 -*-
# Copyright © sgr
# CreateTime: 2019-06-27 15:01:11

from flask_script import Manager
from app import api,db

manager = Manager(api)


@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    manager.run()
