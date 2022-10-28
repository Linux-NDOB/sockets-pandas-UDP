import json
import serial
import paho.mqtt.client as mqtt 

broker_address="172.19.0.1" 
client = mqtt.Client("arduino") 
client.connect(broker_address) #connect to broker
 
connection = serial.Serial(port="/dev/ttyACM0", baudrate=115200)
connection.reset_input_buffer()
 
while True:

    data = connection.readline().rstrip().decode('utf-8')
    #print(data)

    try:

        dlist = json.loads(data)

        hrate = dlist[0]
        rrate = dlist[1]
        oxigen = dlist[2]
        temp = dlist[3]
        
        #pub = '{ "heartrate": {}, "resp_rate": {}, "oxigen": {}, "temp": {} }'.format(hrate, rrate, oxigen, temp)
        #print(type(dict_json))
        pub = { "hrate" : hrate, "rrate": rrate, "oxigen": oxigen, "temp": temp }
        jpub = json.dumps(pub)
        client.publish("ehealth", jpub )#publish

    except json.JSONDecodeError as e:

        print("JSON:", e)




#broker_address="iot.eclipse.org" #use external broker
#client = mqtt.Client("arduino") #create new instance
#client.connect(broker_address) #connect to broker
#client.publish("ehealth",'{ "temperature": 45, "oxigen": 95, "heart_rate": 100}')#publish
