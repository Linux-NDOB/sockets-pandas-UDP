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
        tipo = input("Tipo vehiculo 1: Buseta, 2:Bus : ")
        modelo = input("Introduzca el modelo: ")
        capacidad = input("Introduzca la capacidad del vehiculo: ")

        dic = { "header": 1,
                "tipo": tipo ,
                "modelo": modelo,
                "capacidad": capacidad,
               }

        stdic = js.dumps(dic)

        # Send message to server
        client_socket.sendto(stdic.encode("utf-8"),(serverName, serverPort))

        print('*******************************')
        print("Registrado con exito: ")
        print('*******************************')


    def reports():
        dic = { "header" : 2,
                "dc" : 1}
        msg = js.dumps(dic)

        client_socket.sendto(msg.encode("utf-8"),(serverName, serverPort))

        modifiedMessage, serverAddress = client_socket.recvfrom(2048)

        dic = js.loads(modifiedMessage)

        print("********Estadisticas**********")
        print("Modelo anterior a 1995: ", dic['C1'])
        print("Modelo mayor a 1995 y capacidad menor que 35: ", dic['C2'])
        print("Bus modelo mayor a 1995 y capacidad mayor que 35: ", dic['C3'])
        print("Buseta con capacidad menor que 35: ", dic['C4'])
        print("Total vehiculos", dic['C5'])
        print('******************************')

        
    # Menu    
    print("""            *******************************************
            *                                         *
            *      Bienvenido al menu principal       *  
            *                                         *
            *******************************************
            
            Porfavor rellene los campos correctamente:

            1) Aniadir vehiculo
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


