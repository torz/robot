#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM()

while (True):
  # Change speed of continuous servo on channel O
  print '10'
  pwm.setPWMpercent(0, 10)
  time.sleep(2)
  print '20'
  pwm.setPWMpercent(0, 20)
  time.sleep(2)
  print '30'
  pwm.setPWMpercent(0, 30)
  time.sleep(2)
  print '40'
  pwm.setPWMpercent(0, 40)
  time.sleep(2)
  print '50'
  pwm.setPWMpercent(0, 50)
  time.sleep(2)
  print '60'
  pwm.setPWMpercent(0, 60)
  time.sleep(2)
  print '70'
  pwm.setPWMpercent(0, 70)
  time.sleep(2)
  print '80'
  pwm.setPWMpercent(0, 80)
  time.sleep(2)
  print '90'
  pwm.setPWMpercent(0, 90)
  time.sleep(2)
  print '100'
  pwm.setPWMpercent(0, 100)
  time.sleep(2)
  print 'sleep'
  pwm.setSLEEPMode()
  break



