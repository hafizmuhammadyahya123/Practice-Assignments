#CH:CONTROL STRUCTURE..      (TOPIC CONDITIONAL STATEMENT)

# A company decided to give bonus of 5% to employee if his/her year of service is more
# than 5 years. Ask user for their salary and year of service and print the net bonus amount.

year_of_service = input('kiya as a Senior employee ho company k..')
if year_of_service == 'yes':
    print('Ok That\'s Great...')

    total_service = int(input('kitny year ho gye kaam krty huway..'))
    if total_service > 5:  # Nested if             
        print('Almost Bonus Milny K CHANCES Hain...')

        employee_salary = float(input('ENTER YOUR MONTHLY SALARY..'))
        if employee_salary >= 500000:
            print(f'CONGRATUALATIONS YOUR BONUS IS Confirmed:{employee_salary * 0.5}....')
    else:
        print('SOory your total service is < 5') 
else:
    print('SOory you are Junior Engineer')               



