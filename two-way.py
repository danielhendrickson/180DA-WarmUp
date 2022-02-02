import paho.mqtt.client as mqtt
import numpy as np
import time,logging
# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connection returned result: "+str(rc))
  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  client.subscribe("ece180d/test", qos=1)

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
  if rc != 0:
    print('Unexpected Disconnect')
  else:
    print('Expected Disconnect')
# The default message callback.
# (won't be used if only publishing, but can still exist)

def on_message(client, userdata, message):
  print('Received message: "' + str(message.payload) + '" on topic "' +message.topic + '" with QoS ' + str(message.qos))
  print(count)

# 1. create a client instance.
client = mqtt.Client()
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
# 2. connect to a broker using one of the connect*() functions.
client.connect_async("test.mosquitto.org")
# client.connect("test.mosquitto.org", 1883, 60)
# client.connect("mqtt.eclipse.org")
# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()

count=1
while True: #runs forever break with CTRL+C
   client.publish('ece180d/test', float(np.random.random(1)), qos=1) 
   count +=1
   time.sleep(5)



client.loop_stop()
client.disconnect()