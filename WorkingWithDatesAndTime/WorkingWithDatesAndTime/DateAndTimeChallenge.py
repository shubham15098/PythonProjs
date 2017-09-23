import datetime

userInput=input("Please enter the deadline (dd/mm/yyyy)- ")
deadline=datetime.datetime.strptime(userInput,'%d/%m/%Y').date()
todayIs=datetime.date.today()
print(todayIs)
