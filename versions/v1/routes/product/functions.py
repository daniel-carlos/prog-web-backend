from models import Product, ProductCategory, Category

def list_products(size=20):
    products = Product.query.limit(size).all()
    return products

def list_products_by_ids(ids):
    products = Product.query.filter(Product.id.in_(ids)).all()
    return products