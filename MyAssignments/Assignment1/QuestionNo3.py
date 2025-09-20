# Write a program in which use all the operators we can use in Python

# 1.Comparision Operators (> , < , >= , <= , != , ==)
# using f'string {}' method 
print(f'Absolutely Right {10 > 5}...')  #T

print(f'Absolutely Right {20 < 30}...') #T

print(f'Absolutely Wronge {10 < 5}...') #F

print(f'Absolutely Right {10 != 5}...') #T

print(f'Absolutely Right {10 == 10}...') #T

print(f'Absolutely Wronge {10 >= 20}...') #F

print(f'one condition is {10 <= 20} 10 is less then 20 ...\n') #T

# 2. Logical Operators (and , or , not) This is most useful 

print(f'Absolutely Right {(10 > 5) and (50 < 100)}')  #T

print(f'second condition is {20 < 30 and 20 != 20}') #F

print(f'second condition is {(10 < 5) or (10 > 5)}..') #T

print(f'Both condition is {10 != 5 or 10 <= 20} but 10 != 20...') #T

print(f'Both condition is {10 != 10 or 10 > 20}...') #F

print('output is-->' , not(10 >= 20) , '\tBut Actual Value Is False') #T

# 3. Assignment/Advance Operators  (Augment statement +=,-=,*=,/=,//=,%=)
                                      #e.g: a += 2   
# Arthematic operators ko Assignment operator k saath combined kr k Augment stat tyaar 
 
a = 20
a += 10  #Augment satement
print(a)

MyNumber = 100  #Pascal case var 
MyNumber -= 50
print(f'Difference = {MyNumber}')

my_num_1 = 40 #snake case var 
my_num_2 = 2
my_num_1 *= my_num_2 
print(f'Product = {my_num_1}')

MyNumber1 , MyNumber2 , MyNumber3 = 100 , 50 , 2
MyNumber1 /= MyNumber2 * MyNumber3 
            #PEMDAS Rule use huwa ha 
print(MyNumber1)

MyNumber1 = MyNumber2 = MyNumber3 = 40
MyNumber2 //= MyNumber3 * 2
            #PEMDAS Rule use huwa ha 

print(MyNumber2) 
# ----------------------------------------

MyNumberA = 12
MyNumberA %= 5 + 2  

print(MyNumberA)

MyNumberB = 30
MyNumberB **= 1
print(MyNumberB)

# ----------------------------------------
# 4. Arthematic Operators (+,-,*,**,/,//,%)
print('sum',2+5) 
print('Difference',10-5)
print('Product',20*2)
print('Exponent',2**3)
print('Quotient',30/5)
print('Floor Division',30//5)
print('Reminder',10%3)

# 5. Identity Operators (is , is not)
# is 
my_int_var_x = 20 
my_int_var_y = 20
print(my_int_var_x is my_int_var_y)

# is not 
my_int_var_x = 50 
my_int_var_y = 50

print(my_int_var_x is not my_int_var_y)

# 6. Membership Oerators (in , not in)
str = 'MY string'
dict = {'name':'ANDREW NG'}

# in 
print('MY' in str)

# not in 
print('name' not in dict)

