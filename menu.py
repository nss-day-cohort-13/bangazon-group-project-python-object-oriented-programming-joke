from bangazon import *
from prompt import *

class Menu:

    def __init__(self):
        self.bang = Bangazon()

    def main(self):
        while True:
            title = 'Welcome to Bangazon! Command Line Ordering System'

            heading = '\n'
            heading += '*' * 54 + '\n'
            heading += '*' + title.center(52, ' ') + '*' + '\n'
            heading += '*' * 54 + '\n'

            menu = {
                '1. Create a customer account': self.prompt_customer,
                '2. Choose active customer': self.prompt_choose_customer,
                '3. Create a payment option': self.prompt_create_payment,
                '4. Add product to shopping cart': self.prompt_add_product,
                '5. Complete an order': self.prompt_complete_order,
                '6. See product popularity': self.print_popular_products,
                '7. Exit Bangazon!': exit
            }

            prompt_message = 'Choose an option'

            choice = show_menu(heading, menu, prompt_message)
            choice()

    def prompt_customer(self):
        name = prompt("Enter Customer Name")
        address = prompt("Enter Street Name")
        city = prompt("Enter City")
        state = prompt("Enter State")
        zipcode = prompt("Enter Zip Code")
        phone = prompt("Enter Phone Number")
        self.bang.create_new_user(name, address, city, state, zipcode, phone)
        print('Your new user has been created')

    def prompt_choose_customer(self):
        pass

    def prompt_create_payment(self):
        pass

    def prompt_add_product(self):
        pass

    def prompt_complete_order(self):
        pass

    def print_popular_products(self):
        pass

if __name__ == '__main__':
    Menu().main()
