# Bangazon

## The Command Line Ordering System

A Python3 command line application for purchasing products where data persists between sessions.

## Interface Displays

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
7. Exit Bangazon!
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
User List:
1. Human Person

>
```


### Create Payment Option

```bash
Enter payment type (e.g. AmEx, Visa, Checking)
>

Enter account number
>
```

### Add Product to an Order

When a product is selected to order, the menu of products is shown again.

```bash
Add Products                     

Products:                        
1. Charmin                       
2. Cottenelle                    
3. Everyone Poops: the Book      
4. Party Pooper: the game        
5. Nickleback                    
6. Sharknado 3                   
7. Back to main menu             


>     
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

Once the order is complete, the main menu is shown again, where the user can start creating another order.

### See Product Popularity

When selecting this option, you a report is generated resembling the following.

```bash
Product           Orders     Customers  Revenue
*******************************************************
Cottenelle        2          1          $13.00
Charmin           1          1          $7.00
Everyone Poops... 1          1          $12.99
Nickleback        1          1          $3.50
Party Pooper: ... 0          0          $0.00
Sharknado 3       0          0          $0.00
*******************************************************
Totals:           5          4          $36.49

Press ENTER to continue.
```

1. The product column is 18 characters wide, and displays a maximum of 17 characters for the product name.
1. The orders column is 11 characters wide.
1. The customers column is 11 characters wide.
1. The revenue column is 15 characters wide.


## File-Based Relational Data

Data generated by the program persists on disk through Python's pickle module.

1. The `customers.dat` file stores a serialized dictionary of customers, stored by id, that contains the following information.
    1. A unique customer id (integer).
    1. All information collected about the user (see prompts above).

1. The `payment_options.dat` file stores a serialized dictionary of payment options, stored by id, that contains the following information.
    1. A unique payment option id (integer).
    1. Payment option name.
    1. Payment option account number.

1. The `products.dat` file stores a serialized dictionary of products, stored by id, that contains the following information.
    1. A unique product id (integer).
    1. Product name.
    1. Product price.

1. The `orders.dat` file stores a serialized dictionary of orders, stored by id, that contains the following information.
    1. A unique order id (integer).
    1. The order's customer id.
    1. The order's payment option id.
    1. Whether the order has been paid in full.

1. The `order_line_items.dat` file stores a serialized dictionary of line items, stored by id, that contains the following information.
    1. A unique line item id (integer).
    1. The order id.
    1. The product id.
