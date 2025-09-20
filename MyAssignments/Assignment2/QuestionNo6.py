# Write a program to display the last digit of a number.

Number = 104

if Number%10 == 4:
    print('Reminder =', 4 ,' = Last Digit..' )
else:
    print('104 is not last digit')    

# OR -------------------------------------------
InputFromUser = int(input('Enter Number...'))

if InputFromUser%10 == 4:
    print('Last digit = Reminder = 4' )
else:
    print('104 is not last digit')    