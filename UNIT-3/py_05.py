#display current date and time using datetime module
import datetime
now=datetime.datetime.now()
print('date and time:',now)


formated_now=now.strftime("%d-%m-%Y  %H:%M:%S")
print('formated date and time:',formated_now)

