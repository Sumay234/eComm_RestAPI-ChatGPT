# app/routes/products.py
from flask import request
from flask_restful import Resource
from flask_mongoengine import Pagination
from models import Product
from logger import logging

class ProductsResource(Resource):
    def get(self):
        try:
            # Implement pagination, searching, filtering, sorting as needed
            # Example: products = Product.objects().paginate(page=1, per_page=10)
            return {"products": [product.to_json() for product in products.items]}
        except Exception as e:
            logging.error(f"Error in ProductsResource - GET: {str(e)}")
            return {"message": "Internal Server Error"}, 500

    def post(self):
        try:
            data = request.get_json()
            product = Product(**data).save()
            return {"product": product.to_json()}, 201
        except Exception as e:
            logging.error(f"Error in ProductsResource - POST: {str(e)}")
            return {"message": "Internal Server Error"}, 500

# Similar structures for customers and orders routes
