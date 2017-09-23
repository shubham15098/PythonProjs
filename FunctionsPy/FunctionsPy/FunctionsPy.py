import csv
import helpers
def main():

   # printMessage('hi','sexy')
    #printNames()
   # guestList()
   # writeToFile( guestList(),'demo.txt')
    readFromFile('demo.txt')
    helpers.displayDeadline ()
    return

def printMessage():

    print('Hello World\n')
    return

def printNames():

    names=['john','bob','simon','nathan']

    for name in names:
        print(name)
    return

def printMessage(message):

    print(message+'\n')
    return

def printMessage(message1,message2):

    print(message1+' '+message2+'\n')
    return

def writeToFile(text,filename):

    file=open(filename,'w')
    for name in text:
        file.write(name+'\n')

    print('file written successfully!!!')
    file.close()
    return
def guestList():
    names=[]
    userInput=input('Enter the guest name: \n')
    while userInput != '':
        names.append(userInput)
        userInput=input('Enter the guest name: \n')

    return names

def readFromFile(filename):
    with open(filename,'r') as guestList:
        allguestsInList=csv.reader(guestList)

        for currentGuest in allguestsInList:
            print(' '.join(currentGuest))
        
    return
main()