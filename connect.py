from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here' 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/assignment' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
  
    db.init_app(app) 
    
    return app