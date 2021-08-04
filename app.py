import os

DB_CONNECTION = os.getenv("DB_CONNECTION")

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from flask_jwt_extended import JWTManager
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 30
jwt = JWTManager(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)