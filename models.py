from app import db
from datetime import datetime

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    adminname = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"Administrador {self.adminname}"

class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"Usuário {self.username}"

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    thumb = db.Column(db.String, unique=True, nullable=False)
    image = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, thumb, image, price):
        self.name = name
        self.thumb = thumb
        self.image = image
        self.price = price

    def __repr__(self):
        return f"Produto {self.name} (R$ {round(self.price,2)})"

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    icon = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name, icon):
        self.name = name
        self.icon = icon
    
    def __repr__(self):
        return f"Categoria: {self.name}"
  
class ProductCategory(db.Model):
    __tablename__ = 'product_category'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)

    def __init__(self, product_id, category_id):
        self.product_id = product_id
        self.category_id = category_id
class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(10), default="open")

    def __init__(self, client_id):
        self.client_id = client_id

class ProductOrder(db.Model):
    __tablename__ = 'product_order'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey(Order.id), nullable=False)
    amount = db.Column(db.Integer, default=1)

    def __init__(self, product_id, order_id, amount):
        self.product_id = product_id
        self.order_id = order_id
        self.amount = amount

class ProductInventory(db.Model):
    __tablename__ = 'product_inventory'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    amount = db.Column(db.Integer, default=1)

    def __init__(self, product_id, amount):
        self.product_id = product_id
        self.amount = amount

class Evaluation(db.Model):
    __tablename__ = 'eval'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    comment = db.Column(db.String(240), nullable=True)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, client_id, product_id, comment, rating):
        self.client_id = client_id
        self.product_id = product_id
        self.comment = comment
        self.rating = rating