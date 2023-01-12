import json as js
import socket #Librerias para utilizar Sockets
#Nombre del servidor
serverName = "localhost"
# ServerPort corresponde al puerto por donde escucha el servidor
serverPort = 12000
#Se instancia un cliente socket de tipo UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Extrae del teclado una palabra escrita por el cliente
#message = input("Introduzca una palabra: ")

while True:

    def adds():
        tipo = input("""Introduza el tipo con el cual usted se dientifica:

                     1) Abstencionista
                     2) Belicoso
                     3) Capo 
                     4) Fascista
                     5) Izquierda
                     6) Indeciso \n
                     : """)


        dic = { "header": 1,
                "tipo": tipo ,
                }

        stdic = js.dumps(dic)

        # Send message to server
        client_socket.sendto(stdic.encode("utf-8"),(serverName, serverPort))

        print('*******************************')
        print("Respuesta guardada con exito! ")
        print('*******************************')



    def reports():
        dic = { "header" : 2,
                "dc" : 1}
        msg = js.dumps(dic)

        client_socket.sendto(msg.encode("utf-8"),(serverName, serverPort))

        modifiedMessage, serverAddress = client_socket.recvfrom(2048)

        dic = js.loads(modifiedMessage)

        print("********Estadisticas**********")
        print("Abstencionistas: ", dic['C1'][0], (dic['C1'][0]/dic['C7'][0])*100, '%')
        print("Belicosos: ", dic['C2'][0], (dic['C2'][0]/dic['C7'][0])*100, '%')
        print("Capos: ", dic['C3'][0], (dic['C3'][0]/dic['C7'][0])*100, '%')
        print("Fascistas: ", dic['C4'][0], (dic['C4'][0]/dic['C7'][0])*100, '%')
        print("Izquierda", dic['C5'][0], (dic['C5'][0]/dic['C7'][0])*100, '%')
        print("Indecisos", dic['C6'][0], (dic['C6'][0]/dic['C7'][0])*100, '%')
        print("Total", dic['C7'][0])

        print('******************************')

        
    # Menu    
    print("""            *******************************************
            *                                         *
            *      Bienvenido al menu principal       *  
            *                                         *
            *******************************************

            Porfavor introduzca el numero de la opcion que desea seleccionar:
            
            1) Registrarse
            2) Generar reporte

            """)
    
    #Input
    message = input("Introduzca un numero: ")

    #Conditionals
    if(message == '1'):
        adds()

    elif (message == '2'):
        reports()

    else:
        print('Ingrese un numero dentro del rango')

    
    #client_socket.close()


