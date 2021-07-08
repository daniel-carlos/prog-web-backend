from ... import version_name
from flask import Blueprint
from app import app

view_name = "auth"
bp = Blueprint(view_name, __name__, url_prefix="/"+version_name)
from . import view
app.register_blueprint(bp)