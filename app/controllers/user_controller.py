from flask import request, jsonify, Response
from bson import json_util

from app.services.user_services import UserService

def get_users():
    users = UserService.get_all_users()
    return Response(json_util.dumps(users), mimetype='application/json')

def get_user(user_id):
    user = UserService.get_user(user_id)
    if user:
        return Response(json_util.dumps(user), mimetype='application/json')
    else:
        return not_found()
    
def create_user():
    username = request.json['username']
    password = request.json['password']

    user = UserService.create_user(username, password)

    if user:
        return user
    else: 
        return not_found()

def update_user(user_id):
    user_data = request.get_json()
    result = UserService.update_user(user_id, user_data)
    
    if result:
        return jsonify({'message': 'User Updated'})
    else: 
        return not_found()

def delete_user(user_id):
    result = UserService.delete_user(user_id)

    if result:
        return jsonify({'message': 'User Deleted'})
    else:
        return not_found()
    
def not_found(error=None):
    response = jsonify({
        'message': 'User Not Found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response