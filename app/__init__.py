# -*- coding: utf-8 -*-
# CreateTime: 2019-06-27 15:04:49


from flask import Flask, jsonify

api = Flask(__name__)
api.config.from_object = ('config.DevConfig')


@api.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify({
    'status': 'success',
    'message': 'pong!'
  })
