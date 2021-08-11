from models import Product
from app import db
from flask_jwt_extended import get_jwt_identity,verify_jwt_in_request

def list_products(size=20, min_stock=0, admin=False):
    if size <= 0:
        size = int('inf')

    _products = Product.query.filter(Product.stock >= min_stock).limit(size).all()
    products = []

    for p in _products:
        if admin:
            products.append({
                "name": p.name,
                "price": p.price,
                "thumb": p.thumb,
                "image": p.image,
                "id": p.id,
                "stock": p.stock,
                "reserved": p.reserved,
                "shipment": p.shipment,
                "total": p.total,
                "available": p.stock - p.reserved,
            })
        else:
            products.append({
                "name": p.name,
                "price": p.price,
                "thumb": p.thumb,
                "image": p.image,
                "id": p.id,
                "available": p.stock - p.reserved,
            })
    
    return products

def add_inventory(product_id, amount):
    _product = Product.query.filter_by(id = product_id).first()
    if _product != None:
        _product.stock = max(_product.stock + amount, 0)
        db.session.commit()
    
def list_products_by_ids(ids, admin=False):
    _products = Product.query.filter(Product.id.in_(ids)).all()
    products = []
    for p in _products:
        if admin:
            products.append({
                "name": p.name,
                "price": p.price,
                "thumb": p.thumb,
                "image": p.image,
                "id": p.id,
                "stock": p.stock,
                "reserved": p.reserved,
                "shipment": p.shipment,
                "total": p.total,
                "limit": p.limit,
                "available": p.stock - p.reserved,
            })
        else:
            products.append({
                "name": p.name,
                "price": p.price,
                "thumb": p.thumb,
                "image": p.image,
                "id": p.id,
                "available": p.stock - p.reserved,
                "limit": p.limit,
            })
    return products