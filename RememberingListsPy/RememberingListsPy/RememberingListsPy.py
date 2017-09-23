#lists or generally arrays

'''
#looping and filling a list
guests=[]
userInput=input('Enter the guest name: \n')
counter=0
while userInput !='':
    guests[counter].append(userInput)
    print(guests[counter])
    counter +=1
    userInput=input('Enter the guest name: \n')
    
'''

#display the element of a list
guests=['buddhi','bob','john']
print(guests[1])

print(guests[-1]) #to get the last value

guests.append('newton') #append is to add a value
print(guests[3])

guests.remove('bob') #remove element by name
print(guests[1])
#removing will not leave a empty list element, it will completely remove the specified element

del guests[0] # remove element b index
print(guests[0])

guests.append('colin')
print(guests[2])
print(guests[-1])

print(guests[0])
#this will update the value
guests[0]='mike'
print(guests[0])


people=['buddhi','bob','colin','colin']#new list

people.remove('colin')# when duplicate values are available, this method will remove the first value only
print(people[-1])# therefore the last person is still colin

print(people.index('bob')) #will return the index number of where it's equal to bob

#loop all the values in the list using for loop
for steps in range(3):
    print(guests[steps])

 #loop all the elements using the index number and function len()

for steps in range(len(guests)):#len() will get the length of the list
    print(guests[steps])

#for each loop to display all elements
for guest in guests:
    print(guest)

#sort the list in alphabetical order
guests.sort()
for guest in guests:
    print(guest)


#CHALLENGE

print('Party List')
partyGuests=[]
singleGuest=input('Enter the guest name: \n')

while singleGuest !='':
    partyGuests.append(singleGuest)
    singleGuest=input('Enter the guest name: \n')

partyGuests.sort()
for guest in partyGuests:
    print(guest)


