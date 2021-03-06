import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN,GPIO.IN)

try:
	print("PIR Module Test")
	time.sleep(2)
	print("Ready")

	while True:
		if GPIO.input(PIR_PIN):
			print("Motion detected!")
		time.sleep(1)
except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
