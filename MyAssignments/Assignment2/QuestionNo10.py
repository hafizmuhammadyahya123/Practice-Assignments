# A school has following rules for grading system:
# a. Below 25 - F

# b. 25 to 45 - E

# c. 45 to 50 - D

# d. 50 to 60 - C

# e. 60 to 80 - B

# f. Above 80 - A

# Ask user to enter marks and print the corresponding grade

input_from_user = float(input('Enter your marks.'))

if input_from_user < 25:
    print('Your grade is F, means fail..')

elif input_from_user >= 25 and input_from_user < 45:
    print('Your grade is E')

elif input_from_user >= 45  and input_from_user < 50:
    print('Your grade is D') 

elif input_from_user >= 50 and input_from_user < 60:
    print('Your grade is C')     

elif input_from_user >= 60 and input_from_user <= 80:
    print('Your grade is B')

elif input_from_user > 80 and input_from_user <= 99.99:    
    print('CONGRATULATIONS YOUR GRADE IS A...')  

else:
    print('Invalid Marks...')        