import sqlite3

def run_statement(statement, parameters=None, fetch_amount=0):
    """
    Run a statment against the database

    Arguments:
        statement               the statement string to be executed
        parameters (optional)   a tuple of statement parameters
            defaults to None
        fetch_amount (optional) the number of records to return
                                 -1: fetch all
                                  0: none (default)
                                  1: fetch one
                                  #: fetch many

    Returns:
        the fetched result of the statement
    """
