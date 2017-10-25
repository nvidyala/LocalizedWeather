import paho.mqtt.client as mqtt
import ast
import json
import os
import socket
import ssl
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc) )
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("reading/0001" , 1 )

def on_message(client, userdata, msg):
	json_string = json.loads(msg.payload)
	rain = json_string["Rain"]
	print(rain)
	if rain=='1':
		GPIO.output(27,1)
		sleep(1)
		GPIO.output(27,0)
		sleep(1)
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message


awshost = "a30yzo4z66lz12.iot.us-west-2.amazonaws.com"
awsport = 8883
clientId = "RPi"
caPath = "/home/pi/deviceSDK/VeriSign-Class3-Public-Primary-Certification-Authority-G5.pem"
certPath = "/home/pi/deviceSDK/65cbb92693-certificate.pem.crt"
keyPath = "/home/pi/deviceSDK/65cbb92693-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqttc.connect(awshost, awsport, keepalive=60)
mqttc.loop_forever()
