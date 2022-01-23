# main.py
#
# Jonathan Ingram -  Software
# Zachary Ingram  -  
#
#


import RPi.GPIO as GPIO
import time
from datetime import datetime
import timer
#import touch

servoPIN1 = 15
servoPIN2 = 27

GPIO.setmode(GPIO.BCM)


#motor 1
GPIO.setup(servoPIN1, GPIO.OUT)
p1 = GPIO.PWM(servoPIN1, 50)

#motor 2
GPIO.setup(servoPIN2, GPIO.OUT)
p2 = GPIO.PWM(servoPIN2, 50)

p1.start(2.5)  #initalization
p2.start(2.5)

def get_month(dt_string):

	#get_current date 
	datetime_object = datetime.now()
	timer.month_to_time(datetime_object.month)
#def touch_rotate(touchCount):
	#tc = touchCount % 2
	#t = touch.read_touch()
	#if (t):
		#if (tc == 0):
			#rotate(0)
		#else:#
			#rotate(10)
def rotate(angle):
 
    if (angle > 0):	
        angle -= (angle/2) #speed/changing angle on rotation
        print(angle, "going down")
        p1.ChangeDutyCycle(angle) #this is what actually makes it spin
        p2.ChangeDutyCycle(angle)
        time.sleep(9) #14 or 15 change this value for change length of rotation
        

    if (angle == 0):
        angle += 10
        print(angle, "going up")
        p1.ChangeDutyCycle(angle) #this is what actually makes it spin
        p2.ChangeDutyCycle(angle)
        time.sleep(9) #12  change this



def test(val):
	#just for testing
	p1.ChangeDutyCycle(val)
	p2.ChangeDutyCycle(val)				


try:
#    pass
    # rotate(10) #go down
     rotate(0) #go up
except KeyboardInterrupt:
	p1.stop()
	p2.stop()
	GPIO.cleanup() 
