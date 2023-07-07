from app.app import mongo
from bson.objectid import ObjectId

class PostService:
    def get_all_posts():
        posts = mongo.db.posts.find()
        return [post for post in posts]
    
    def get_post_by_id(post_id):
        post = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
        if post:
            return post
        else:
            return None
    
    def create_post(user_id, title):
        if user_id and title:
            mongo.db.posts.insert_one({'user_id': ObjectId(user_id), 'title': title})
            return {
                'user_id': user_id, 
                'title': title
            }
        else:
            return None
    
    def get_all_posts_by_user_id(user_id):
        posts = mongo.db.posts.find({'user_id': ObjectId(user_id)})
        return [post for post in posts]