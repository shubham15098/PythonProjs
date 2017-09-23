import turtle

count='0'
while count !='4':
    count=input('2+2 is ')

#Challenge Sketch Program

print('Sketch Program')
colour=''
lnLen=1
angle=0


while lnLen !=0:
    lnLen=int(input('What is the line length you prefer \n'))
    angle=int(input('What is the angle you prefer \n'))
    colour=input('What is the pen colour you prefer \n')
    turtle.color(colour)
    turtle.forward(lnLen)
    turtle.left(angle)
