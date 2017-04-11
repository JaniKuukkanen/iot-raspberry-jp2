import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
Timenow = time.strftime("%Y-%m-%d %H:%M:%S")

while True:
	i=GPIO.input(7)
	if i==0:
	
		time.sleep(0.1)
	elif i==1:
		print("PANIC!!!" + time.strftime("%Y-%m-%d %H:%M:%S"))
		time.sleep(0.1)
