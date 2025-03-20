from flask import Blueprint, request, jsonify
from models import db, User, Task

# create a blueprint for routes
routes = Blueprint('routes', __name__)

# Home
@routes.route('/')
def home(): 
    return {"mesasge": "Flask API is running!"}

# Get all users
@routes.route('/users', methods=['GET'])
def get_users(): 
    users = User.query.all()
    user_list = []
    for u in users: 
        user_list.append({
            "id": u.id,
            "username": u.username
        })
    return jsonify(user_list)

# Get one user
@routes.route('/users/<int:id>', methods=['GET'])
def get_user(id): 
    user = User.query.get(id)
    if not user: 
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "id": user.id,
        "username": user.username
    })