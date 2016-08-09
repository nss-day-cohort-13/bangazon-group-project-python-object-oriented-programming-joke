from easy_io import *
from customer import *
from payment_option import *
from product import *
from order import *
from order_line_item import *

class Bangazon(object):
    """
    Contain the logic for all functionality accessible through the user interface, including
    creating a new user, paying an order, creating a new order, adding a product to an order,
    selecting an active customer, creating a new payment, and getting popular products.

    Static properties:
        customers_filename          file storing all customer data
        payment_options_filename    file storing all payment options data
        products_filename           file storing all product data
        orders_filename             file storing all order data
        line_items_filename         file storing all line item data
    """

    customers_filename = 'customers.dat'
    payment_options_filename = 'payment_options.dat'
    products_filename = 'products.dat'
    orders_filename = 'orders.dat'
    line_items_filename = 'line_items.dat'

    def __init__(self):
        """
        Initialize bangazon, deserialize data files for customers, payment options, products, orders, and line items


        """

        self.customers = deserialize(Bangazon.customers_filename, dict())
        self.payment_options = deserialize(Bangazon.payment_options_filename, dict())
        self.products = deserialize(Bangazon.products_filename, dict())
        self.orders = deserialize(Bangazon.orders_filename, dict())
        self.order_line_items = deserialize(Bangazon.line_items_filename, dict())

        self.active_customer_id = 0
        self.active_order_id = 0

    def create_new_user(self, name, address, city, state, zipcode, phone):
        """
        Add a new customer to the customers dictionary

        Arguments:
            name        new customer's name
            address     new customer's street address
            city        new customer's city
            state       new customer's state
            zipcode     new customer's zip code
            phone       new customer's phone number
        """

        new_cust = Customer(name, address, city, state, zipcode, phone)
        self.customers[new_cust.id] = new_cust
        serialize(self.customers, Bangazon.customers_filename)

    def create_new_payment(self, payment_type, account_number, customer_id):
        """Create New Payment

        Arguments:
        payment_type        ie. visa, mastercard
        account_number      number associated with account_number
        customer_id         id number of active customer"""

        if self.active_customer_id == 0:
            return
        new_payment = PaymentOption(payment_type, account_number, customer_id)
        self.payment_options[new_payment.id] = new_payment
        serialize(self.payment_options, Bangazon.payment_options_filename)

    def pay_order(self, payment_option_id):
        """
        Pay/close an open order

        """

        if self.active_order_id == 0:
            return

        active_order = self.orders[self.active_order_id]
        active_order.payment_option_id = payment_option_id
        active_order.is_paid = True
        serialize(self.orders, Bangazon.orders_filename)

    def create_new_order(self, customer_id):
        """
        Create a new order, add it to orders dictionary

        Arguments:
            customer_id         the id of the active customer
            payment_option_id   the id of the selected payment option
        """

        if self.active_order_id == 0:
            new_order = Order(customer_id, payment_option_id=0, is_paid=False)
            self.orders[new_order.id] = new_order
            self.active_order_id = new_order.id
            serialize(self.orders, Bangazon.orders_filename)

    def add_product_to_order(self, order_id, product_id):
        """
        Add selected product to an order

        Arguments:
            order_id     the id of the current order
            product_id   the id of the selected product
        """

        new_line_item = OrderLineItem(order_id, product_id)
        self.order_line_items[new_line_item.id] = new_line_item
        serialize(self.order_line_items, Bangazon.line_items_filename)

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
        popular = {'products': []}
        for prod in self.products.values():
            popular['products'].append({
                'name': prod.name,
                'product_id': prod.id,
                'count': len([
                    li.order_id for li in self.order_line_items.values()
                    if li.product_id == prod.id]),
                'order_count': len({
                    li.order_id for li in self.order_line_items.values()
                    if li.product_id == prod.id}),
                'customer_count': len({
                    self.orders[li.order_id].customer_id for li in self.order_line_items.values()
                    if li.product_id == prod.id}),
                'revenue': sum([
                    prod.price for li in self.order_line_items.values()
                    if li.product_id == prod.id])
            })

        # store totalsuu
        popular['totals'] = {
            'order_sum': sum([p['order_count'] for p in popular['products']]),
            'customer_sum': sum([p['customer_count'] for p in popular['products']]),
            'revenue_sum': sum([p['revenue'] for p in popular['products']])
        }

        return popular
