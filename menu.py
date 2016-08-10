import os
from bangazon import *
from prompt import *

class Menu:

    def __init__(self):
        self.bang = Bangazon()

    def main(self):
        while True:
            self.clear_menu()
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
        self.clear_menu()
        name = prompt('Enter Customer Name')
        address = prompt('Enter Street Name')
        city = prompt('Enter City')
        state = prompt('Enter State')
        zipcode = prompt('Enter Zip Code')
        phone = prompt('Enter Phone Number')
        self.bang.create_new_user(name, address, city, state, zipcode, phone)
        print('Your new user has been created')

    def prompt_choose_customer(self):
        self.clear_menu()
        customer_menu = {
            '{}. {}'.format(c.id, c.name):c for c in self.bang.customers.values()}
        chosen_user = show_menu('', customer_menu, '')
        self.bang.select_active_customer(chosen_user.id)
        print('You are using Bangazon as ' + chosen_user.name)

    def prompt_create_payment(self):
        self.clear_menu()
        if self.bang.active_customer_id == 0:
            print('You must choose a customer account first')
            self.prompt_choose_customer()
            return

        payment_type = prompt('Enter Payment Type (e.g. AmEx, Visa, Checking)')
        account_number = prompt('Enter Account Number')
        self.bang.create_new_payment(payment_type, account_number, self.bang.active_customer_id)

    def prompt_add_product(self):
        self.clear_menu()
        print('Add Products')
        product_menu = {
            '{}. {}'.format(p.id, p.name):p for p in self.bang.products.values()}
        chosen_product = show_menu('', product_menu, '')
        self.bang.create_new_order(self.bang.active_customer_id)
        self.bang.add_product_to_order(self.bang.active_customer_id, chosen_product.id)
        order_total = sum([self.bang.products[item.product_id].price
                for item in self.bang.order_line_items.values()
                if item.order_id == self.bang.active_order_id])
        print('You have added ' + chosen_product.name + ' to your shopping cart')
        print('Your current total is ${:.2f}.'.format(order_total))
        input('')

    def prompt_complete_order(self):
        self.clear_menu()
        if self.bang.active_order_id == 0:
            print("You must have an active order before you can checkout")
            return
        order_total = sum([self.bang.products[item.product_id].price
                for item in self.bang.order_line_items.values()
                if item.order_id == self.bang.active_order_id])
        print('Your order total is ${:.2f}.'.format(order_total))
        payment_menu = {
            '{}. {}'.format(p.id, p.payment_type):p for p in self.bang.payment_options.values()}
        chosen_payment = show_menu('Choose Your Payment Method', payment_menu, '')
        self.bang.pay_order(chosen_payment.id)
        print('Your order is complete! You paid ${:.2f} with your {}.'.format(
            order_total,
            chosen_payment.payment_type))
        input('')

    def print_popular_products(self):
        self.clear_menu()
        popular = self.bang.get_popular_products()
        products = popular['products']
        totals = popular['totals']

        # column widths
        products_col_width = 18
        orders_col_width = 11
        customers_col_width = 11
        revenue_col_width = 15
        total_width = (products_col_width +
                       orders_col_width +
                       customers_col_width +
                       revenue_col_width)

        # formating strings for table lines
        title_string = '{:<18}{:<11}{:<11}{:<15}'
        line_string = '{:<18}{:<11}{:<11}${:<14,.2f}'

        print()
        print(title_string.format('Product', 'Orders', 'Customers', 'Revenue'))
        print('*' * total_width)
        for p in products:
            name = p['name']
            # limit name string length
            name = (name if len(name) <= 17 else name[:14] + '...') + ' '
            orders = p['order_count']
            customers = p['customer_count']
            revenue = p['revenue']
            print(line_string.format(name, orders, customers, revenue))
        print('*' * total_width)
        print(line_string.format(
            'Totals:', totals['order_sum'], totals['customer_sum'], totals['revenue_sum']))

        # wait to continue
        input('\nPress ENTER to continue.')

    def clear_menu(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

if __name__ == '__main__':
    Menu().main()
