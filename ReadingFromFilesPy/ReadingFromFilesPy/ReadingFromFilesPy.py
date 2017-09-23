'''
file=open('zooList.txt','w+')
file.write('Tiger, endangered\n')
file.write('Possom, common\n')
file.write('Panda, endangered\n')
file.write('Dire Wolf,  extinct\n')
'''
'''
file=open('zooList.txt','r')

firstAnimal=file.readline()# reads line by line
secondAnimal=file.readline()
print(firstAnimal)
print(secondAnimal)


fileContent=file.read()  #reads the whole file
print(fileContent
file.close()
'''

import csv
'''
with open('zooList.csv','r') as animalFile:
    allRowList = csv.reader(animalFile)
'''

'''
    #prints each row into the console
    for currentRow in allRowList:
        print(currentRow)
'''

'''
     #prints each row into the console
    for currentRow in allRowList:
        print(','.join(currentRow)) # this will take two words and join using the comma
'''

'''
    #prints each row into the console and prints each sentence separated by a comma of each row
    for currentRow in allRowList:
        print(currentRow)
        for currentWord in currentRow:
            print(currentWord)

'''

#Challenge

with open('Guests.txt','r') as guestList:
    allGuestList=csv.reader(guestList)

    for currentGuest in allGuestList:
        print(' '.join(currentGuest))
       # for guestAndAge in currentGuest:
          # print('')

