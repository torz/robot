#!/usr/bin/python

import smbus
import time
bus = smbus.SMBus(1)

address = 0x40

def sleepMODE():
	print 'Sleep Mode'
	bus.write_byte_data(address, 0x00, 0b00010001)
	print bin(bus.read_byte_data(address, 0x00))
	time.sleep(1)

def normalMODE():
	# normal mode
	print 'Normal mode'
	bus.write_byte_data(address, 0x00, 0b00000001)
	print bin(bus.read_byte_data(address, 0x00))
	time.sleep(1)
	print bin(bus.read_byte_data(address, 0x00))
	
def setMODE2():
	# setting MODE2
	print 'Setting mode2'
	bus.write_byte_data(address, 0x01, 0b00001000)
	print bin(bus.read_byte_data(address, 0x00))
	time.sleep(1)
	
def setPRESCALE():
	sleepMODE()
	
	# set prescaler
	print 'Setting prescaler'
	print bin(bus.read_byte_data(address, 0xfe))
	bus.write_byte_data(address, 0xfe, 0x04)
	time.sleep(1)
	
	normalMODE()

def SetPWM1():
	print 'Setting PWM 1'
	bus.write_byte_data(address, 0x06, 0b00000000)
	bus.write_byte_data(address, 0x07, 0x00000000)
	bus.write_byte_data(address, 0x08, 0b00000000)
	bus.write_byte_data(address, 0x09, 0b00000100)
	time.sleep(2)

def SetPWM2():
	print 'Setting PWM 2'
	bus.write_byte_data(address, 0x06, 0b00000000)
	bus.write_byte_data(address, 0x07, 0x00000000)
	bus.write_byte_data(address, 0x08, 0b11111111)
	bus.write_byte_data(address, 0x09, 0b00000100)
	time.sleep(2)

def SetPWM3():
	print 'Setting PWM 3'
	bus.write_byte_data(address, 0x06, 0b00000000)
	bus.write_byte_data(address, 0x07, 0x00000000)
	bus.write_byte_data(address, 0x08, 0b00000000)
	bus.write_byte_data(address, 0x09, 0b00001000)
	time.sleep(2)

def SetPWM4():
	print 'Setting PWM 4'
	bus.write_byte_data(address, 0x06, 0b00000000)
	bus.write_byte_data(address, 0x07, 0x00000000)
	bus.write_byte_data(address, 0x08, 0b11111111)
	bus.write_byte_data(address, 0x09, 0b00001111)
	time.sleep(2)

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
