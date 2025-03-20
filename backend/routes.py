from flask import Blueprint, request, jsonify
from models import db, User, Task

# create a blueprint for routes
routes = Blueprint('routes', __name__)

# Home
@routes.route('/')
def home(): 
    return {"mesasge": "Flask API is running!"}



### ---- USER ROUTES ---- ###

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

# Create a user
@routes.route('/users', methods=['POST'])
def create_user(): 
    data = request.get_json()
    if not data or "username" not in data or "password" not in data: 
        return jsonify({"error": "Missing username or password"}), 400
    
    new_user = User(username=data["username"], password=data["password"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully", "user_id": new_user.id}), 201

# Update a user
@routes.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if not user: 
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    if "username" in data: 
        user.username = data["username"]
        # TODO: check if username is unique
        # if not unique, return error
    if "password" in data: 
        user.password = data["password"]
    
    db.session.commit()
    return jsonify({"message": "User updated", "id": user.id})

# Delete a user
@routes.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id): 
    user = User.query.get(id)
    if not user: 
        return jsonify({"error": "User not found"}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})



### ---- TASK ROUTES ---- ###
