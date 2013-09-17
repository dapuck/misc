#!/usr/bin/python

import time
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from myDHCPip import myDHCPip

lcd = Adafruit_CharLCDPlate()
lcd.begin(16,2)
lcd.clear()
lcd.message("Hello!")
time.sleep(3)
lcd.clear()
lcd.message("The date is\n%s" % time.strftime('%b %d, %Y'))
time.sleep(5)
lcd.clear()
lcd.message("The time is\n%s" % time.strftime('%I:%M %p'));
time.sleep(5)
lcd.clear()
ip = ''
try:
	ip = myDHCPip('eth0').ip
except Exception as i:
	ip = 'Not connected'
lcd.message("IP Address\n%s" % ip)
time.sleep(10)
lcd.clear()
lcd.backlight(lcd.OFF)

while True:
	if lcd.buttonPressed(lcd.SELECT):
		lcd.backlight(lcd.ON)
		lcd.message("IP Address\n%s" % ip)
		time.sleep(10)
		lcd.clear()
		lcd.backlight(lcd.OFF)
	time.sleep(0.1)
