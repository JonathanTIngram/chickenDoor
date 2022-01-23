#Timer.py


# @author: Jonathan Ingram
# Project: Chicken Door
# Created : 1/14/2021



import datetime

def month_to_time(month):
	if (month == 1):
		#"January"
                dt = datetime.datetime.today()
                hour = dt.time().strftime('%H:%M:%S')
                print(hour)
                if (hour == '20:03:00'):
                        import main1
                        print("make door go down")
                        try:
                            main1.rotate(10) #going down
                        except KeyboardInterrupt:
                            main1.p1.stop()
                            main1.p2.stop()
                            GPIO.cleanup()

                elif (hour == '06:30:00'):
                        print("make door go up")
                        try:
                            main1.rotate(10) #going up
                        except KeyboardInterrupt:
                            main1.p1.stop()
                            main1.p2.sto()
                            GPIO.cleanup()
                else:
                        print("do nothing")
                        print("\n     __//")
                        print("    /.__.\\")
                        print("    \ \\/ /")
                        print(" '__/   \\")
                        print("  \\-      )")
                        print("   \\_____/")
                        print("_____|_|_____")
                        print('     " " ')

	
	elif (month == 2):
		#Feb
		if (hour == '06:30:00'):
                        print('make door go up')
                        import main
                        main.rotate(0) #going up

		elif (hour == '18:30:00'):
                        print("make door go down")
                        import main
                        main.rotate(10)
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
