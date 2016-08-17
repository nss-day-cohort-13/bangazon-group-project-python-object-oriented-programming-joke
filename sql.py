import sqlite3

def run_statement(statement, parameters=(), fetch_amount=0):
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

def select_customers_menu():
    return run_statement("""
        SELECT c.customerId, c.name
        FROM Customer AS c
        """, -1)
