# app/models.py
from flask_mongoengine import MongoEngine

db = MongoEngine()

class Product(db.Document):
    name = db.StringField(required=True)
    price = db.FloatField(required=True)

class Customer(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True)

class Order(db.Document):
    product = db.ReferenceField(Product, required=True)
    customer = db.ReferenceField(Customer, required=True)
    quantity = db.IntField(required=True)
