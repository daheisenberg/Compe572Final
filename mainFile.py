import os, os.path
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

GPIO.setup(11,GPIO.IN)




while True:

	i= GPIO.input(11)

#hello
	if i == 0:
		print "no intruders" , i
		GPIO.output(3,0)
		time.sleep(1)
	
	if i == 1:
		print "intruder" , i
		GPIO.output(3,1)
		os.system("python captureImage.py") 
		time.sleep(1)








