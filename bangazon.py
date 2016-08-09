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

    def create_new_order(self, customer_id, payment_option_id):
        if self.active_order_id == 0:
            new_order = Order(customer_id, payment_option_id=0, is_paid=False)
            self.orders[new_order.id] = new_order
            self.active_order_id = new_order.id

    def add_product_to_order(self, order_id, product_id):
        new_line_item = OrderLineItem(order_id, product_id)
        self.order_line_items[new_line_item.id] = new_line_item

    def select_active_customer(self, customer_id):
        """
        Set active customer

        Arguments:
        customer_id   the id of the active customer
        """
        self.active_customer_id = customer_id

    def get_popular_products(self):
        """
        Generate data for the popular products sold

        Returns:
            dictionary with totals and individual products
        """

        # collect data for each product individually
        product_counts = {}
        for item in self.order_line_items.values():
            prod = product_counts.get(item.product_id, {
                'name': self.products[item.product_id].name,
                'product_id': item.product_id,
                'count': 0,
                'unique_orders': set(),
                'unique_customers': set()})
            prod['count'] += 1
            prod['unique_orders'].add(item.order_id)
            prod['unique_customers'].add(self.orders[item.order_id].customer_id)

            product_counts[item.product_id] = prod

        # calculate revenues
        for p in product_counts.values():
            p['revenue'] = p['count'] * self.products[p['product_id']].price

        # reorganize data
        popular = {'products': []}
        for p in product_counts.values():
            popular['products'].append({
                'name': p['name'],
                'product_id': p['product_id'],
                'count': p['count'],
                'order_count': len(p['unique_orders']),
                'customer_count': len(p['unique_customers']),
                'revenue': round(p['revenue'], 2)
            })

        # calculate sums
        order_sum = sum([p['order_count'] for p in popular['products']])
        customer_sum = sum([p['customer_count'] for p in popular['products']])
        revenue_sum = sum([p['revenue'] for p in popular['products']])

        # store totals
        popular['totals'] = {
            'order_sum': order_sum,
            'customer_sum': customer_sum,
            'revenue_sum': revenue_sum
        }

        return popular
