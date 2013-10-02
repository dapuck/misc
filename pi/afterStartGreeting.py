#!/usr/bin/python

import time
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from myDHCPip import myDHCPip

lcd = Adafruit_CharLCDPlate()
ip = ''
try:
	ip = myDHCPip('eth0').ip
except Exception as i:
	ip = 'Not connected'

def main():
	init_greeting()
	main_loop()

def init_greeting():
	lcd.begin(16,2)
	lcd.clear()
	lcd.message("Hello!")
	time.sleep(3)
	show_date()
	time.sleep(5)
	show_time()
	time.sleep(5)
	show_ip()
	time.sleep(10)
	lcd.clear()
	lcd.backlight(lcd.OFF)

def show_date():
	lcd.backlight(lcd.ON)
	lcd.clear()
	lcd.message("The date is\n%s" % time.strftime('%b %d, %Y'))

def show_time():
	lcd.backlight(lcd.ON)
	lcd.clear()
	lcd.message("The time is\n%s" % time.strftime('%I:%M %p'))

def show_ip():
	lcd.backlight(lcd.ON)
	lcd.clear()
	lcd.message("IP Address\n%s" % ip)

def main_loop():
	time_of_last_press = time.time();
	while True:
		btns = lcd.buttons()
		if btns > 0:
			change_state(btns)
			time_of_last_press = time.time()
		elif time.time() - time_of_last_press >= 10:
			time_of_last_press = time.time()
			change_state(0,True)
		time.sleep(0.1)
'''
btn is the button bit mask from the LCD Plate Lib.
The bit mask is 5 bits representing (from left to right):

Left Up Down Right Select

 0   0   0     0     0

Obviously, when a button is pressed, the coresponding bit
is set to 1.

Using the bit mask here allows us to use button combos to 
change state.
'''
def change_state(btn, reset=False):
	global current_state
	# get dict for current state 
	#print lcd.buttons()
	if reset:
		lcd.clear()
		lcd.backlight(lcd.OFF)
		current_state = 'start'
		return
	state_dict = states[current_state]
	# if btn is in dict for current state
	if btn in state_dict:
		# set current state to dict[btn][0]
		# run func dict[btn][1]
		current_state = state_dict[btn][0]
		state_dict[btn][1]()
	time.sleep(0.5)

current_state = 'start'
states = {
  'start': {
    (1 << lcd.SELECT): [ 'date', show_date ]
  },
  'date': {
    (1 << lcd.SELECT): [ 'time', show_time ],
    (1 << lcd.DOWN): [ 'time', show_time ]
  },
  'time': {
    (1 << lcd.SELECT): [ 'ip', show_ip ],
    (1 << lcd.DOWN): [ 'ip', show_ip ]
  },
  'ip': {
    (1 << lcd.SELECT): [ 'date', show_date ],
    (1 << lcd.DOWN): [ 'date', show_date ]
  }
}

if __name__ == '__main__':
	main()

