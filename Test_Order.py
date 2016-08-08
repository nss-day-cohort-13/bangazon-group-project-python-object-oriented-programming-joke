import unittest

from order import *

class TestOrder(unittest.TestCase):

    def test_create_order(self):
        order = Order(1, 1)

        self.assertNotEqual(order.id, 0)
        self.assertEqual(order.customer_id, 1)
        self.assertEqual(order.payment_option_id, 1)
        self.assertFalse(order.is_paid)

    def test_next_order_id_increments(self):
        Order.next_order_id = 1

        Order(1, 1)

        self.assertEqual(Order.next_order_id, 2)


if __name__ == '__main__':
    unittest.main()
