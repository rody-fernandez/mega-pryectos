from picamera import PiCamera
from time import sleep
import smtplib
gmail_user = 'cuentaenvio@gmail.com'  
gmail_password = 'password'
import time
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import RPi.GPIO as GPIO
import time

toaddr = 'cuentarecepcion@gmail.com'
me = 'cuentaenvio@gmail.com'
Subject='security alert'

GPIO.setmode(GPIO.BCM)

P=PiCamera()
P.resolution= (1024,768)
P.start_preview()
    
GPIO.setup(23, GPIO.IN)
while True:
    if GPIO.input(23):
        print("Motion...")
        #camera warm-up time
        time.sleep(1)
        P.capture('movement.jpg')
        time.sleep(4)
        subject='Security allert!!'
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = toaddr
        
        fp= open('movement.jpg','rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)

        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()