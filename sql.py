import sqlite3

def run_statement(statement, *, parameters=(), fetch_amount=0):
    """
    Run a statment against the database

    Arguments:
        statement               the statement string to be executed
        parameters (optional)   a tuple of statement parameters
            defaults to empty tuple
        fetch_amount (optional) the number of records to return
                                 -1: fetch all
                                  0: none (default)
                                  1: fetch one
                                  #: fetch many

    Returns:
        the fetched result of the statement
    """

    with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()
            c.execute(statement, parameters)
            conn.commit()

            # return resulte of appropriate fetch function
            if fetch_amount:
                if fetch_amount == -1:
                    return c.fetchall()
                elif fetch_amount == 1:
                    return c.fetchone()
                else:
                    return c.fetchmany(fetch_amount)


def select_customers_for_menu():
    """
    Get list of ids and customers for menu

    Returns:
        the rows of customer ids and names
    """

    return run_statement("""
        SELECT c.customerId, c.name
        FROM Customer AS c
        """, fetch_amount=-1)

def select_customer_unpaid_orders(customer_id):
    pass

def select_customer_payment_options(customer_id):
    """
    Get list of payment options for the selected customer

    Returns:
        the rows of payment options and account numbers
    """

    return run_statement("""
        SELECT
            po.type AS 'Payment Type',
            po.number AS 'Account Number',
            po.paymentId
        FROM Payment_Option AS po
        WHERE po.customerId = ?
        """, parameters=(customer_id,), fetch_amount=-1)

def select_products():
    pass

def select_popular_products():
    pass


def insert_new_customer(name, address, city, state, zip, phone):
    pass

def insert_new_payment_option(name, account_number, customer_id):
    pass

def insert_new_order(customer_id):
    pass

def insert_new_line_item(order_id, product_id):
    pass


def update_complete_order(order_id, payment_option_id):
    pass
