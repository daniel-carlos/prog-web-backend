from models import Client, Order, Product, ProductOrder
from app import db

def create_order(user_id, cart):
    user = Client.query.filter_by(id=user_id).first()

    if user == None:
        return False

    order = Order(user_id)
    db.session.add(order)
    db.session.flush()
    
    
    for pid in cart.keys():
        amount = cart[pid]
        product = Product.query.filter_by(id=pid)
        if product == None:
            continue
        product_order = ProductOrder(pid, order.id, amount)
        db.session.add(product_order)
        db.session.flush()
    
    db.session.commit()
    
    return True