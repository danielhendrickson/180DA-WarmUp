#will run on computer


import numpy as np
import csv
import sys
import time
import math
import datetime
import os
import paho.mqtt.client as mqtt
import time,logging
from pydub import AudioSegment
from pydub.playback import play


															#ALL PRINT STATMENTS ARE STILL IN THIS CODE


def on_message(client, userdata, message):                  #This entire block is intended to run when melodies are received from the server
															#it is the logic for which sound should be played through the speakers and also
															#publishes the correct answer (^,V,>) to the IMU.
															#It also handles the IMU info being sent back and then publishes "Correct" or "Incorrect" to the client
	clienttemp = mqtt.Client('tempclient')
	clienttemp.connect_async('test.mosquitto.org')		#subscribing using clienttemp so can publish in def of on_message
	clienttemp.loop_start()
	ans = ''
	message_string = str(message.payload.decode("utf-8"))  #changes input from bytes to string and cleans up for reading into array
	disallowed_characters = "'"
	for character in disallowed_characters:
		message_string = message_string.replace(character, "") #removes characters from the payload before converting to array
	disallowed_characters = '"'
	for character in disallowed_characters:
		message_string = message_string.replace(character, "")
	disallowed_characters = '['
	for character in disallowed_characters:
		message_string = message_string.replace(character, "")
	disallowed_characters = ']'
	for character in disallowed_characters:
		message_string = message_string.replace(character, "")
	disallowed_characters = '('
	for character in disallowed_characters:
		message_string = message_string.replace(character, "")
	disallowed_characters = ')'
	for character in disallowed_characters:
		message_string = message_string.replace(character, "")
	disallowed_characters = ' '
	for character in disallowed_characters:
		message_string = message_string.replace(character, "")
	arr = message_string.split(',')
	if arr[0] == 'A#3.wav':										#cases of receiving message from client
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'A#4.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'A3.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'A4.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'B3.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'B4.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'C#3.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'C#4.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'C3.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
			print('published')
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'C4.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'D#3.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'D#4.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'D3.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'D4.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'E3.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'E4.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'F#3.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'F#4.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'F3.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'F4.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'G#3.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'G#4.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'G3.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'G4.wav':
		# start countdown 3... 2... 1...
		time.sleep(3.05) #delay while countdown is shown
		sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
		play(sound)
		if arr[1] == 'A#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'A4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/A4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'B4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/B4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'C4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/C4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'D4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/D4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'E4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/E4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'F4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/F4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G#4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G#4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G3.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G3.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)
		elif arr[1] == 'G4.wav':
			sound = AudioSegment.from_wav('/Users/danielhendrickson/Desktop/Notes/G4.wav')
			play(sound)
			clienttemp.publish('ece180d/IMU', str(arr[2]), qos=1)

	elif arr[0] == 'Correct!':                             #cases of receiving message back from IMU
		ans = 'Correct'
		#display arr()
		clienttemp.publish('ece180d/test2', str(ans), qos=1)  #publishes to test2 in order to go back to server without calling itself
		print('pub')

	else:
		ans = 'Incorrect'
		#display arr()
		clienttemp.publish('ece180d/test2', str(ans), qos=1)  #publishes to test2 in order to go back to server without calling itself
		print('pub')

	clienttemp.loop_stop()				 #publish message back to server
	clienttemp.disconnect()




client = mqtt.Client('firstclient')
client.on_message = on_message
client.connect_async('test.mosquitto.org')
client.loop_start()

print('running')

while True:
	client.subscribe('ece180d/IMU2')
	client.subscribe('ece180d/test')



client.loop_stop()
client.disconnect()




#glove on right hand with palm facing down (IMU on back, wire on left side, long side towards fingers)

#proceed to status phase screen?



