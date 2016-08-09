import unittest

from bangazon import *

class TestBangazon(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.bangazon = Bangazon()

    def test_bangazon_creation(self):
        bangazon = Bangazon()
        self.assertIsInstance(bangazon, Bangazon)
        self.assertIsInstance(bangazon.customers, dict)
        self.assertIsInstance(bangazon.payment_options, dict)
        self.assertIsInstance(bangazon.orders, dict)
        self.assertIsInstance(bangazon.order_line_items, dict)
        self.assertIsInstance(bangazon.products, dict)
        self.assertEqual(bangazon.active_customer_id, 0)
        self.assertEqual(bangazon.active_order_id, 0)

    def test_create_new_customer(self):
        initial_customers = len(self.bangazon.customers)
        self.bangazon.create_new_user('John Doe',
                        '1 Main St',
                        'Nashville',
                        'TN',
                        '37210',
                        '123-456-7890')
        self.assertEqual(len(self.bangazon.customers), initial_customers + 1)

    def test_select_active_customer(self):
        customer_id = 1
        self.bangazon.select_active_customer(customer_id)
        self.assertEqual(self.bangazon.active_customer_id, customer_id)

    def test_create_new_order(self):
        bangazon = Bangazon()
        initial_order_count = len(bangazon.orders)
        customer_id = 1
        payment_option_id = 0
        bangazon.create_new_order(customer_id, payment_option_id)
        self.assertEqual(len(bangazon.orders), initial_order_count + 1)

    def test_add_product_to_order(self):
        initial_line_item_count = len(self.bangazon.order_line_items)
        order_id = 1
        product_id = 1
        self.bangazon.add_product_to_order(order_id, product_id)
        self.assertEqual(len(self.bangazon.order_line_items), initial_line_item_count + 1)

    def test_complete_order(self):
        self.bangazon.orders = {1: Order(2)}
        self.bangazon.active_order_id = 1
        active_order = self.bangazon.orders[self.bangazon.active_order_id]
        self.bangazon.pay_order()
        self.assertTrue(active_order.is_paid)

    def test_new_payment_creation(self):
        bangazon = Bangazon()
        bangazon.active_customer_id = 1
        initial_payment_count = len(bangazon.payment_options)
        customer_id = 1
        payment_type = 'Visa'
        account_number = 12345
        bangazon.create_new_payment(payment_type, account_number, customer_id)
        self.assertEqual(len(bangazon.payment_options), initial_payment_count + 1)

    def test_get_popular_products(self):
        self.maxDiff = None

        bangazon = Bangazon()
        bangazon.products = {
            1: Product('Item A', 0.50),
            2: Product('Item B', 0.75),
            3: Product('Item C', 1.10)}
        bangazon.orders = {
            1: Order(1, 1, True),
            2: Order(2, 1, True),
            3: Order(1, 1, True),
            4: Order(1, 1, True)}
        bangazon.order_line_items = {
            1: OrderLineItem(1, 1),
            2: OrderLineItem(1, 1),
            3: OrderLineItem(1, 1),
            4: OrderLineItem(1, 2),
            5: OrderLineItem(1, 2),
            6: OrderLineItem(1, 3),
            7: OrderLineItem(1, 3),
            8: OrderLineItem(1, 3),
            9: OrderLineItem(1, 3),
            10: OrderLineItem(2, 2),
            11: OrderLineItem(2, 3),
            12: OrderLineItem(3, 1),
            13: OrderLineItem(3, 2),
            14: OrderLineItem(3, 2),
            15: OrderLineItem(3, 3)}

        expected = {
            'totals': {
                'order_sum': 8,
                'customer_sum': 5,
                'revenue_sum': 12.35
            },
            'products': [
                {
                    'name': 'Item A',
                    'product_id': 1,
                    'count': 4,
                    'order_count': 2,
                    'customer_count': 1,
                    'revenue': 2.0
                },
                {
                    'name': 'Item B',
                    'product_id': 2,
                    'count': 5,
                    'order_count': 3,
                    'customer_count': 2,
                    'revenue': 3.75
                },
                {
                    'name': 'Item C',
                    'product_id': 3,
                    'count': 6,
                    'order_count': 3,
                    'customer_count': 2,
                    'revenue': 6.60
                }
            ]
        }

        result = bangazon.get_popular_products()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
