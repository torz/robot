#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

print('setting pins to out')
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

def forward():
    print('forward')
    GPIO.output(17, True)
    GPIO.output(18, False)
    GPIO.output(26, True)
    GPIO.output(20, False)

def reverse():
    print('reverse')
    GPIO.output(17, False)
    GPIO.output(18, True)
    GPIO.output(26, False)
    GPIO.output(20, True)

def left():
    print('left')
    GPIO.output(17, True)
    GPIO.output(18, False)
    GPIO.output(26, False)
    GPIO.output(20, True)

def right():
    print('right')
    GPIO.output(17, False)
    GPIO.output(18, True)
    GPIO.output(26, True)
    GPIO.output(20, False)

def main():
    forward()
    sleep(5)

    print('cleanup')
    GPIO.cleanup()
    print('exit')

if __name__ == '__main__':
    main()
