robot
=====

RPi robot

Raspberry Pi Model B rev 2

PWM for DC motor speed control:
	http://www.adafruit.com/products/815
	PCA9685 - i2c

MODE1

	 |------------------ RESTART = 1
	 | |---------------- INTCLK 0/1 EXTCLK 
	 | |   |------------ SLEEP = 1
	 | |   |
	 | |   |       |---- ALLCALL
	 0 0 0 0 0 0 0 0

MODE2

	         |----------- Change on ACK = 1
	         |
	 0 0 0 0 0 0 0 0


Motor direction control:
	l293d

