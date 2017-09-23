'''trArea = 0
trHeight= 10
trWidth=20

#area of triangle
trArea=(trHeight*trWidth)/2

print("Area of triangle is %f" %trArea)
'''


#Tripple quotes can be used to create multiline comments because # is not effective at multiline comment
area = 0
height=int(input("Height: "))
width=int(input("width: "))

#Area of rectangle
area=height*width

print("Area of the square = {0:04f}".format(area))


'''
#.format() formatting multiple numbers

print("First Number {0:2d} Second Number {1:03d} Third Number {2:d}".format(1,2,3))

#typing long commands in two lines

print("This is my first Number"+\
    "{0:2d},this is my Second Number {1:03d} and this is my Third Number {2:d}".format(1,2,3))
'''

area=0
width=int(input("Enter the width: "))
height=int(input("Enter the height: "))

area=width*height

print("Area is"+ area)

'''
tripple quotes are used for multiline comments
'''
