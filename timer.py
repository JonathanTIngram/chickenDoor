#Timer.py


# @author: Jonathan Ingram
# Project: Chicken Door
# Created : 1/14/2021



import datetime

dt = datetime.datetime.today()
hour = dt.time().strftime('%H:%M:%S')

def month_to_time(month):
	if (month == 1):
		#"January"
		print(hour)
		if (hour == '18:30:00'):
			print("make door go up")
		
		elif (hour == '19:30:00'):
			print("make door go down")
		else:
			print("do nothing") 

