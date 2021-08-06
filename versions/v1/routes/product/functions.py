from models import Product
from app import db

def list_products(size=20, min_stock=0):
    products = Product.query.filter(Product.stock >= min_stock).limit(size).all()
    return products

def add_inventory(product_id, amount):
    _product = Product.query.filter_by(id = product_id).first()
    if _product != None:
        _product.stock = max(_product.stock + amount, 0)
        db.session.commit()
    
def list_products_by_ids(ids):
    products = Product.query.filter(Product.id.in_(ids)).all()
    return products