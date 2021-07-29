from .functions import *
from . import bp
from flask import request, jsonify

@bp.route("/order/create", methods=["POST"])
def route_create_order():
    data = request.json
    user_id = int(data['user_id'])
    cart = data['cart']

    create = create_order(user_id, cart)

    return "Example of route."

@bp.route("order/list", methods=["POST"])
def route_list_orders():
    data = request.json
    user_id = int(data['user_id'])
    status = data['status']

    orders = list_user_orders(user_id, status="open")

    return jsonify({
        "ok": True,
        "orders": orders
    })