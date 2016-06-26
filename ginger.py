#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

print('setting pins to out')
GPIO.setup(19, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

def forward():
    print('forward')
    GPIO.output(19, True)
    GPIO.output(16, False)
    GPIO.output(26, True)
    GPIO.output(20, False)

def reverse():
    print('reverse')
    GPIO.output(19, False)
    GPIO.output(16, True)
    GPIO.output(26, False)
    GPIO.output(20, True)

def left():
    print('left')
    GPIO.output(19, True)
    GPIO.output(16, False)
    GPIO.output(26, False)
    GPIO.output(20, True)

def right():
    print('right')
    GPIO.output(19, False)
    GPIO.output(16, True)
    GPIO.output(26, True)
    GPIO.output(20, False)

def main():
    forward()
    sleep(1)
    reverse()
    sleep(1)
    left()
    sleep(1)
    right()
    sleep(1)

    print('cleanup')
    GPIO.cleanup()
    print('exit')

if __name__ == '__main__':
    main()
