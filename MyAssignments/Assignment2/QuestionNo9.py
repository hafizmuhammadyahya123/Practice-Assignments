# A shop will give discount of 10% if the cost of purchased quantity is more than 1000. 
# Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

price_unit_product = 100

perchased_product_quantity = int(input('Enter product quantity..'))
if perchased_product_quantity > 10:
    print(f'Rs{perchased_product_quantity * price_unit_product}')

    price = perchased_product_quantity * price_unit_product 
    if (price > 1000):
        print("CONGRATULATIONS....")
        print("You are eligible for '10%' discount")
        print(f'DISCOUNT = {price*0.10}')
        
else:
    print('perchased product quantity is less than 10')        



