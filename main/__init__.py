import os


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session


from config import app_config


db = SQLAlchemy()
sess = Session()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    if config_name != None:
        app.config.from_object(app_config[config_name])
    else:
        app.config.from_pyfile('config.py')
    
    
    register_blueprints(app)
    initialize_extensions(app)

    with app.app_context():
        db.create_all()
    
    return app



def initialize_extensions(app):

    db.init_app(app)
    sess.init_app(app)
    
    



def register_blueprints(app):

   
    from .review import review_bp as review_blueprint
    from .institute import institute_bp as institute_blueprint
    from .wall import wall_bp as wall_blueprint
 


  
    app.register_blueprint(review_blueprint)
    app.register_blueprint(institute_blueprint)
    app.register_blueprint(wall_blueprint)


