# app/app.py
import app, logger
import products, customers, orders

'''import app, api, logger
from routes import products, customers, orders'''

'''from . import app, api, logger
from .routes import products, customers, orders'''

app.add_resource(products.ProductsResource, '/products')
app.add_resource(products.ProductResource, '/products/<string:product_id>')
app.add_resource(customers.CustomersResource, '/customers')
app.add_resource(customers.CustomerResource, '/customers/<string:customer_id>')
app.add_resource(orders.OrdersResource, '/orders')
app.add_resource(orders.OrderResource, '/orders/<string:order_id>')


'''api.add_resource(products.ProductsResource, '/products')
api.add_resource(products.ProductResource, '/products/<string:product_id>')
api.add_resource(customers.CustomersResource, '/customers')
api.add_resource(customers.CustomerResource, '/customers/<string:customer_id>')
api.add_resource(orders.OrdersResource, '/orders')
api.add_resource(orders.OrderResource, '/orders/<string:order_id>')
'''
if __name__ == '__main__':
    logger.info("Starting the eCommerce API...")
    app.run(debug=True)
