from app.app import mongo
from bson.objectid import ObjectId

class UserService:
    def get_all_users():
        users = mongo.db.users.find()
        return [user for user in users]

    def get_user(user_id):
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user:
            return user
        else:
            return None
    
    def create_user(username, password):
        if username and password:
            mongo.db.users.insert_one({'username': username, 'password': password})
            return {
                'username': username,
                'password': password
            }
        else:
            return None
    
    def update_user(user_id, user_data):
        result = mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': user_data})
        if result.modified_count == 1:
            return True
        else:
            return False
        
    def delete_user(user_id):
        result = mongo.db.users.delete_one({'_id': ObjectId(user_id)})
        if result.deleted_count == 1:
            return True
        else:
            return False