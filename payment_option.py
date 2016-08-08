class PaymentOption(object):
    """
    Creates new payment option, storing to the payment option data file.

    Static Property:
        next_payment_option_id   incrementing id for next created payment option.
    """


    next_payment_option_id = 1

    def __init__(self, payment_type, account_number, customer_id):
        """
        Store values for new payment option and increment next id.

        Arguments:
            payment_type      the form of payment
            account_number    the account number for the payment type
            customer_id       the customer associated with the payment option

        """

        self.payment_type = payment_type
        self.account_number = account_number
        self.customer_id = customer_id
        PaymentOption.next_payment_option_id += 1

