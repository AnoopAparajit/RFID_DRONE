import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)      

while True:
    if GPIO.input(7):
        print("Intruder detected")
        subprocess.call("python rfid.py 1", shell=True)
        time.sleep(2)
    else:
        print("No intruders")
        time.sleep(1)
        
