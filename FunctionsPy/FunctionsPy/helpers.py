import datetime

def displayDaysFrmBday():
    todayIs= datetime.date.today()
    userInput=input('Enter Your Birthday "Format(dd/mm/yyyy)"')
    birthday= datetime.datetime.strptime(userInput, '%d/%m/%Y').date()
    print(birthday)

    days=todayIs-birthday
    print(days.days)
    return

def displayDeadline():
    userInput=input("Please enter the deadline (dd/mm/yyyy)- ")
    deadline=datetime.datetime.strptime(userInput,'%d/%m/%Y').date()
    todayIs=datetime.date.today()
    print(deadline-todayIs)
    return
