import os
from . import bp
from app import jwt
import app
from flask import request, jsonify, url_for, send_file, render_template, render_template_string

from .functions import *

from flask_jwt_extended import jwt_required, get_jwt_identity, get_current_user
import uuid


@bp.route("/image/upload", methods=["POST"])
@jwt_required(optional=False)
def upload_image():
    file = request.files['image']

    fname = get_unique_name()
    path = os.path.join(app.UPLOAD_FOLDER, f"{fname}.png")
    
    file.save(path)
    
    return ({
        "file_name": fname,
        "ok": True,
    })

@bp.route("/image/<name>", methods=["GET"])
def get_image(name):
    url = url_for("static", filename=f"uploads/{name}.png")
    HOST = os.getenv("HTTP_HOST")
    PORT = os.getenv("HTTP_PORT")
    return f"http://{HOST}:{PORT}{url}"