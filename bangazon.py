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

        self.active_customer_id = sql.insert_new_customer(name, address, city, state, zipcode, phone)

    def create_new_payment(self, payment_type, account_number, customer_id):
        """Create New Payment

        Arguments:
        payment_type        ie. visa, mastercard
        account_number      number associated with account_number
        customer_id         id number of active customer"""

        if self.active_customer_id == 0: return

        sql.insert_new_payment_option(customer_id, payment_type, account_number)

    def pay_order(self, payment_option_id):
        """
        Pay/close an open order
        """

        if self.active_order_id == 0: return

        sql.update_complete_order(self.active_order_id, payment_option_id)
        self.active_order_id = 0

    def create_new_order(self, customer_id):
        """
        Create a new order if there is not an active order

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

        t = sql.select_popular_totals()
        return {
            'products': [{
                'name': p[0],
                'order_count': p[1],
                'customer_count': p[2],
                'revenue': p[3]}
                for p in sql.select_popular_products()],
            'totals': {
                'order_sum': t[0],
                'customer_sum': t[1],
                'revenue_sum': t[2]}
        }

    def is_active_customer(self):
        return self.active_customer_id != 0

    def is_active_order(self):
        return self.active_order_id != 0

    def get_customers(self, extra_option=None):
        """
        Get a dictionary of the customers from the database

        Returns:
            the resulting dictionary
        """

        # get the customers from the database and convert to dictionary
        tuple_list = sql.select_customers_for_menu()
        customers = {
            '{}. {}'.format(c[0], c[1]): c
            for c in tuple_list}

        # add an extra option if present
        if extra_option:
            customers.update(extra_option)

        return customers

    def get_products(self, extra_option=None):
        """
        Get a dictionary of the products from the database

        Returns:
            the resulting dictionary
        """

        # get the products from the database and convert to dictionary
        tuple_list = sql.select_products()
        products = {
            '{}. {}'.format(p[0], p[1]):p
            for p in tuple_list}

        # add an extra option if present
        if extra_option:
            products.update(extra_option)

        return products
