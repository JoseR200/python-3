from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId

from config import config

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flask_test'

mongo = PyMongo(app)

@app.route('/api/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    print(user)
    if user:
        response = json_util.dumps(user)
        return Response(response, mimetype='application/json')
    else:
        return not_found()

@app.route('/api/users', methods=['POST'])
def create_user():
    username= request.json['username']
    password= request.json['password']

    if username and password:
        id = mongo.db.users.insert_one(
            {'username': username, 'password': password}
        )
        response = {
            'username': username,
            'password': password
        }
        return response
    else: 
        return not_found()

@app.route('/api/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    result = mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': user_data})
    
    if result.modified_count == 1:
        return jsonify({'message': 'User Updated'})
    else: 
        return not_found()
    
@app.route('/api/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = mongo.db.users.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'User deleted'})
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Resource Not Found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()
