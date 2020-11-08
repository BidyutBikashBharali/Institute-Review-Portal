import os
import redis
import datetime

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "sqlite123.db"))

DEBUG = False
SQLALCHEMY_DATABASE_URI = database_file
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'



SESSION_TYPE = 'redis'