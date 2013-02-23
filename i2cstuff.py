#!/usr/bin/python

import smbus
import sys
import time 
bus = smbus.SMBus(1)

address = 0x40 # I2C address of MCP23017
#bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to outputs 
#bus.write_byte_data(0x20,0x01,0x00) # Set all of bank B to outputs 


def InitPCA9685():
	# MODE1 
	bus.write_byte_data(address,0x00,0b0)
	time.sleep(2)
	bus.write_byte_data(address,0x00,0b00110001)
	time.sleep(0.5)
	bus.write_byte_data(address,0xfe,0x04)
	time.sleep(0.5)
	bus.write_byte_data(address,0x00,0xa1)
	time.sleep(0.5)
#	bus.write_byte_data(address,0x01,0b00011111)
	bus.write_byte_data(address,0x01,0b00011101)
	time.sleep(0.5)
	return

def SetPWM7():
	bus.write_byte_data(address,0x06, 0b00000000)
	bus.write_byte_data(address,0x07, 0b00000000)
	bus.write_byte_data(address,0x08, 0b00000000)
	bus.write_byte_data(address,0x09, 0b00001000)
#try write all...	
#	bus.write_byte_data(address,0xfa,0x00)
#	bus.write_byte_data(address,0xfb,0x00)
#	bus.write_byte_data(address,0xfc,0xFF)
#	bus.write_byte_data(address,0xfd,0x00)
	return

def GetPWM7():
   try:
	mode1 = bus.read_byte_data(address,0x00)
	mode2 = bus.read_byte_data(address,0x01)
	onL = bus.read_byte_data(address,0x22)
	onH = bus.read_byte_data(address,0x23)
	offL = bus.read_byte_data(address,0x24)
	offH = bus.read_byte_data(address,0x25)
	print 'Mode1 ',bin(mode1)
	print 'Mode2 ',bin(mode2)
	print 'onLow ',bin(onL),' onHigh ',bin(onH)
	print 'offLow ',bin(offL),' offHigh ',bin(offH)
   except:
	return

def main():
	InitPCA9685()
	SetPWM7()
	GetPWM7()
   
  
if __name__ == "__main__":
   main()
