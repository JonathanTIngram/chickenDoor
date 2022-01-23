# main.py
#
# Jonathan Ingram -  Software
# Zachary Ingram  -  Testing
#
#


import RPi.GPIO as GPIO
import time
from datetime import datetime


servoPIN1 = 15
servoPIN2 = 27

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

#motor 1
GPIO.setup(servoPIN1, GPIO.OUT, initial=GPIO.HIGH)
p1 = GPIO.PWM(servoPIN1, 50)



#motor 2
#GPIO.setup(servoPIN2, GPIO.OUT)
#p2 = GPIO.PWM(servoPIN2, 50)

p1.start(1.0)  #initalization
#p2.start(2.5)

def get_month(dt_string):

        #get_current date
        datetime_object = datetime.now()
        timer.month_to_time(datetime_object.month)

def rotate(angle):

        if (angle > 0):

                angle -= (angle/2) #speed/changing angle on rotation
                print(angle, "increasing")
                p1.ChangeDutyCycle(angle) #this is what actually makes it spin
                #p2.ChangeDutyCycle(angle)

        if (angle == 0):
                angle += 10
                print(angle, "decreasing")
                p1.ChangeDutyCycle(angle) #this is what actually makes it spin
                #p2.ChangeDutyCycle(angle)
                time.sleep(13) #change this

GPIO.setwarnings(False)

def test(val):
        GPIO.warnings(False)
        #just for testing
        #p2.ChangeDutyCycle(val)


try:
        while True:
                rotate(10)

except KeyboardInterrupt:
        p1.stop()
        #p2.stop()
        GPIO.cleanup()
