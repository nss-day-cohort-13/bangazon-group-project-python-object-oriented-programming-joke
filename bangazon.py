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

    def create_new_user(self, name, address, city, state, zipcode, phone):
        new_cust = Customer(name, address, city, state, zipcode, phone)

        self.customers[new_cust.id] = new_cust

    def pay_order(self):
        if self.active_order_id == 0:
            return

        active_order = self.orders[self.active_order_id]

        active_order.is_paid = True

