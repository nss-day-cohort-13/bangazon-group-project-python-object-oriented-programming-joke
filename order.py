class Order(object):
    """
    Contain data for a single order.

    Static Property:
        next_order_id   incrementing id for next created order
    """

    next_order_id = 1

    def __init__(self, customer_id, payment_option_id=0, is_paid=False):
        """
        Store values for new order and increment next id

        Arguments:
            customer_id         the customer who creates the order
            payment_option_id   the payment option used for the order
            is_paid             has the order been paid
        """

        self.id = Order.next_order_id
        self.customer_id = customer_id
        self.payment_option_id = payment_option_id
        self.is_paid = is_paid
        Order.next_order_id += 1