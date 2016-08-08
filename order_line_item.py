class OrderLineItem(object):

    next_line_item_id = 1

    def __init__(self, order_id, product_id):
        self.id = OrderLineItem.next_line_item_id
        self.order_id = order_id
        self.product_id = product_id
        OrderLineItem.next_line_item_id += 1
