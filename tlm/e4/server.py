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

        
        #Create dataframe adding vehicle
        with open('data.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=jsage.keys())
            writer.writerow(jsage)

        #Read csv file with totals 
        dt = pd.read_csv('totals.csv')

        # If is empty creates a void dataframe
        if dt.empty:
            totals = {"codigo": 0,
                      "avaluo": 0,
                      "laagua": 0, 
                      "lacagua": 0, 
                      "laen": 0,
                      "lacen": 0,
                      "lant": 0,
                      "lact": 0,
                      "otras": 0,
                      }
                
            mtotals = json.dumps(totals)
            df = pd.DataFrame([totals])
            df.to_csv('totals.csv', index=False, header=True)

        dt = pd.read_csv('totals.csv')


        #From second dataframe
        c11= dt.loc[0,'C1']
        c22= dt.loc[0,'C2']
        c33= dt.loc[0,'C3']
        c44= dt.loc[0,'C4']
        c55= dt.loc[0,'C5']
        c66= dt.loc[0,'C6']
        c77= dt.loc[0,'C7']



        c1 = int(c11) 
        c2 = int(c22)
        c3 = int(c33)
        c4 = int(c44)
        c5 = int(c55)
        c6 = int(c66)
        c7 = int(c77)

        if typev == '1':
            c1 +=1
            c7 +=1
        elif typev == '2':
            c2 +=1
            c7 +=1
        elif typev == '3':
            c3 +=1
            c7 +=1
        elif typev == '4':
            c4 +=1
            c7 +=1
        elif typev == '5':
            c5 +=1
            c7 +=1
        elif typev == '6':
            c6 +=1
            c7 +=1
   
        #After conditionals creates an updated dictionary
        totals = {
                  "C1": c1,
                  "C2": c2,
                  "C3": c3, 
                  "C4": c4, 
                  "C5": c5,
                  "C6": c6,
                  "C7": c7
                }

        #Converts to dataframe and updates the csv file
        mtotals = json.dumps(totals)
        df = pd.DataFrame([totals])
        df.to_csv('totals.csv', index=False, header=True)


    elif (jsage['header'] == 2):
        dt = pd.read_csv('totals.csv')
        dtd = dt.to_dict('list')
        jdt = json.dumps(dtd)
        serverSocket.sendto(jdt.encode(),clientAddres)
 

 


