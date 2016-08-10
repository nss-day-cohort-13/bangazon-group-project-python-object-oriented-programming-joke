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
        name = prompt('Enter Customer Name')
        address = prompt('Enter Street Name')
        city = prompt('Enter City')
        state = prompt('Enter State')
        zipcode = prompt('Enter Zip Code')
        phone = prompt('Enter Phone Number')
        self.bang.create_new_user(name, address, city, state, zipcode, phone)
        print('Your new user has been created')

    def prompt_choose_customer(self):
        customer_menu = {
            '{}. {}'.format(c.id, c.name):c for c in self.bang.customers.values()}
        chosen_user = show_menu('', customer_menu, '')
        self.bang.select_active_customer(chosen_user.id)
        print('You are using Bangazon as ' + chosen_user.name)

    def prompt_create_payment(self):
        if self.bang.active_customer_id == 0:
            print('You must choose a customer account first')
            self.prompt_choose_customer()
            return

        payment_type = prompt('Enter Payment Type (e.g. AmEx, Visa, Checking)')
        account_number = prompt('Enter Account Number')
        self.bang.create_new_payment(payment_type, account_number, self.bang.active_customer_id)

    def prompt_add_product(self):
        print('Add Products')
        product_menu = {
            '{}. {}'.format(p.id, p.name):p for p in self.bang.products.values()}
        chosen_product = show_menu('', product_menu, '')
        self.bang.create_new_order(self.bang.active_customer_id)
        self.bang.add_product_to_order(self.bang.active_customer_id, chosen_product.id)
        print('You have added ' + chosen_product.name + ' to your shopping cart')

    def prompt_complete_order(self):
        if self.bang.active_order_id == 0:
            print("You must have an active order before you can checkout")
            return

        payment_menu = {
            '{}. {}'.format(p.id, p.payment_type):p for p in self.bang.payment_options.values()}
        chosen_payment = show_menu('Choose Your Payment Method', payment_menu, '')
        self.bang.pay_order(chosen_payment.id)
        print('Your order is complete! You paid ${:.2f} with your {}.'.format(
            sum([self.bang.products[item.product_id].price
                for item in self.bang.order_line_items.values()
                if item.order_id == self.bang.active_order_id]),
            chosen_payment.payment_type))
        input("")

    def print_popular_products(self):
        print('Print Popular Products')

if __name__ == '__main__':
    Menu().main()
