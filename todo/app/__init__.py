from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# create database globally
db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config['secret_key']='mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.__init__(app)

    from app.routes.auth import auth_bp
    from app.routes.auth import task_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    return app