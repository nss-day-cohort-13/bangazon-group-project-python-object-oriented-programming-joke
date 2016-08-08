import unittest

from order import *

class TestOrderLineItem(unittest.TestCase):

    def test_create_order_line_item(self):
        line_item = OrderLineItem(1, 2)

        self.assertNotEqual(line_item.id, 0)
        self.assertEqual(line_item.order_id, 1)
        self.assertEqual(line_item.product_id, 2)

    def test_next_order_line_item_id_increments(self):
        OrderLineItem.next_line_item_id = 1

        OrderLineItem(1, 2)

        self.assertEqual(OrderLineItem.next_line_item_id, 2)

    def test_next_order_line_item_id_increments(self):
        pass


if __name__ == '__main__':
    unittest.main()
