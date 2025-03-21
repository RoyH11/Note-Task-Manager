from flask import Blueprint, request, jsonify
from models import db, User, Task
from datetime import datetime, timedelta, timezone

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

# Get all tasks
@routes.route('/tasks', methods=['GET'])
def get_tasks(): 
    tasks = Task.query.all()
    task_list = []
    for t in tasks: 
        task_list.append({
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "due_date": t.due_date.isoformat(),
            "user_id": t.user_id
        })
    return jsonify(task_list)

# Get one task
@routes.route('/tasks/<int:id>', methods=['GET'])
def get_task(id): 
    task = Task.query.get(id)
    if not task: 
        return jsonify({"error": "Task not found"}), 404
    
    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "due_date": task.due_date.isoformat(), 
        "user_id": task.user_id
    })

# Create a new task
# TODO: Description should be optional
@routes.route('/tasks', methods=['POST'])
def create_task(): 
    data = request.get_json()
    if (not data) or ("title" not in data) or ("description" not in data) or ("due_date" not in data) or ("user_id" not in data): 
        return jsonify({"error": "Missing required fields"}), 400
    
    try: 
        due_date = datetime.fromisoformat(data["due_date"])
    except ValueError:
        return jsonify({"error": "Invalid due date format"}), 400

    new_task = Task(
        title=data["title"],
        description=data["description"],
        due_date=due_date,
        user_id=data["user_id"]
    )

    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created successfully", "id": new_task.id}), 201

# Update a task
@routes.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id): 
    task = Task.query.get(id)
    if not task: 
        return jsonify({"error": "Task not found"}), 404
    
    data = request.get_json()
    if "title" in data: 
        task.title = data["title"]
    if "description" in data:
        task.description = data["description"]
    if "due_date" in data:
        try: 
            task.due_date = datetime.fromisoformat(data["due_date"])
        except ValueError:
            return jsonify({"error": "Invalid due date format"}), 400
    if "user_id" in data:
        task.user_id = data["user_id"]

    db.session.commit()
    return jsonify({"message": "Task updated successfully", "id": task.id})

# Delete a task
@routes.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id): 
    task = Task.query.get(id)
    if not task: 
        return jsonify({"error": "Task not found"}), 404
    
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})