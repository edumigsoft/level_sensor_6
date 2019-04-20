#
#
#
from machine import Pin
import const
import firebase

LED_STATUS = int(firebase.get(const.FIREBASE_LED_STATUS))
pin = Pin(const.LED_PIN, Pin.OUT, LED_STATUS)

def ledExec():
	
	global pin
	
	firebase.set(const.FIREBASE_LED_STATUS, int(LED_STATUS))
	pin.value(LED_STATUS)
#####################################################################

def ledOn():
	
	global LED_STATUS
	
	LED_STATUS = const.LED_ON
	ledExec()
	
	print("ledOn")
	print("\r\n")
#####################################################################

def ledOff():
	
	global LED_STATUS
	
	LED_STATUS = const.LED_OFF
	ledExec()
	
	print("ledOff")
	print("\r\n")
#####################################################################

def ledToggle():
	
	global LED_STATUS
	
	if LED_STATUS == const.LED_ON:
		LED_STATUS = const.LED_OFF
	else:
		LED_STATUS = const.LED_ON
	ledExec()
	
	print("ledToggle")
	print("\r\n")
#####################################################################
