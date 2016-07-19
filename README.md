# group-project-command-line-apps


# Bangazon!
## The Command Line Ordering System

In this exercise, you will be allowing a user to interact with a basic product ordering database.

## Setup

```bash
mkdir -p workspace/python/group-project/command-line-app && cd $_
```

## Instructions

You will create a series of prompts that will allow the user to create various types of data in your ordering system.

### Main Menu

```bash
*********************************************************
**  Welcome to Bangazon! Command Line Ordering System  **
*********************************************************
1. Create a customer account
2. Choose active customer
3. Create a payment option
4. Add product to shopping cart
5. Complete an order
6. See product popularity
7. Leave Bangazon!
>
```

### Create Customer

```bash
Enter customer name
>

Enter street address
>

Enter city
>

Enter state
>

Enter postal code
>

Enter phone number
>
```

### Choose active customer

```bash
Which customer will be active?
1. John Q. Public
2. Svetlana Z. Herevazena
>
```


### Create Payment Option

```bash
Enter payment type (e.g. AmEx, Visa, Checking)
>

Enter account number
>
```

### Add Product to Shopping Cart

> **Note:** These are examples. Add your own products to the *Product* table.

To make it easier to add multiple products, when the user selects a product to order, display the menu of products again. Make sure the last option of *Back to main menu* so the user can specify that no more products are needed.

```bash
1. Diapers
2. Case of Cracking Cola
3. Bicycle
4. AA Batteries
...
9. Done adding products
```

### Complete an Order

##### If no products have been selected yet

```bash
Please add some products to your order first. Press any key to return to main menu.
```

##### If there are current products in an order

```bash
Your order total is $149.54. Ready to purchase
(Y/N) >

# If user entered Y
Choose a payment option
1. Amex
2. Visa
>

Your order is complete! Press any key to return to main menu.

# If user entered N, display the main menu again
```

Once the order is complete, show the main menu again, where the user can start creating another order.

##### See product popularity

```bash
Print columns w/ basic formatting (i.e. money column has 2 decimals places)
1. AA Batteries ordered 10 times by 2 customers for total revenue of $99.90
2. Diapers ordered 5 times by 1 customers for total revenue of $64.95
3. Case of Cracking Cola ordered 4 times by 3 customers for total revenue of $27.96

-> Press any key to return to main menu
```

# References

## How to get started

```bash
Create a customer.txt file
This will include id number and customer information

Create a payment_options.txt file
This will include id number, customer id, and payment options information

Create a products.txt file
This will include id number, product name, product price information.

Create an order.txt file
This will include id number, customer id, payment id, and complete flag

Create an line_items.txt file
This will include id number, order id, product id
```

1. You can use `input()` and `print()` to show prompts and read user input.
1. You can write conditional logic with `if` or `switch`.

So start with the basics.

1. Show the main menu and read the user's choice of options with a `input()`.
1. Based on what the user entered in, `print()` their choice (e.g. "You chose to order a product")
1. Then create logic in each one of your conditions to accept further input.
1. Once all user input is gathered, perform the appropriate actions - reading or writing - and direct the user back to the main menu.
