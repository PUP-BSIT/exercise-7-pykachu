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
    customer_name = input("Enter customer name: ")
    senior_id = input("Enter senior ID no. (leave blank if not a senior "
    "citizen): ")
    
    return customer_name, senior_id

# TODO(Besa): Calculate the grand total for the order(s).

def calculate_grand_total(product_prices, product_quantities, is_senior):
    grand_total = 0

    for i in range(len(product_prices)):
        grand_total += product_prices[i] * product_quantities[i]

    if is_senior:
        discount = grand_total * 0.10
        grand_total -= discount
    
    return grand_total

# TODO(Serquina): Display the summary of order(s).

def display_order_summary(product_names, prices, quantities, customer_name,
                          senior_id, grand_total): 
    print("\n-------------- Order Summary ---------------")
    print("Items:")
    print("--------------------------------------------")

    for i in range(len(product_names)):
        product_name = product_names[i]
        price = prices[i]
        quantity = quantities[i]
        total_price = price * quantity
        print(f"{product_name} {price} x {quantity} = {total_price}")
    
    print("--------------------------------------------")
    print(f"Customer Name: {customer_name}")
    print(f"Senior ID No.: {senior_id if senior_id else 'N/A'}") 
    print(f"Grand Total: {grand_total}")
    print("--------------------------------------------")

#TODO(Bualat): Call the functions in the main function.

def main():

    product_names, product_prices, product_quantities = get_order_details()

    customer_name, senior_id = get_customer_details()
    
    is_senior = bool(senior_id)  
    
    grand_total = calculate_grand_total(product_prices, product_quantities, 
                                        is_senior)
    
    display_order_summary(product_names, product_prices, product_quantities, 
                          customer_name, senior_id, grand_total)

if __name__ == "__main__":
    main()