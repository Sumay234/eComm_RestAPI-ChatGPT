# app/routes/customers.py
from flask import request
from flask_restful import Resource
from models import Customer

class CustomersResource(Resource):
    def get(self):
        # Implement pagination, searching, filtering, sorting as needed
        # Example: customers = Customer.objects().paginate(page=1, per_page=10)
        return {"customers": [customer.to_json() for customer in customers.items]}

    def post(self):
        data = request.get_json()
        customer = Customer(**data).save()
        return {"customer": customer.to_json()}, 201

class CustomerResource(Resource):
    def get(self, customer_id):
        customer = Customer.objects.get_or_404(id=customer_id)
        return {"customer": customer.to_json()}

    def put(self, customer_id):
        data = request.get_json()
        customer = Customer.objects.get_or_404(id=customer_id).update(**data)
        return {"customer": customer.to_json()}

    def delete(self, customer_id):
        Customer.objects.get_or_404(id=customer_id).delete()
        return {"message": "Customer deleted successfully."}
