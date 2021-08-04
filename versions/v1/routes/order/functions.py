from ..product.functions import list_products_by_ids
from models import Client, Order, Product, ProductOrder
from app import db

def create_order(user_id, cart):
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
    _orders = Order.query.with_entities(
            Order.id, 
            Order.created_date, 
            Order.status,
        ).filter_by(
            client_id=user_id
        ).order_by(
            Order.created_date.desc()
        ).all()

    order_list = []
    for order in _orders:

        _products = ProductOrder.query.filter_by(
            order_id=order.id
        ).join( 
            Product, Product.id == ProductOrder.product_id
        ).with_entities(
            ProductOrder.amount,
            Product.name,
            Product.thumb,
            Product.price,
        ).all()

        products = []
        for p in _products:
            products.append({
                "name": p.name,
                "amount": p.amount,
                "thumb": p.thumb,
                "price": p.price,
            })

        order_list.append({
            "order_id": order.id,
            "created_date": order.created_date,
            "status": order.status,
            "products": products
        })


    return order_list


def list_user_orders_admin(status="all"):
    _orders = Order.query.with_entities(
            Order.id, 
            Order.created_date, 
            Order.status,
            Client.username,
        ).join(
            Client, Client.id == Order.client_id
        ).order_by(
            Order.created_date.desc()
        ).all()

    order_list = []
    for order in _orders:

        _products = ProductOrder.query.filter_by(
            order_id=order.id
        ).join( 
            Product, Product.id == ProductOrder.product_id
        ).with_entities(
            ProductOrder.amount,
            Product.name,
            Product.thumb,
            Product.price,
        ).all()

        products = []
        for p in _products:
            products.append({
                "name": p.name,
                "amount": p.amount,
                "thumb": p.thumb,
                "price": p.price, 
            })

        order_list.append({
            "order_id": order.id,
            "created_date": order.created_date,
            "status": order.status,
            "products": products,
            "username": order.username,
        })


    return order_list


def update_order(id, new_status):
    order = Order.query.filter_by(id=id).first()
    order.status = new_status
    db.session.commit();