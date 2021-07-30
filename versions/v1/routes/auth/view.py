from . import bp

from flask import jsonify, request
from .functions import *


@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    _username = data['username']
    _password = data['password']

    user = login_with_credentials(_username, _password)
    if user['code'] != 0:
        return jsonify({
            "ok": False,
            "code": user['code'],
        })

    token = generate_token(user['name'], user['admin'], user['id'])
    return jsonify({
        "ok": True,
        "msg": "Successfully logged in.",
        "user": {
                "id": user['id'],
                "username": user['name'],
                "email": user['email'],
                "admin": user['admin'],
            },
        "token": token
    })


@bp.route("/create_user", methods=["POST"])
def create_user_route():
    data = request.json
    _username = data['username']
    _password = data['password']
    _email = data['email']

    if not password_check(_password):
        return jsonify({
            "ok": False,
            "code": 1 # password inválido
        })
    
    if not is_username_available(_username):
        return jsonify({
            "ok": False,
            "code": 2 # username já existe
        })
    
    # if not email_check(_email):
    #     return jsonify({
    #         "ok": False,
    #         "code": 3 # email inválido
    #     })
    
    try:
        user = create_user(_username, _password, _email)
        return jsonify({
            "ok": True,
            "user_id": user.id 
        })
    except Exception as e:
        print(e)
        return jsonify({
            "ok": False,
            "code": 0,
            "msg": e
        })