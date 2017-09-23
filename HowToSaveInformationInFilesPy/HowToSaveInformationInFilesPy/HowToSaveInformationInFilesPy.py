'''filename='demo.txt'
WRITE='w' # write a new file
READ='r' #read file
APPEND='a' #append a file
READWRITE='w+' # w+ means read/write

file=open(filename,WRITE)
file.write('This is the first line\n    ')
file.write('This is the second line')

print('File writing successfull')

file.close()
'''

#Challenge

filename='newFile01.dat'
WRITE='w'
READ='r'
APPEND='a'
READWRITE='w+'
userInput=input('Enter a name:\n')

file=open(filename,WRITE)

while userInput !='':
    file.write(userInput)
    print ('Name added successfully!!!')
    userInput=input('Enter a name:\n')

file.close()

#file=open(filename,WRITE)
#file.close()
