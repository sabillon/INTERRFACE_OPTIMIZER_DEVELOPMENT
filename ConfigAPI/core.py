from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt


app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app_settings = os.getenv(
    'APP_SETTINGS',
    'ConfigAPI.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

DB = SQLAlchemy(app)
DB.create_all()

from methods import test_blueprint
#from ConfigAPI.JWT.JWTmethods import JWT_blueprint
app.register_blueprint(test_blueprint)
#app.register_blueprint(JWT_blueprint)