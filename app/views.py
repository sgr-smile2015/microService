# -*- coding: utf-8 -*-
# CreateTime: 2019-06-27 19:59:12

from flask import Blueprint, jsonify, request
from app.module import db, User
from sqlalchemy import exc

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
    'status': 'success',
    'message': 'pong!'
  })


@users_blueprint.route('/users', methods=['POST'])
def add_user():
    from_post = request.get_json()
    if not from_post:
        response_data = {
            'status': 'fail',
            'message': 'Invalid payload'
        }
        return jsonify(response_data), 400

    email = from_post.get('email')
    username = from_post.get('username')

    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            db.session.add(User(username=username, email=email))
            db.session.commit()
            response_data = {
                'status': 'success',
                'message': '{} was added!!'.format(email)
            }
            return jsonify(response_data), 201
        #邮件已经存在
        response_data = {
            'status': 'fail',
            'message': 'Sorry email already exists'
        }
        return jsonify(response_data), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        response_data = {
            'status': 'fail',
            'message': 'Invalid payload'
        }
        return jsonify(response_data), 400


@users_blueprint.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    response_data = {
        'status': 'fail',
        'message': 'User not exists'
    }
    code = 404
    try:
        user = User.query.filter_by(id=int(user_id)).first()
        if user:
            response_data = {
                'status': 'success',
                'data': {
                    'username': user.username,
                    'email': user.email,
                    'created_at': user.created_at
                }
            }
            code = 200
    except ValueError:
        response_data = {
            'status': 'fail',
            'message': 'Param id error'
        }
        code = 400
    finally:
        return jsonify(response_data), code

@users_blueprint.route('/users', methods=['get'])
def get_all_users():
    users = User.query.all()
    users_list = []
    for user in users:
        user_obj = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at
        }
        users_list.append(user_obj)
    
    response_data = {
        'status': 'success',
        'data': {
            'users': users_list
        }
    }
    code = 200

    return jsonify(response_data), code