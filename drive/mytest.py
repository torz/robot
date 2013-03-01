#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM()

while (True):
  # Change speed of continuous servo on channel O
  pwm.setPWMpercent(0, 10)
  time.sleep(2)
  pwm.setPWMpercent(0, 20)
  time.sleep(2)
  pwm.setPWMpercent(0, 30)
  time.sleep(2)
  pwm.setPWMpercent(0, 40)
  time.sleep(2)
  pwm.setPWMpercent(0, 50)
  time.sleep(2)
  pwm.setPWMpercent(0, 60)
  time.sleep(2)
  pwm.setPWMpercent(0, 70)
  time.sleep(2)
  pwm.setPWMpercent(0, 80)
  time.sleep(2)
  pwm.setPWMpercent(0, 90)
  time.sleep(2)
  pwm.setPWMpercent(0, 100)
  time.sleep(2)
  pwm.setSLEEPMode()
  break



