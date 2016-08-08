class OrderLineItem(object):
    """
    Contain data for a single line item.

    Static Property:
        next_line_item_id   incrementing id for next created line item
    """

    next_line_item_id = 1

    def __init__(self, order_id, product_id):
        """
        Store values for new line item and increment next id

        Arguments:
            order_id    the order the line item belongs to
            product_id  the product pertaining to the line item
        """

        self.id = OrderLineItem.next_line_item_id
        self.order_id = order_id
        self.product_id = product_id
        OrderLineItem.next_line_item_id += 1
