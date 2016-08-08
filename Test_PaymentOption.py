import unittest

from payment_option import *

class TestPaymentOption(unittest.TestCase):

    def test_create_payment_option(self):
        payment_option = PaymentOption('Amex', 123456789, 1)

        self.assertNotEqual(payment_option, 0)
        self.assertEqual(payment_option.payment_type, 'Amex')
        self.assertEqual(payment_option.account_number, 123456789)
        self.assertEqual(payment_option.customer_id, 1)

    def test_next_payment_option_id_increments(self):
        PaymentOption.next_payment_option_id = 1

        payment_option = PaymentOption('Amex', 123456789, 1)

        self.assertEqual(PaymentOption.next_payment_option_id, 2)


if __name__ == '__main__':
    unittest.main()
