import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)   #Left motor input A
GPIO.setup(40,GPIO.OUT)   #Left motor input B
GPIO.setup(32,GPIO.OUT)   #Left motor input A
GPIO.setup(36,GPIO.OUT)
GPIO.setwarnings(False)
while True:
        print "Rotating both motors in clockwise direction"
        GPIO.output(38,1)
        GPIO.output(40,0)
        GPIO.output(32,0)
        GPIO.output(36,1)
         
