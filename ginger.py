#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

class Ginger():

    runtime = 1

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)

    def forward(self):
        print('forward')
        self.setup()
        GPIO.output(17, True)
        GPIO.output(18, False)
        GPIO.output(26, True)
        GPIO.output(20, False)
        sleep(self.runtime)
        GPIO.cleanup()


    def reverse(self):
        print('reverse')
        self.setup()
        GPIO.output(17, False)
        GPIO.output(18, True)
        GPIO.output(26, False)
        GPIO.output(20, True)
        sleep(self.runtime)
        GPIO.cleanup()

    def left(self):
        print('left')
        self.setup()
        GPIO.output(17, True)
        GPIO.output(18, False)
        GPIO.output(26, False)
        GPIO.output(20, True)
        sleep(self.runtime)
        GPIO.cleanup()

    def right(self):
        print('right')
        self.setup()
        GPIO.output(17, False)
        GPIO.output(18, True)
        GPIO.output(26, True)
        GPIO.output(20, False)
        sleep(self.runtime)
        GPIO.cleanup()

    def stop(self):
        GPIO.cleanup()

