from .functions import *
from . import bp
from flask import request, jsonify, abort

from flask_jwt_extended import jwt_required, get_jwt_identity, get_current_user


@bp.route("order/list", methods=["GET", "POST"])
@jwt_required()
def route_list_orders():
    user = get_jwt_identity()
    status = request.json.get("status", "open")

    if(user['admin']):
        orders = list_user_orders_admin(status)
    else:
        orders = list_user_orders(user["id"], status)

    return jsonify({
        "ok": True,
        "orders": orders
    })


@bp.route("/order/create", methods=["POST"])
@jwt_required()
def route_create_order():
    data = request.json
    cart = data['cart']
    user = get_jwt_identity()
    
    create = create_order(user['id'], cart)
    
    return jsonify(create)


@bp.route("order/confirm", methods=["POST"])
@jwt_required()
def route_confirm_order():
    user = get_jwt_identity()
    id = request.json.get("id", None)

    if(user['admin']):
        orders = update_order(id, "confirmed")
    else:
        return jsonify({
            "ok": False,
        })
        
    return jsonify({
        "ok": True,
        "orders": orders
    })


@bp.route("order/deliver", methods=["POST"])
@jwt_required()
def route_deliver_order():
    user = get_jwt_identity()
    id = request.json.get("id", None)

    if(user['admin']):
        orders = update_order(id, "delivered")
    else:
        return jsonify({
            "ok": False,
        })
        
    return jsonify({
        "ok": True,
        "orders": orders
    })


@bp.route("order/cancel", methods=["POST"])
@jwt_required()
def route_cancel_order():
    user = get_jwt_identity()
    id = request.json.get("id", None)

    if(user['admin']):
        orders = update_order(id, "canceled")
    else:
        return jsonify({
            "ok": False,
        })
        
    return jsonify({
        "ok": True,
        "orders": orders
    })