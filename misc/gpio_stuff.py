import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

def forward():
	GPIO.output(24, False)
	GPIO.output(25, True)

def back():
	GPIO.output(24, True)
	GPIO.output(25, False)

def stop():
	GPIO.output(24, False)
	GPIO.output(25, False)

