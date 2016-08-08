import unittest

from customer import *

class TestCustomer(unittest.TestCase):

    def test_create_customer(self):
        cust = Customer('John Doe',
                        '1 Main St',
                        'Nashville',
                        'TN',
                        '37210',
                        '123-456-7890')

        self.assertNotEqual(cust.id, 0)
        self.assertEqual(cust.name, 'John Doe')
        self.assertEqual(cust.address, '1 Main St')
        self.assertEqual(cust.city, 'Nashville')
        self.assertEqual(cust.state, 'TN')
        self.assertEqual(cust.zip, '37210')
        self.assertEqual(cust.phone, '123-4566-7890')

    def test_next_customer_id_increments(self):
        Customer.next_customer_id = 1

        Customer('John Doe',
                 '1 Main St',
                 'Nashville',
                 'TN',
                 '37210',
                 '123-456-7890')

        Customer('Jane Doe',
                 '2 Main St',
                 'Nashville',
                 'TN',
                 '37210',
                 '223-456-7890')

        self.assertEqual(Customer.next_customer_id, 3)

    def test_next_customer_id_increments(self):
        pass


if __name__ == '__main__':
    unittest.main()
