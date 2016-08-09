from customer import *
from payment_option import *
from product import *
from order import *
from order_line_item import *

class Bangazon(object):

    def __init__(self):
        self.customers = dict()
        self.payment_options = dict()
        self.products = dict()
        self.orders = dict()
        self.order_line_items = dict()

        self.active_customer_id = 0
        self.active_order_id = 0

    def create_new_order(self, customer_id, payment_option_id):
        if self.active_order_id == 0:
            new_order = Order(customer_id, payment_option_id=0, is_paid=False)
            self.orders[new_order.id] = new_order
            self.active_order_id = new_order.id

    def add_product_to_order(self, order_id, product_id):
        new_line_item = OrderLineItem(order_id, product_id)
        self.order_line_items[new_line_item.id] = new_line_item
