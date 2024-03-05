# app/routes/orders.py
from flask import request
from flask_restful import Resource
from models import Order, Product, Customer

class OrdersResource(Resource):
    def get(self):
        # Implement pagination, searching, filtering, sorting as needed
        # Example: orders = Order.objects().paginate(page=1, per_page=10)
        return {"orders": [order.to_json() for order in orders.items]}

    def post(self):
        data = request.get_json()
        product_id = data.get("product")
        customer_id = data.get("customer")

        product = Product.objects.get_or_404(id=product_id)
        customer = Customer.objects.get_or_404(id=customer_id)

        order = Order(product=product, customer=customer, **data).save()
        return {"order": order.to_json()}, 201

class OrderResource(Resource):
    def get(self, order_id):
        order = Order.objects.get_or_404(id=order_id)
        return {"order": order.to_json()}

    def put(self, order_id):
        data = request.get_json()
        order = Order.objects.get_or_404(id=order_id).update(**data)
        return {"order": order.to_json()}

    def delete(self, order_id):
        Order.objects.get_or_404(id=order_id).delete()
        return {"message": "Order deleted successfully."}
