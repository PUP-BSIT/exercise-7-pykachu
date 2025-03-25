# TODO(Salespara): Get the user inputs for the details of the order(s).

def get_order_details():
    product_names = []
    product_prices = []
    product_quantities = []

    while True:
        product_name = input("Enter Product Name: ")
        product_price = float(input("Enter Product Price: "))
        product_quantity = int(input("Enter Product Quantity: "))
        product_names.append(product_name)
        product_prices.append(product_price)
        product_quantities.append(product_quantity)
        another_item = input("Add another item? (y/n): ").lower()
        if another_item != 'y':
            break
        
    return product_names, product_prices, product_quantities

# TODO(Maestre): Get the user inputs for the details of the customer.

def get_customer_details():
    pass

# TODO(Besa): Calculate the grand total for the order(s).

def calculate_grand_total():
    pass

# TODO(Serquina): Display the summary of order(s).
def display_order_summary():
    pass

#TODO(Bualat): Call the functions in the main function.

def main():
    pass

if __name__ == "__main__":
    main()