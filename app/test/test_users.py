# -*- coding: utf-8 -*-
# CreateTime: 2019-07-02 11:46:34

from base import BaseTestCase
import json
from app.module import db, User


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


class TestUsersService(BaseTestCase):
    
    def test_users(self):
        "/ping 服务"
        response = self.client.get('/ping')

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', data['message'])
        self.assertIn('success', data['status'])
    
    def test_add_users(self):
        "添加用户"
        with self.client:
            response = self.client.post(
                '/users', 
                data=json.dumps(dict(username='test_python', email='test@python.org')), 
                content_type='application/json')
        
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('test@python.org', data['message'])
            self.assertEqual('success', data['status'])
    
    def test_add_user_invalid_json(self):
        "user,email为空"
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict()),
                content_type='application/json')

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertEqual('fail', data['status'])
    
    def test_add_user_invalid_json_keys(self):
        "user,email参数错误"
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(email='test@python.org')),
                content_type='application/json'
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertEqual('fail', data['status'])

        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(email='test_python')),
                content_type='application/json'
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertEqual('fail', data['status'])
    
    def test_get_user(self):
        "获取单个用户信息"
        user = add_user('python', 'python@python.org')
        with self.client:
            response = self.client.get('/users/{}'.format(user.id))
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual('success', data['status'])
            self.assertIn('created_at', data['data'])
            self.assertEqual('python', data['data']['username'])
            self.assertEqual('python@python.org', data['data']['email'])
    
    def test_get_user_no_id(self):
        "获取用户信息,用户id必须为int类型"
        with self.client:
            response = self.client.get('/users/xxxx')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Param id error', data['message'])
            self.assertEqual('fail', data['status'])

    def test_get_user_incorrect_id(self):
        "获取用户信息,用户id不存在"
        with self.client:
            response = self.client.get('/users/-1')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User not exists', data['message'])
            self.assertEqual('fail', data['status'])

    def test_all_users(self):
        "获取所有用户信息"
        add_user('lucy', 'lucy@163.com')
        add_user('lilei', 'lilei@163.com')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual('success', data['status'])
            self.assertEqual(2, len(data['data']['users']))