from os import abort
from . import bp
from app import jwt
from flask import request, jsonify
from .functions import *

from flask_jwt_extended import jwt_required, get_jwt_identity, get_current_user

@bp.route("/product/list", methods=["GET"])
@jwt_required(optional=True)
def p_list():
    size = request.args.get("size", default=20, type=int)
    in_stock = request.args.get("stock", default=1, type=int)

    user = get_jwt_identity()
    admin = user != None and user['admin']
    products = list_products(size, in_stock, admin)


    return jsonify({
        "ok": True,
        "products": products
    })


@bp.route("/product/list", methods=["POST"])
@jwt_required(optional=True)
def p_list_2():
    ids = request.json['ids']
    int_ids = map(int, ids)
    products = list_products_by_ids(int_ids)
    
    return jsonify({
        "ok": True,
        "products": products
    })


@bp.route("/product/<id>", methods=["GET"])
@jwt_required(optional=True)
def product(id):
    p = Product.query.filter_by(id=int(id)).first()

    if p != None:
        return jsonify({
            "ok": True,
            "product": {
                "name": p.name,
                "price": p.price,
                "thumb": p.thumb,
                "image": p.image,
                "id": p.id
            }
        })
    else:
        return jsonify({
            "ok": False,
            "msg": "Produto não encontrado"
        })



@bp.route("/product/add-inventory", methods=["POST"])
@jwt_required()
def add_inventary_route():
    product_id = int(request.json['product'])
    amount = int(request.json['amount'])
    
    user = get_jwt_identity()
    if user['admin'] == False:
        abort(401)

    try:
        add_inventory(product_id, amount)
        return jsonify({
            "ok": True,
        })
    except Exception as e:
        return jsonify({
            "ok": True,
            "msg": e
        })

    