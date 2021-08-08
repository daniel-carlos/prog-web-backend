from . import bp
from flask import request, jsonify
from .functions import *

@bp.route("/product/list", methods=["GET"])
def p_list():
    size = request.args.get("size", default=20, type=int)
    in_stock = request.args.get("stock", default=1, type=int)

    products = list_products(size, in_stock)

    return jsonify({
        "ok": True,
        "products": products
    })


@bp.route("/product/list", methods=["POST"])
def p_list_2():
    ids = request.json['ids']
    int_ids = map(int, ids)
    products = list_products_by_ids(int_ids)
    
    return jsonify({
        "ok": True,
        "products": products
    })


@bp.route("/product/<id>", methods=["GET"])
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
def add_inventary_route():
    product_id = int(request.json['product'])
    amount = int(request.json['amount'])
    
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

    