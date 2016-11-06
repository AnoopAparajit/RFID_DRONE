import RPi.GPIO as GPIO
import time
import multiprocessing as m
import sys
import os
import threading as t

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)   #Left motor input A
GPIO.setup(40,GPIO.OUT)   #Left motor input B
GPIO.setup(32,GPIO.OUT)   #Left motor input A
GPIO.setup(36,GPIO.OUT)
GPIO.setup(7, GPIO.IN) 
GPIO.setwarnings(False)
class motor(t.Thread):
        def __init__(self):
                super(motor, self).__init__()
                self.stoprequest = t.Event()


        def run(self):
                while not self.stoprequest.isSet():
                        print("motor is running")
                        time.sleep(2)
                        GPIO.output(38,1)
                        GPIO.output(40,0)
                        GPIO.output(32,0)
                        GPIO.output(36,1)
        def join(self, timeout=None):
                self.stoprequest.set()
                super(motor, self).join(timeout)
mob=motor()
class pir(t.Thread) :
         def __init__(self):
                t.Thread.__init__(self)
         def run(self):
                 while True:
                        if GPIO.input(7):
                                print("Intruder detected")
                                mob.join()
                                time.sleep(2)
                        else:
                                print("No intruders")
                                time.sleep(1)

pob=pir()
mob.start()
pob.start()
