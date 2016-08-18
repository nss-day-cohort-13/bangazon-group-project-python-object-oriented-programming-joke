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

            heading = ''
            heading += '\033[34m'
            heading += '*' * 54 + '\n'
            heading += '*\033[36m' + title.center(52, ' ') + '\033[34m*\n'
            heading += '*' * 54 + '\n'
            heading += '\033[37;40m'

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

        print(name + ' has been created')
        pause()

    def prompt_choose_customer(self):
        self.clear_menu()

        customer_menu = self.bang.get_customers()
        chosen_user = show_menu('User List:', customer_menu, '')
        self.bang.select_active_customer(chosen_user[0])

        print('You are using Bangazon as ' + chosen_user[1])
        pause()

    def prompt_create_payment(self):
        self.clear_menu()

        if self.bang.is_active_customer():
            pause('You must choose a customer account first')
            return

        payment_type = prompt('Enter Payment Type (e.g. AmEx, Visa, Checking)')
        account_number = prompt('Enter Account Number')
        self.bang.create_new_payment(payment_type, account_number, self.bang.active_customer_id)

        print('New Payment Option created as {} with account number {}'
            .format(payment_type, account_number))
        pause()

    def prompt_add_product(self):
        self.clear_menu()

        if self.bang.is_active_customer() == 0:
            pause('Please choose a user first.')
            return

        while True:
            self.clear_menu()
            print('Add Products')
            product_menu = {
                '{}. {}'.format(p[0], p[1]):p for p in sql.select_products()}
            product_menu['{}. Back to main menu'.format(len(product_menu) + 1)] = None
            chosen_product = show_menu('Products:', product_menu, '')

            if chosen_product is None: break

            self.bang.create_new_order(self.bang.active_customer_id)
            self.bang.add_product_to_order(self.bang.active_order_id, chosen_product[0])

            order_total = float(sql.select_order_total(self.bang.active_order_id)[0])
            print('You have added ' + chosen_product[1] + ' to your shopping cart')
            print('Your current total is ${:.2f}.'.format(order_total))
            pause('Press enter to continue adding to your cart')

    def prompt_complete_order(self):
        self.clear_menu()
        if self.bang.active_order_id == 0:
            pause('You must have an active order before you can checkout')
            return

        order_total = float(sql.select_order_total(self.bang.active_order_id)[0])
        should_continue = prompt('Your order total is ${:.2f}. Pay now? [\033[32mY\033[37m/n]'
                                    .format(order_total))

        if should_continue and should_continue.lower()[0] == 'n': return

        payment_menu = {
            '{}. {}'.format(p[2], p[0]):p
            for p in sql.select_customer_payment_options(self.bang.active_customer_id)}
        chosen_payment = show_menu('Choose Your Payment Method', payment_menu, '')
        self.bang.pay_order(chosen_payment[2])

        print('Your order is complete! You paid ${:.2f} with your {}.'.format(
            order_total,
            chosen_payment[0]))
        pause()

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
        total_string = '\033[36m{:<18}\033[37m{:<11}{:<11}${:<14,.2f}'

        print('\033[36m' + title_string.format('Product', 'Orders', 'Customers', 'Revenue'))
        print('\033[34m*\033[37m' * total_width)
        for p in products:
            name = p['name']
            # limit name string length
            name = (name if len(name) <= 17 else name[:14] + '...') + ' '
            orders = p['order_count']
            customers = p['customer_count']
            revenue = p['revenue']
            print(line_string.format(name, orders, customers, revenue))
        print('\033[34m*\033[37m' * total_width)
        print(total_string.format(
            'Totals:', totals['order_sum'], totals['customer_sum'], totals['revenue_sum']))

        # wait to continue
        pause()

    def clear_menu(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

if __name__ == '__main__':
    Menu().main()
