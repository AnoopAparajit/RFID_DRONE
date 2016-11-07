import RPi.GPIO as GPIO
import time
import picamera as p
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

camera = p.PiCamera()
def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Hello'
    msg['From'] = 'dudabootstrap@gmail.com'
    msg['To'] = 'rishabhchawla1995@gmail.com'

    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('dudabootstrap@gmail.com', '2applepie')
    s.sendmail('dudabootstrap@gmail.com', 'rishabhchawla1995@gmail.com', msg.as_string())
    s.quit()

while True:
    if GPIO.input(7):
        print("Intruder detected")
        camera.start_preview()
        time.sleep(2)
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.stop_preview()
        SendMail('/home/pi/Desktop/image.jpg')
        time.sleep(2)
    else:
        print("No intruders")
        time.sleep(1)
