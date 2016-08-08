class Customer:
    """
    Creates a new customer with the users information and increments the static
    variable to change the customer's id
    """
    next_customer_id = 1

    def __init__(self, name, address, city, state, zipcode, phone):
        """
        __init__ function passes in varibles to store the information on the class
        """
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone
        self.id = Customer.next_customer_id
        Customer.next_customer_id += 1
