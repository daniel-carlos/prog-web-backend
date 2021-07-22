from .functions import *
from . import bp
from flask import request, jsonify

@bp.route("/order/create", methods=["POST"])
def route_name():
    data = request.json
    user_id = int(data['user_id'])
    cart = data['cart']

    create = create_order(user_id, cart)

    return "Example of route."