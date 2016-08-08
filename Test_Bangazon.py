import unittest

from bangazon import *

class TestBangazon(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.bangazon = Bangazon()

    def test_bangazon_creation(self):
        bangazon = Bangazon()
        self.assertIsInstance(bangazon, Bangazon)
        self.assertIs(bangazon.customers, dict)
        self.assertIs(bangazon.payment_options, dict)
        self.assertIs(bangazon.orders, dict)
        self.assertIs(bangazon.order_line_items, dict)
        self.assertIs(bangazon.products, dict)
        self.assertEqual(bangazon.active_customer, None)
        self.assertEqual(bangazon.active_order, None)

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
        active_customer = self.bangazon.select_active_customer(customer_id)
        self.assertEqual(active_customer.name, 'John Doe')

    def test_create_new_order(self):
        initial_order_count = len(self.bangazon.orders)
        customer_id = 1
        payment_option_id = 0
        self.bangazon.create_new_order(customer_id, payment_option_id)
        self.assertEqual(len(self.bangazon.orders), initial_order_count + 1)

    def test_add_product_to_new_order(self):
        initial_line_item_count = len(self.bangazon.order_line_items)
        order_id = 1
        product_id = 1
        self.bangazon.add_product_to_order(1,1)
        self.assertEqual(len(self.bangazon.order_line_items), initial_line_item_count + 1)

    def test_add_product_to_existing_order(self):
        pass

    def test_complete_order(self):
        active_order = self.bangazon.orders['1']
        self.pay_order(active_order)
        self.assertTrue(active_order.is_paid)

    def test_get_popular_products(self):
        pass



if __name__ == '__main__':
    unittest.main()
