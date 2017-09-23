#if with strings
#answer=input("yes or no \n");

#if answer.upper() == "yes":
#    print("You selected yes")
    
#print("Have a nice day")


#if with int
#deposit=int(input("enter amount "))

#if deposit>100:
#    print("You won!!")
#print("Have a nice day")

##if and else
#deposit=int(input("enter the amount "))

#if deposit > 100 :
#    print("won a toaster!!")
#else :
#    print("Won a mug!!")

#print("Have a nice day")

##if with boolean
#deposit=int(input("enter the amount "))
#freeToaster=False #gave an initial value
#if deposit > 100 :
#    freeToaster=True

##several lines of codes

#if freeToaster:

#    print("Won a toaster!!")

#print("Have a nice day")

##Challenge
#shipChgs=int(input("Please enter the amount : "))


#if shipChgs<50:
#    shipChgs=shipChgs+10
#    print("Final Total with Shipping cost : $"+shipChgs)
#else :
#    print("Final Total (Shipping charge is free!!) : $"+shipChgs)

##If/ELseIf & Else
#country=input("Country?").lower();

#if country=="england":
#    print("Hello");
#elif country=="france":
#    print("Bonjour");
#else:
#    print("Salut/Ciao/G'day/Aloha");

##if with AND, OR

#sport=input("Enter your favourite sport : ").lower();
#team=input("Enter you favourite cricket team : ").lower();

#if sport=="cricket" and team=="england":
#    print("England has a great cricket team!!");
#elif team=="india" or team=="pakistan":
#        print("Good luck getting the cup this years");
#else:
#    print("not a sports person aye?");

##if with AND/OR in same statement with parenthesis
##if the sport is cricket, and the team is sri lanka or england, display the msg
#sport=input("Enter your favourite sport : ").lower();
#team=input("Enter you favourite cricket team : ").lower();

#if sport=='cricket' and (team=='sri lanka' or team=='england'):
#    print('Good luck in the world cup!!');
#else:
#     print("not a cricket person aye?");

##nested if conditions, (careful with the indentations)
#monday=True
#freshCoffee=False

#if monday:
#    if not freshCoffee:
#        print("go buy a coffee");
#    print("I hate mondays");
#print("Now start working");

#Challenge for Complex desicions with code

'''
print("Online Store In Canada");
country=input("Where are you from?\n").lower();
userTotal=int(input("What's the order total?\n"));

if country=="canada":
    province=input("From which province?\n").lower();
    if province=="alberta":
        userTotal=userTotal*1.05
        print("Online Store Bill\n You are from "+country+", "+province+" Your bill is $"+str(userTotal)+ \
            " ,including Tax");
    elif province=="ontario" or province=="new brunswick" or province=="nova scotia":
        userTotal=userTotal*1.13
        print("Online Store Bill\n You are from "+country+", "+province+" Your bill is $"+str(userTotal)+ \
            " ,including Tax");
    else:
        userTotal=(userTotal*1.06)*1.05
        print("Online Store Bill\n You are from "+country+", "+province+" Your bill is $"+str(userTotal)+ \
            " ,including Tax");

else:
    print("Online Store Bill\n You are from "+country+"\n You are bill is $"+str(userTotal));


'''

print('Online Store')
custName=input('Enter Your Name ')
total=int(input('Enter Bill Total '))

if custName=='bob':
    total=total+1;
    print(custName+"'s total is "+str(total))
    if total>=10:
        total=total*2;
        print(custName+"'s total is "+str(total)+" which is greater than 10");
    elif total<10:
        print(custName+"'s total is "+str(total)+" which is less than 10");
elif custName=='john':
    total=total+1;
    print(custName+"'s total is"+str(total));
else:
    print(custName+"'s total is"+str(total));
