# Take values of length and breadth of a rectangle from user and print if 
# it is square or rectangle.

length = float(input('Enter Length ..'))
breadth = float(input('Enter Breadth ...'))

if length == breadth:
    print('Four Sides Are Equal.This Is A Square.')
else:
    print('Rectangle')   

# OR ....................................................

# Area of Rectangle 
length = float(input('Enter Length..'))
breadth = float(input('Enter Breadth/width..'))

AreaOfRectangle = length*breadth

if length != breadth:
    print('THIS IS A RECTANGLE...')
    print(f'Area of Rectangle = {AreaOfRectangle}...')
else:
    print('Square..')

# OR....................................................

#  AREA OF SQUARE 
s = int(input('Enter legth side..'))
s **= 2
Area = s
if s == s:
    print('This is a square...')
    print('AREA OF SQUARE =' , Area)
else:
    print('Rectangle..')    
   



