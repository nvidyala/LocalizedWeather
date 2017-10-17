#! /usr/bin/python
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27,GPIO.OUT)
try:
	while True:
		rain = GPIO.input(17)
		if rain: 
			print('No rain detected')
			GPIO.output(27,0)
		else: 
			print('Rain detected')
			GPIO.output(27,1)
			time.sleep(1)
			GPIO.output(27,0)
		time.sleep(2)

finally:
	GPIO.cleanup()
