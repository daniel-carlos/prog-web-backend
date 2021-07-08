import json
from math import prod
import models
from app import db
import random

with open("./fakeData/games.json") as json_file:
    data = json.load(json_file)
    
    for p in data:
        plat_name = p['platform']
        cat = models.Category.query.filter_by(name=plat_name).first()
        if cat == None:
            cat = models.Category(plat_name,plat_name)
            db.session.add(cat)
            db.session.commit()
            print("Categoria criada ", cat)
    

    for p in data:
        plat_name = p['platform']
        cat = models.Category.query.filter_by(name=plat_name).first()
        
        product = models.Product.query.filter_by(name=p['title']).first()
        
        if product == None:
            product = models.Product(p['title'], p['img_m'], p['img_l'], round((random.random() * 80 + 20), 2))
            db.session.add(product)
            db.session.flush()
            print("p =>", product, product.id)
            pc = models.ProductCategory(product.id, cat.id)
            db.session.add(pc)
            db.session.commit()
