from flask import Flask, request, render_template
import paho.mqtt.client as mqtt
import numpy as np
import json

app = Flask(__name__)

message_list = []
player_tiles = [[False]*15]*15

def button_callback(channel):
    print("Button was pushed!")
    
def sendButtonData(button):
    
    payload = json.dumps({
        button: True
    })
    
    client.publish("controlpanel/buttons", payload, qos=1)
    
    payload = json.dumps({
        button: False
    })
    
    client.publish("controlpanel/buttons", payload, qos=1)
    

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("topic")  # Subscribe to MQTT topic

def on_message(client, userdata, msg):
    global player_tiles
    # get convert the string to json
    if msg.topic == "player/pos":
        try:
            playerPos = json.loads(msg.payload)
            player_tiles = [[False for _ in range(15)] for _ in range(15)]
            x = int(playerPos["x"]) + 7
            y = int(playerPos["y"]) + 7
            player_tiles[x][y] = True
        except:
            print("Error reseving data from server. Please check game connection")
        
    print("Received message: " + msg.topic + " " + str(msg.payload))
    # Reload the page when a new message is received
    
    message_list.append("Received message: " + msg.topic + " " + str(msg.payload))

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("10.42.0.1", 1883, 60)  # Connect to MQTT broker
client.subscribe("player/pos")

# Flask routes
@app.route('/', methods=['GET', 'POST'])
def index():
                
    if request.method == 'POST':
        try:
            message = request.form['message']   # Get message from HTML form
            client.publish("topic", message, qos=1)  # Publish message to MQTT topic
        except:
            pass
        # check with button was pressed
        if button := request.form.get("but"):
            print(button)
            sendButtonData(str(button))

    return render_template('index.html', tiles=player_tiles)

@app.route('/messages', methods=['GET'])
def messages():
    # You can implement logic here to retrieve messages from a database or other storage
    # In this example, we simply return a static list of messages
    return render_template('messages.html', messages=message_list)

if __name__ == '__main__':
    client.loop_start()  # Start MQTT loop
    app.run(debug=True, port=5000)
