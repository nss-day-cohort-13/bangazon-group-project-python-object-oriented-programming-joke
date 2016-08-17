import sql

class Bangazon(object):
    """
    Contain the logic for all functionality accessible through the user interface, including
    creating a new user, paying an order, creating a new order, adding a product to an order,
    selecting an active customer, creating a new payment, and getting popular products.
    """

    def __init__(self):
        """
        Initialize active_customer_id and active_order_id to 0
        """

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

        sql.create_new_user(name, address, city, state, zipcode, phone)

    def create_new_payment(self, payment_type, account_number, customer_id):
        """Create New Payment

        Arguments:
        payment_type        ie. visa, mastercard
        account_number      number associated with account_number
        customer_id         id number of active customer"""

        if self.active_customer_id == 0: return

        sql.insert_new_payment_option(payment_type, account_number, customer_id)

    def pay_order(self, payment_option_id):
        """
        Pay/close an open order
        """

        if self.active_order_id == 0: return

        sql.update_complete_order(self.active_order_id, payment_option_id)
        self.active_order_id = 0

    def create_new_order(self, customer_id):
        """
        Create a new order, add it to orders dictionary

        Arguments:
            customer_id         the id of the active customer
            payment_option_id   the id of the selected payment option
        """

        if self.active_order_id == 0:
            self.active_order_id = sql.insert_new_order(customer_id)

    def add_product_to_order(self, order_id, product_id):
        """
        Add selected product to an order

        Arguments:
            order_id     the id of the current order
            product_id   the id of the selected product
        """

        sql.insert_new_line_item(order_id, product_id)

    def select_active_customer(self, customer_id):
        """
        Set active customer and active order if exists for customer

        Arguments:
            customer_id   the id of the active customer
        """

        self.active_customer_id = customer_id

        # set active order if unfinished order exists
        active_customer_orders = sql.select_customer_unpaid_orders(customer_id)
        self.active_order_id = (active_customer_orders[0]
                                if active_customer_orders
                                else 0)

    def get_popular_products(self):
        """
        Generate data for the popular products sold

        Returns:
            dictionary with totals and individual products
        """

        return {
            # name, product_id, order_count, customer_count, revenue
            'products': sql.select_popular_products(),
            # order_sum, customer_sum, revenue_sum
            'totals': sql.select_popular_totals()
        }
