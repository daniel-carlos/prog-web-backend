import os
from dotenv import load_dotenv
load_dotenv()

DB_CONNECTION = os.getenv("DB_CONNECTION")

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION
db = SQLAlchemy(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)