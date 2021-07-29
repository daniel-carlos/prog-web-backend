from ..product.functions import list_products_by_ids
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

def list_user_orders(user_id, status="all"):
    user = Client.query.filter_by(id=user_id).first()

    if user == None:
        return False

    result = Order.query.with_entities(
            Order.id, 
            Order.created_date, 
            Order.status,
        ).filter_by(
            client_id=user_id
        ).all()

    order_list = []
    for order in result:

        order_list.append({
            "order_id": order.id,
            "created_date": order.created_date,
            "status": order.status,
        })

    return order_list