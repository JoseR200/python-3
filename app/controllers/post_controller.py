from flask import request, jsonify, Response
from bson import json_util

from app.services.post_services import PostService

def get_posts():
    posts = PostService.get_all_posts()
    return Response(json_util.dumps(posts), mimetype='application/json')

def get_post_by_id(post_id):
    post = PostService.get_post_by_id(post_id)
    if post:
        return Response(json_util.dumps(post), mimetype='application/json')
    else:
        return not_found_post()
    
def create_post(user_id):
    title = request.json['title']

    post = PostService.create_post(user_id, title)

    if post:
        return post
    else: 
        return not_found_post()
    
def get_posts_by_user_id(user_id):
    posts = PostService.get_all_posts_by_user_id(user_id)
    return Response(json_util.dumps(posts), mimetype='application/json')
    
def not_found_post(error=None):
    response = jsonify({
        'message': 'Post Not Found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response