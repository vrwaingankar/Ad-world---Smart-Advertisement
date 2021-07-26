# python ad_world.py

import RPi.GPIO as GPIO 
import time 
from picamera import PiCamera
from time import sleep
from trim import convert_and_trim
import argparse
import imutils
import time
import dlib
import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

GPIO.setmode(GPIO.BCM) 
GPIO_TRIG = 11 
GPIO_ECHO = 18

GPIO.setup(GPIO_TRIG, GPIO.OUT) 
GPIO.setup(GPIO_ECHO, GPIO.IN) 
GPIO.output(GPIO_TRIG, GPIO.LOW) 
Time.sleep(1) 
GPIO.output(GPIO_TRIG, GPIO.HIGH) 
Time.sleep(0.00001) 
GPIO.output(GPIO_TRIG, GPIO.LOW) 

while GPIO.input(GPIO_ECHO)==0: 
	start_time = time.time() 

while GPIO.input(GPIO_ECHO)==1: 
	Bounce_back_time = time.time() 

pulse_duration = Bounce_back_time - start_time 
distance = round(pulse_duration * 17150, 2) 

if distance <=400:
	camera = PiCamera()
	camera.start_preview()
	for i in range(5):
		sleep(5)
		camera.capture(str(i)+'.jpg')
camera.stop_preview()
GPIO.cleanup()

detector = dlib.cnn_face_detection_model_v1("face_detector.dat")
tot_det = 0

for i in range(1,6):
	image = cv2.imread(str(i)+'.jpg')
	image = imutils.resize(image, width=600)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	start = time.time()
	results = detector(rgb, 1)
	end = time.time()
	print("[INFO] face detection took {:.4f} seconds".format(end - start))
	boxes = [convert_and_trim_bb(image, r.rect) for r in results]
	for (x, y, w, h) in boxes:
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
	tot_det+= len(boxes)

print(tot_det//5)
file1 = open('Individual_Samples.txt', 'a')
file1.write(str(tot_det//5) + '\n')
file1.close()

fromaddr = "sender mail address"
toaddr = "receiver mail address"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "New possible viewer detected"
body = "A possible interested viewer has been detected"
msg.attach(MIMEText(body, 'plain'))

filename = "Individual_Samples.txt"
attachment = open("path of file", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "sender mail password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()