class Order(object):

    next_order_id = 1

    def __init__(self, customer_id, payment_option_id, is_paid=False):
        self.id = Order.next_order_id
        self.customer_id = customer_id
        self.payment_option_id = payment_option_id
        self.is_paid = is_paid
        Order.next_order_id += 1
