#!/usr/bin/python

import smbus
from time import sleep
bus = smbus.SMBus(1)

address = 0x40


__MODE1					= 0x00
__MODE2					= 0x01
__PRESCALE				= 0xFE
__LED0_ON_L				= 0x06
__LED0_ON_H				= 0x07
__LED0_OFF_L			= 0x08
__LED0_OFF_H			= 0x09
__ALLLED_ON_L			= 0xFA
__ALLLED_ON_H			= 0xFB
__ALLLED_OFF_L			= 0xFC
__ALLLED_OFF_H			= 0xFD


def changeMODE1(mode='normal'):
	# Modes available
	__NORMAL_MODE		= 0x01
	__SLEEP_MODE		= 0x11
	__RESTART			= 0x80
	# set mode
	if mode == 'normal':
		newmode = __NORMAL_MODE
	elif mode == 'sleep':
		newmode = __SLEEP_MODE
	elif mode == 'restart':
		changeMODE1('sleep')
		newmode = __RESTART
	else:
		print 'No such mode available'
		return False
	# write mode
	bus.write_byte_data(address, __MODE1, newmode)
	sleep(0.005)
	return newmode

def sleepMODE():
	print 'Sleep Mode'
	bus.write_byte_data(address, 0x00, 0b00010001)
	print bin(bus.read_byte_data(address, 0x00))
	sleep(1)

def normalMODE():
	# normal mode
	print 'Normal mode'
	bus.write_byte_data(address, 0x00, 0b00000001)
	print bin(bus.read_byte_data(address, 0x00))
	sleep(1)
	print bin(bus.read_byte_data(address, 0x00))
	
def setMODE2():
	# setting MODE2
	print 'Setting mode2'
	bus.write_byte_data(address, 0x01, 0b00001000)
	print bin(bus.read_byte_data(address, 0x00))
	sleep(1)
	
def setPRESCALE():
	sleepMODE()
	
	# set prescaler
	print 'Setting prescaler'
	print bin(bus.read_byte_data(address, 0xfe))
	bus.write_byte_data(address, 0xfe, 0b01100101)
	sleep(1)
	
	normalMODE()

def SetPWM1():
	print 'Setting PWM 1'
	bus.write_byte_data(address, 0x06, 0b00000000)
	bus.write_byte_data(address, 0x07, 0x00000000)
	bus.write_byte_data(address, 0x08, 0b00000000)
	bus.write_byte_data(address, 0x09, 0b00000100)
	sleep(2)

def SetPWM2():
	print 'Setting PWM 2'
	bus.write_byte_data(address, 0x06, 0b00000000)
	bus.write_byte_data(address, 0x07, 0x00000000)
	bus.write_byte_data(address, 0x08, 0b11111111)
	bus.write_byte_data(address, 0x09, 0b00000100)
	sleep(2)

def SetPWM3():
	print 'Setting PWM 3'
	bus.write_byte_data(address, 0x06, 0b00000000)
	bus.write_byte_data(address, 0x07, 0x00000000)
	bus.write_byte_data(address, 0x08, 0b00000000)
	bus.write_byte_data(address, 0x09, 0b00001000)
	sleep(2)

def SetPWM4():
	print 'Setting PWM 4'
	bus.write_byte_data(address, 0x06, 0b00000000)
	bus.write_byte_data(address, 0x07, 0x00000000)
	bus.write_byte_data(address, 0x08, 0b11111111)
	bus.write_byte_data(address, 0x09, 0b00001111)
	sleep(2)

def GetPWM():
	onL = bus.read_byte_data(address, 0x06)
	onH = bus.read_byte_data(address, 0x07)
	offL = bus.read_byte_data(address, 0x08)
	offH = bus.read_byte_data(address, 0x09)
	print 'onLow ', bin(onL), ' onHigh ', bin(onH)
	print 'offLow ', bin(offL), ' offHigh ', bin(offH)
	print '============================================'

def main():
	normalMODE()
	setPRESCALE()
	setMODE2()
	SetPWM1()
	SetPWM2()
	SetPWM3()
	SetPWM4()
  	sleepMODE()

if __name__ == "__main__":
	main()
