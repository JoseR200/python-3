from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flask_test'

mongo = PyMongo(app)
from app.controllers.user_controller import *
from app.controllers.post_controller import *

app.route('/api/users', methods=['GET'])(get_users)
app.route('/api/users/<user_id>', methods=['GET'])(get_user)
app.route('/api/users', methods=['POST'])(create_user)
app.route('/api/users/<user_id>', methods=['PUT'])(update_user)
app.route('/api/users/<user_id>', methods=['DELETE'])(delete_user)

app.route('/api/posts', methods=['GET'])(get_posts)
app.route('/api/post/<post_id>', methods=['GET'])(get_post_by_id)
app.route('/api/posts/<user_id>', methods=['POST'])(create_post)
app.route('/api/posts/<user_id>', methods=['GET'])(get_posts_by_user_id)

app.errorhandler(404)(not_found)
app.errorhandler(404)(not_found_post)