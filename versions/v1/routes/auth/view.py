from . import bp

from flask import jsonify, request
import json
from .functions import *
import jwt

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    _username = data['username']
    _password = data['password']
    user = login_with_credentials(_username, _password)
    if user != None:
        token = jwt.encode({"name": user['name'], "admin": user['admin'], "user_id": user['id']}, "SECRET", algorithm="HS256")
        return jsonify({
            "ok": True,
            "msg": "Successfully logged in.",
            "user_id": user['id'],
            "token": token
        })
    else:
        return jsonify({
            "ok": False,
            "msg": "Invalid credentials"
        })