from . import bp

from flask import jsonify, request
from .functions import *

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    _username = data['username']
    _password = data['password']
    user = login_with_credentials(_username, _password)
    if user != None:
        token = generate_token(user['name'], user['admin'], user['id'])
        return jsonify({
            "ok": True,
            "msg": "Successfully logged in.",
            "user_id": user['id'],
            "admin": False,
            "token": token
        })
    else:
        return jsonify({
            "ok": False,
            "msg": "Invalid credentials"
        })