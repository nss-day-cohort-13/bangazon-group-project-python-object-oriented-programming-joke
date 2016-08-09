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

    def select_active_customer(self, customer_id):
        """
        Set active customer

        Arguments:
        customer_id   the id of the active customer
        """
        self.active_customer_id = customer_id

