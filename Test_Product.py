import unittest

from order import *

class TestProduct(unittest.TestCase):

    def test_create_product(self):
        product = Product('water', 1.25)

        self.assertNotEqual(product.id, 0)
        self.assertEqual(product.name, 'water')
        self.assertEqual(product.price, 1.25)

    def test_next_product_id_increments(self):
        Product.next_product_id = 1

        product = Product('water', 1.25)

        self.assertEqual(Product.next_product_id, 2)

    def test_next_product_id_increments(self):
        pass


if __name__ == '__main__':
    unittest.main()
