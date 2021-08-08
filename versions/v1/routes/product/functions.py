from models import Product
from app import db
import math

def list_products(size=20, min_stock=0):
    if size <= 0:
        size = int('inf')

    _products = Product.query.filter(Product.stock >= min_stock).limit(size).all()
    products = []
    for p in _products:
        products.append({
            "name": p.name,
            "price": p.price,
            "thumb": p.thumb,
            "image": p.image,
            "id": p.id,
            "stock": p.stock,
            "reserved": p.reserved,
            "available": p.stock - p.reserved,
        })
    
    return products

def add_inventory(product_id, amount):
    _product = Product.query.filter_by(id = product_id).first()
    if _product != None:
        _product.stock = max(_product.stock + amount, 0)
        db.session.commit()
    
def list_products_by_ids(ids):
    _products = Product.query.filter(Product.id.in_(ids)).all()
    products = []
    for p in _products:
        products.append({
            "name": p.name,
            "price": p.price,
            "thumb": p.thumb,
            "image": p.image,
            "id": p.id,
            "stock": p.stock,
            "reserved": p.reserved,
            "available": p.stock - p.reserved,
        })
    return products