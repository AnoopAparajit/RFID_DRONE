import RPi.GPIO as GPIO
import serial
import os, time

#Enable Serial Communication
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.01)
 
# Find a character in a string
def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch: 
           yield i
 
fd=''
while True:
    # Read the port
    rcv = port.read(10)
    if len(rcv) > 1:
        fd=fd+rcv
        ps=fd.find('\r')
        if ps >= 0:
            print fd[0:ps]
            fd=''
