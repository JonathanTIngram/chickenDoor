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
	
	elif (month == 2):
		#Feb
		if (hour == '18:30:00'):
			print('make door go up')
		elif (hour == '19:30:00'):
			print("make door go down")
		else:
			print('do nothing')

	elif (month == 3):
		#March
		if (hour == '18:30:00'):
			print("make door go up")
		elif (hour == '19:30:00'):
			print('make door go won')
		else:
			print("do nothing")

	elif (month == 4):
		#April
		if (hour == '18:30:00'):
			print('make door go up')
		elif (hour == '19:30:00'):
			print('make door go down')
		else:
			print('do nothing')

	elif (month == 5):
		#May
		if (hour == '18:30:00'):
			print('make door go up')
		elif (hour == '19:30:00'):
			print('make door go down')
		else:
			print('do nothing')

	elif (month == 6):
		#June
		if (hour == '18:30:00'):
			print('make door go up')
		elif (hour == '19:30:00'):
			print('make door go down')
		else:
			print('do nothing')

	elif (month == 7):
		#July
		if (hour == '18:30:00'):
			print('make door go up')
		elif (hour == '19:30:00'):
			print('make door go down')
		else:
			print('do nothing')

	elif (month == 8):
		#August
		if (hour == '18:30:00'):
			print('make door go up')
		elif (hour == '19:30:00'):
			print('make door go down')
		else:
			print('do nothing')

	elif (month == 9):
		#September
		if (hour == '18:30:00'):
			print('make door go up')
		elif (hour == '19:30:00'):
			print('make door go down')
		else:
			print('do nothing')

	elif (month == 10):
		#October
		if (hour == '18:30:0'):
			print('make door go up')
		elif (hour == '19:30:00'):
			print('make door go down')
		else:
			print('do nothing')

	elif (month == 11):
		#November
		if (hour == '18:30:00'):
			print('make door go up')
		elif (hour == '19:30:00'):
			print('make door down')
		else:
			print('do nothing')

	elif (month == 12):
		#December
		if (hour == '18:30:00'):
			print('make door go up')
		elif (hour == '19:30:00'):
			print('make door go down')
		else:
			print('do nothing')
