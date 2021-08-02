from .functions import *
from . import bp
from flask import request, jsonify

from flask_jwt_extended import jwt_required, get_jwt_identity, get_current_user

@bp.route("/order/create", methods=["POST"])
@jwt_required()
def route_create_order():
    data = request.json
    cart = data['cart']

    user = get_jwt_identity()
    
    create = create_order(user['id'], cart)

    return "Example of route."

@bp.route("order/list", methods=["GET", "POST"])
@jwt_required()
def route_list_orders():
    user = get_jwt_identity()
    status = request.json.get("status", "open")

    orders = list_user_orders(user["id"], status)

    return jsonify({
        "ok": True,
        "orders": orders
    })