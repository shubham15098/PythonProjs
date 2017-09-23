import datetime

todayIs= datetime.date.today()
#print(todayIs)
#print(todayIs.strftime('%d-%b-%Y')) #date format as dd-MMM-YYYY
#print(todayIs.year)
#print(todayIs.month)
#print(todayIs.day)

userInput=input('Enter Your Birthday "Format(dd/mm/yyyy)"')
birthday= datetime.datetime.strptime(userInput, '%d/%m/%Y').date()
print(birthday)

days=todayIs-birthday
print(days.days)
