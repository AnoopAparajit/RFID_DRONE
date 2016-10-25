import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)      

while True:
    if GPIO.input(7):
        print("Intruder detected")
        time.sleep(1)
    else:
        print("No intruders")
        time.sleep(1)
