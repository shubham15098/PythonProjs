import datetime

currentTime=datetime.datetime.now().time().strftime('%H:%M:%S %p') #%f can be used to display mSec
#print(currentTime.time())
#print(currentTime.hour)
#print(currentTime.minute)
#print(currentTime.second)
#currentTime=str(currentTime)
print(currentTime)

#print(datetime.datetime.now().time().strftime("%H:%M:%S"))
