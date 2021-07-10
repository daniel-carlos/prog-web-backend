from . import bp
from flask import request, jsonify
from .functions import *

@bp.route("/product/list", methods=["GET"])
def p_list():
    size = request.args.get("size", default=20, type=int)

    products = []
    for p in list_products(size):
        products.append({
            "name": p.name,
            "price": p.price,
            "thumb": p.thumb,
            "image": p.image,
            "id": p.id
        })
    
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

@bp.route("/product/list", methods=["POST"])
def p_list_2():
    ids = request.json['ids']
    print(request.headers.get("Authorization"))
    products = []
    for p in list_products_by_ids(ids):
        products.append({
            "name": p.name,
            "price": p.price,
            "thumb": p.thumb,
            "image": p.image,
            "id": p.id
        })
    
    return jsonify({
        "ok": True,
        "products": products
    })