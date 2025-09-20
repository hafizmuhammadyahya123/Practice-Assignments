# Modify the above question to allow student to sit if he/she has medical cause. 
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly

# snake case var name use
medical_case = input('He/She Please Enter Your MEDICAL CASE Or Not (Yes or No)..')

held_class = int(input('Enter your held classes...'))

attend_class = int(input('Enter your attend classes...'))

total_class = int(input('Enter your total classes..'))

percen_of_attend_class = (attend_class / total_class) * 100

if percen_of_attend_class >= 75:
    print(f"Your held classes are = {held_class}.")
    print(f"Your % of attend classes are = {percen_of_attend_class}.Student is allowed to sit exam")
    
elif percen_of_attend_class < 75 and medical_case == 'Yes':
    print(f'To allow student to sit if he/she has medical cause = {medical_case}')
    print('YOU ARE ALLOW TO SIT IN EXAMINATION HALL.....') 

elif percen_of_attend_class < 75 and  medical_case == 'No':
    print(f'To not allow student to sit if he/she has medical cause.{medical_case}..')
    print('You are not allow to sit in examination hall.')

else:
    print('STUDENTS WELCOME TO EXAMINATION HALL...')    

