# Completes the following steps of small task:
# Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
# Mention Variable of Total Marks and assign 300 to it
# Calculate Percentage

# all variables  as a pascal case variable hain.
English = float(input('Enter Your English Marks.'))
Islamiat = float(input('Enter Your Islamiat Marks'))
Math = float(input('Enter your Math Marks'))

ObtainingMarks = English + Islamiat + Math

TotalMarks = 300

YourPercentage = (ObtainingMarks / TotalMarks) * 100  #PEMDAS RULE USE KIYA HA

print('Your_Percentage_IS',YourPercentage,'%')

# OR ...........................................

English , Islamiat , Math = 70 , 89 , 91

TotalMarks = 300

ObtainingMarks = English+Islamiat+Math

MyPercentage = (ObtainingMarks/TotalMarks) * 100

print('My Percentage is' , MyPercentage,'%')
 