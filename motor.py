import RPi.GPIO as GPIO
import time
import multiprocessing as m
import sys
import os
import threading as t

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)   #Left motor input A
GPIO.setup(40,GPIO.OUT)   #Left motor input B
GPIO.setup(32,GPIO.OUT)   #Left motor input A
GPIO.setup(36,GPIO.OUT)
GPIO.setup(7, GPIO.IN) 
GPIO.setwarnings(False)
def motor():
        while True:
                print("Rotating both motors")
                GPIO.output(38,1)
                GPIO.output(40,0)
                GPIO.output(32,0)
                GPIO.output(36,1)
def pir():
         while True:
                
                if GPIO.input(7):
                        print("Intruder detected")
                        time.sleep(2)
                else:
                        print("No intruders")
                        time.sleep(1)

t1=t.Thread(target = motor)
t2=t.Thread(target = pir)
t1.start()
t2.start()
t1.join()
t2.join()
