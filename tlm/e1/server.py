import csv

import pandas as pd

from socket import *
serverPort = 12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
import json
serverSocket.bind(("",serverPort))
print ("El servidor está listo para recibir peticiones")
while True:
      message, clientAddres=serverSocket.recvfrom(2048)
      #print ("mensaje recibido: "+message.decode())
      #modifiedMessage=(message.decode().upper())
      #print ("mensaje modificado: "+modifiedMessage)
             
      msage= message.decode()

      jsage = json.loads(msage)

      dt = pd.read_csv('totals.csv')

      t= dt.loc[0,'Total']
      f= dt.loc[0,'Primera']
      s= dt.loc[0,'Segunda']
      t= dt.loc[0,'Tercera']
      c= dt.loc[0,'Cuarta']
      q= dt.loc[0,'Quinta']


      firsts = int(f) 

      secs = int(s)

      thirds = int(t)

      fourth = int(c)

      fift = int(q)

      total = int(t)

      if jsage['cat'] == "Primera":
          firsts +=1
          total +=1 

      elif jsage['cat'] == "Segunda":
            secs +=1
            total +=1 

      elif jsage['cat'] == "Tercera":
            thirds +=1
            total +=1

      elif jsage['cat'] == "Cuarta":
            fourth +=1
            total +=1

      elif jsage['cat'] == "Quinta":
            fift +=1
            total +=1


      totals = { "Total": total,
                "Primera": firsts,
                "Segunda": secs, 
                "Tercera": thirds, 
                "Cuarta": fourth, 
                "Quinta" : fift }

      mtotals = json.dumps(totals)

      df = pd.DataFrame([totals])
      df.to_csv('totals.csv', index=False, header=True)

      with open('data.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=jsage.keys())
            writer.writerow(jsage)

      #print(df) 
      #print('')
      #val = df.loc[0,'Primera']

      #print('Primera: ', int(val))
      #print(message.decode())

      #serverSocket.sendto(msage.encode(), clientAddres)
      serverSocket.sendto(mtotals.encode(),clientAddres)
  #print("Se envió mensaje modificado al cliente") 

