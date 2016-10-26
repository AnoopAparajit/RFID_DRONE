import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(2.5)

p.ChangeDutyCycle(7.5)  # turn towards 90 degree
time.sleep(1) # sleep 1 second
p.ChangeDutyCycle(2.5)  # turn towards 180 degree
time.sleep(1) # sleep 1 second
p.stop()
GPIO.cleanup()
