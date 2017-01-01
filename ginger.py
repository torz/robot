#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

class Ginger():

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)

    def forward(self):
        print('forward')
        GPIO.output(17, False)
        GPIO.output(18, True)
        GPIO.output(26, False)
        GPIO.output(20, True)

    def reverse(self):
        print('reverse')
        GPIO.output(17, True)
        GPIO.output(18, False)
        GPIO.output(26, True)
        GPIO.output(20, False)

    def left(self):
        print('left')
        GPIO.output(17, False)
        GPIO.output(18, True)
        GPIO.output(26, True)
        GPIO.output(20, False)

    def right(self):
        print('right')
        GPIO.output(17, True)
        GPIO.output(18, False)
        GPIO.output(26, False)
        GPIO.output(20, True)

    def stop(self):
        GPIO.cleanup()

