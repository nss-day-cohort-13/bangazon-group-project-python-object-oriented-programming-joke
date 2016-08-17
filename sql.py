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
    pass

def select_products():
    pass

def select_popular_products():
    pass


def insert_new_customer(name, address, city, state, zip, phone):
    pass

def insert_new_payment_option(name, account_number, customer_id):
    pass

def insert_new_order(customer_id):
    """
    Inserts the new order into the database
    Arguments:
        customer_id     The current customer's id
    """
    run_statement("""
        INSERT INTO Order (paymentId, customerId, isPaid)
        VALUES (?,?,?)
        """), (0, customer_id, 0)

def insert_new_line_item(order_id, product_id):
    """
    Inserts the new order line item into the database
    Arguments:
        order_id    the active order id
        product_id  id of the product being added to the order
    """
    run_statement("""
        INSERT INTO Order_line_item (productId, orderId)
        VALUES (?,?)
        """, (product_id, order_id))



def update_complete_order(order_id, payment_option_id):
    pass
