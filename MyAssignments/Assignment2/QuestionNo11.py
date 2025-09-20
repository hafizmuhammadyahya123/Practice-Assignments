# A student will not be allowed to sit in exam if his/her attendence is less than 75%.

# Take following input from user

# Number of classes held

# Number of classes attended.

# And print

# percentage of class attended

# Is student is allowed to sit in exam or not.


# Pascal case var name use kiyay
HeldClass = int(input('Enter Number of classes held..'))  
AttendClass = int(input('Enter Number of classes attended...')) 
TotalClass = int(input('Enter Total Classes....'))

PercentageOfClassAttend = (AttendClass/TotalClass) * 100

if PercentageOfClassAttend >= 75:
    print(f'Your held classes are = {HeldClass}')
    print(f'Your percentage of attend class is={PercentageOfClassAttend}.Student are allowed to sit in exam..')

elif PercentageOfClassAttend < 75:
    print(f'Your held classes are = {HeldClass}')
    print(f'Your percentage of attend class is={PercentageOfClassAttend}.Student are not allowed to sit in exam...')    

else:
    print('Students, Welcome to examination hall..')
