# Libraries
import json
import serial
import paho.mqtt.client as mqtt 
import time

# MQTT variables
broker_address="172.19.0.1" 
client = mqtt.Client("arduino2") 
client.connect(broker_address) #connect to broker
 
# Arduino ports 
connection = serial.Serial(port="/dev/ttyUSB0", baudrate=115200)
connection.reset_input_buffer()

connection2 = serial.Serial(port="/dev/ttyACM1", baudrate=115200)
connection.reset_input_buffer()

 
while True:
    try:
        # Read por USB0/Arduino UNO
        data = connection.readline().decode('utf-8')
        connection.reset_input_buffer()


        # Parse data
        dlist = json.loads(data)

        #Sensor readings
        weight = dlist[0]

        height = dlist[1]
        print(dlist[0], dlist[1])
        #time.seleep(0.5)

        # ACM0/Arduino ZERO
        data2 = connection2.readline().decode('utf-8')
        connection.reset_input_buffer()

        #ACM0
        dlist2 = json.loads(data2)

        hrate = dlist2[0]
        rrate = dlist2[1]
        oxigen = dlist2[2]
        temp = dlist2[3]
        #time.sleep(0.5)
        
        # UPLOAD TO SERVER 
        pub = { "hrate" : hrate, "rrate": rrate, "oxigen": oxigen, "temp": temp, "weight" :weight,"height": height }
        # TO JSON
        jpub = json.dumps(pub)
        client.publish("ehealth", jpub )#publish
        print('sent')
    # EXCEPTIONS
    except json.JSONDecodeError as e:

        print("JSON:", e)

    except IndexError:
        dlist = 'null'
     
    except Exception as e:
        print("Unicode Error")


