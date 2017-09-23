import string,csv,re



def main():
    messageList=[]
    userInput=input('Enter the message -\n')
    messageList.append(userInput.split(' '))

    print(messageList)
    print(readFile())
    checkIfEqual(messageList,readFile())
    return

def readFile():

    eachSent=[]
    eachSent1=[]

    with open('msg.txt','r')  as fileSolver:
        allRowList=csv.reader(fileSolver)
        for currentRow in allRowList:
            #eachSent.append(currentRow)
             for currentWord in currentRow:
                eachSent.append(currentWord.split(' '))
               
        fileSolver.close()

    #msgSolver.append(file.readline().split('-'))
    #print(msgSolver)
    return eachSent

def checkIfEqual(pMessageList,pEachSent):
    allAbreviations=[]
    for eEachSent in pEachSent:
        eEachSent=' '.join(eEachSent)
        print(eEachSent)

    for steps in range(len()):

    return
main()