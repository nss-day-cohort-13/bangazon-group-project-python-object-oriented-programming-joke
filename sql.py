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
    """
    Get all unpaid orders for the active customer

    Returns:
        customer id and order id of any unpaid orders for that customer

    Arguments:
        customer_id     The current customer's id
    """

    return run_statement("""
        SELECT o.CustomerId, o.Orderid
        FROM `Order` o
        WHERE o.CustomerId = ?
        AND o.isPaid = 0
        """, parameters=(customer_id,), fetch_amount=1)

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
    """
    Get all Product information

    Returns:
        all rows of product ids, names, and prices
    """
    return run_statement("""
        SELECT *
        FROM Product
        """, fetch_amount=-1)

def select_popular_products():
    """
    Get table of popular products sorted by number of times ordered

    Returns:
        Table of popular products with name, number of orders, quantity ordered and total amount made
    """

    return run_statement("""
        SELECT
            p.name AS 'Products',
            COUNT(l.orderId) AS 'Orders',
            COUNT(c.customerId) AS 'Customers',
            SUM(p.price) AS 'Revenue'
        FROM Product p, Order_line_item l, `Order` o, Customer c
        WHERE p.productId = l.productId
        AND l.orderId = o.orderId
        AND o.customerId = c.customerId
        GROUP BY p.productId
        ORDER BY Orders DESC
        """, fetch_amount=-1)

def select_popular_totals():
    """
    Get summary of popular product totals

    Return:
        Row with totals for customers, orders & total amount made
    """

    return run_statement("""
        SELECT
            COUNT(l.orderId) AS 'Orders',
            COUNT(c.customerId) AS 'Customers',
            SUM(p.price) AS 'Revenue'
        FROM Product p, Order_line_item l, `Order` o, Customer c
        WHERE p.productId = l.productId
        AND l.orderId = o.orderId
        AND o.customerId = c.customerId
        """, fetch_amount=1)
    
def insert_new_customer(name, address, city, state, zipcode, phone):
    """
    Inserts new customer information into the database

    Arguments:
        name   The customer's name
        address     The customer's street address
        city    The customer's city
        state   The customer's state
        zipcode     The customer's zipcode
        phoneNumber   The customer's phone number
    """
    run_statement("""
        INSERT INTO Customer (name, address, city, state, zipcode, phoneNumber)
        VALUES (?,?,?,?,?,?)
        """, parameters=(name, address, city, state, zipcode, phone))

def insert_new_payment_option(name, account_number, customer_id):
    pass

def insert_new_order(customer_id):
    """
    Inserts the new order into the database
    Arguments:
        customer_id     The current customer's id
    """
    run_statement("""
        INSERT INTO Order (paymentId, customerId)
        VALUES (?,?,?)
        """, parameters=(0, customer_id))

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
        """, parameters=(product_id, order_id))



def update_complete_order(order_id, payment_option_id):
    run_statement("""
        UPDATE Order
        SET paymentId = ?, isPaid = 1
        WHERE orderId = ?
        """, parameters=(payment_option_id, order_id))
