from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

from routes import routes
from models import db, Task, User

def create_app():
     # create app
     app = Flask(__name__)
     CORS(app)

     # load .env
     load_dotenv()

     # database 
     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
     app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

     # initialize extensions
     db.init_app(app)
     Migrate(app, db)
     JWTManager(app)

     app.register_blueprint(routes)

     return app

if __name__ == '__main__': 
     app = create_app()
     app.run(host="0.0.0.0", port=5000, debug=True)