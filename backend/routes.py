from flask import Blueprint

# create a blueprint for routes
routes = Blueprint('routes', __name__)


@routes.route('/')
def home(): 
    return {"mesasge": "Flask API is running!"}
