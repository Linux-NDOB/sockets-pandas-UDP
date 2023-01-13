import csv

import pandas as pd

from socket import *
serverPort = 12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
import json
serverSocket.bind(("",serverPort))

print("""
      State: on
      """)

while True:
    message, clientAddres=serverSocket.recvfrom(2048)
             
    msage= message.decode()

    jsage = json.loads(msage)

    if( jsage['header'] == 1):

        cod = int(jsage['codigo'])
        av = int(jsage['avaluo'])
        laa = int(jsage['laagua'])
        laca = int(jsage['lacagua'])
        lae = int(jsage['laen'])
        lace = int(jsage['lacen'])
        lat = int(jsage['lant'])
        lact = int(jsage['lact'])
        ot = int(jsage['otras'])

        aseo = (1 * av)/100

        agua = (abs(laa) - abs(laca))*1000

        ener = (abs(lae) - abs(lace))*2000

        tel = (abs(lat) - abs(lact))*3000

        total = abs(aseo) + abs(agua) + abs(ener) + abs(tel) + abs(ot)


        #Create dataframe adding vehicle
        with open('data.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=jsage.keys())
            writer.writerow(jsage)

        #Read csv file with totals 
        dt = pd.read_csv('totals.csv')

        # If is empty creates a void dataframe
        if dt.empty:
            totals = {"codigo": cod,
                      "agua": agua,
                      "aseo": aseo, 
                      "energia": ener, 
                      "telefono": tel, 
                      "otras": ot,
                      "total": total,
                      }
                
            mtotals = json.dumps(totals)
            df = pd.DataFrame([totals])
            df.to_csv('totals.csv', index=False, header=True)

        dt = pd.read_csv('totals.csv')

        #After conditionals creates an updated dictionary
        totals = {
                  "codigo": cod,
                  "agua": agua,
                  "aseo": aseo, 
                  "energia": ener, 
                  "telefono": tel, 
                  "otras": ot,
                  "total": total
                }

        print('Resultado: ', totals)

        with open('totals.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=totals.keys())
            writer.writerow(totals)

        jdt = json.dumps(totals)

        serverSocket.sendto(jdt.encode(),clientAddres)


        #Converts to dataframe and updates the csv file
        #mtotals = json.dumps(totals)
        #df = pd.DataFrame([totals])
        #df.to_csv('totals.csv', index=False, header=True)


    elif (jsage['header'] == 2):
        dt = pd.read_csv('totals.csv')
        dtd = dt.to_dict('list')
        jdt = json.dumps(dtd)
        serverSocket.sendto(jdt.encode(),clientAddres)
 

 


