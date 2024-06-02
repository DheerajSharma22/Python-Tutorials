from datetime import datetime

currHours= datetime.now().hour
currMins = datetime.now().minute

if (currHours >= 5 and (currHours < 12 or (currHours == 12 and currMins == 0))):
    print("Good Morning Sir")
elif (currHours > 12 and  (currHours < 18 or (currHours == 18 and currMins == 0))):
    print("Good Afternoon Sir")          
else:
    print("Good Evening Sir")
