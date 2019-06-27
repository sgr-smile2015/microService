# -*- coding: utf-8 -*-
# Copyright © sgr
# CreateTime: 2019-06-27 15:01:11

from flask_script import Manager
from app import api

manager = Manager(api)

if __name__ == '__main__':
    manager.run()
