from models import Product, Category, ProductCategory
from app import db
from flask_jwt_extended import get_jwt_identity,verify_jwt_in_request

def get_product(id, admin=False):
    p = Product.query.with_entities(
        Product.name,
        Product.price,
        Product.thumb,
        Product.image,
        Product.id,
        Product.description,
        Product.stock,
        Product.reserved,
        Product.shipment,
        Product.total,
        Category.name.label("cat_name"),
        Category.id.label("cat_id"),
    ).filter_by(id=int(id)).join(
        Category, Product.main_category == Category.id
    ).first()
    if p == None:
        return {
            "name": "",
            "price": 0,
            "thumb": "",
            "image": "",
            "description": "",
            "category_id": 1,
            "available": 0,
        }

    if admin:
        return {
            "name": p.name,
            "price": p.price,
            "thumb": p.thumb,
            "image": p.image,
            "description": p.description,
            "id": p.id,
            "stock": p.stock,
            "reserved": p.reserved,
            "shipment": p.shipment,
            "total": p.total,
            "category": p.cat_name,
            "category_id": p.cat_id,
            "available": p.stock - p.reserved,
        }
    else:
        return {
            "name": p.name,
            "price": p.price,
            "thumb": p.thumb,
            "image": p.image,
            "description": p.description,
            "id": p.id,
            "category": p.cat_name,
            "category_id": p.cat_id,
            "available": p.stock - p.reserved,
        }

def list_products(size=20, min_stock=0, admin=False):
    if size <= 0:
        size = int('inf')

    _products = Product.query.with_entities(
        Product.name,
        Product.price,
        Product.thumb,
        Product.image,
        Product.id,
        Product.reserved,
        Product.shipment,
        Product.total,
        Product.description,
        Product.stock,
        Category.name.label("cat_name"),
        Category.id.label("cat_id"),
    ).filter(Product.stock >= min_stock).join(
        Category, Product.main_category == Category.id
    ).limit(size).all()
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
                "category": p.cat_name,
                "category_id": p.cat_id,
                "available": p.stock - p.reserved,
            })
        else:
            products.append({
                "name": p.name,
                "price": p.price,
                "thumb": p.thumb,
                "image": p.image,
                "id": p.id,
                "category": p.cat_name,
                "category_id": p.cat_id,
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

def update_product(product):
    _product = Product.query.filter_by(id=product['id']).first()
    _product.name = product['name']
    _product.price = product['price']
    _product.thumb = product['thumb']
    _product.image = product['image']
    _product.description = product['description']
    db.session.commit()

def list_categories():
    cats = Category.query.all()
    cat_list = []
    for cat in cats:
        cat_list.append({
            "name": cat.name,
            "id": cat.id,
        })
    return cat_list