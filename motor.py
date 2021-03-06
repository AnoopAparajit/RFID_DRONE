import RPi.GPIO as GPIO
import time
import multiprocessing as m
import sys
import os
import threading as t
import serial
import subprocess


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)   #Left motor input A
GPIO.setup(40,GPIO.OUT)   #Left motor input B
GPIO.setup(32,GPIO.OUT)   #Left motor input A
GPIO.setup(36,GPIO.OUT)
GPIO.setup(7, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)
GPIO.setwarnings(False)

class camera(t.Thread):
      def __init__(self):
           t.Thread.__init__(self)
      def run(self):
              import camera
              with picamera.PiCamera() as pc:
                      pc.PiCamera()
                      pc.start_preview()
                      sleep(0)
                      pc.capture('/home/pi/Desktop/image.jpg')       
                      pc.stop_preview()

class rfid(t.Thread):
        def __init__(self):
                super(rfid, self).__init__()
                self.stoprequest = t.Event()
                
        def join(self, timeout=None):
                self.stoprequest.set()
                super(rfid, self).join(timeout)


        def run(self):
                ser = serial.Serial(
              
                    port='/dev/ttyS0',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                        )
                counter=0


                while 1:
                    x=ser.readline()
                    if x:   
                        print x
                        break
                      
                    else:
                        subprocess.call("python servo.py 1", shell=True)
                        break


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
                                rfidob=rfid()
                                rfidob.start()
                                rfidob.join()
                                camob=camera()
                                camob.start
                                time.sleep(2)
                        else:
                                print("No intruders")
                                time.sleep(1)

pob=pir()
mob.start()
pob.start()
