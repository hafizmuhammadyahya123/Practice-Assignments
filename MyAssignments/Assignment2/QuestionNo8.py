# Take two int values from user and print greatest among them.

input1_from_user = int(input('Enter Number1..'))
input2_from_user = int(input('Enter Number2..')) 

if (input1_from_user > input2_from_user):
    print('input1 is greater than input2')

elif input2_from_user > input1_from_user:
    print('input2 is greater than input1') 

else:
    print('input1 is equal to input2')    