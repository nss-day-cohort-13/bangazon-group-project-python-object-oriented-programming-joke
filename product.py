
class Product():
    """
    Contain data for a single line item.

    Static Property:
        next_product_id   incrementing id for next created product
    """

    next_product_id = 1

    def __init__(self, name, price):
        """
        Store values for new product and increment next id

        Arguments:
            name    the name of the product
            price   the price of the product
        """
        self.name = name
        self.price = price
        self.id = Product.next_product_id
        Product.next_product_id += 1
