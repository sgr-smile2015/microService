# -*- coding: utf-8 -*-
# CreateTime: 2019-07-02 11:46:34

from base import BaseTestCase
import json
from app.module import db, User

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
        user = User(username='python', email='python@python.org')
        db.session.add(user)
        db.session.commit()

        with self.client:
            response = self.client.get('/users/{}'.format(user.id))
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual('success', data['status'])
            self.assertEqual('create_at' in data['data'])
            self.assertEqual('python', data['data']['username'])
            self.assertEqual('python@python.org', data['data']['email'])
