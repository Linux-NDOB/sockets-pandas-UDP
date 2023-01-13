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
        codigo = input('Ingrese el codigo del usuario: ')
        avaluo = input('Ingrese el avaluo de la propiedad: ')
        laagua = input('Ingrese lectura anterior del agua: ')
        lacagua = input('Ingrese lectura actual del agua: ')
        laen = input('Ingrese lectura anterior de energia:  ')
        lacen = input('Ingrese lectura actual de energia: ')
        lant = input('Ingrese lectura anterior del telefono: ')
        lact = input('Ingrese lectura actual del agua: ')
        otras = input('Ingrese el valor de otras entidades: ')


        dic = {
                "header": 1,
                "codigo": codigo ,
                "avaluo": avaluo,
                "laagua": laagua,
                "lacagua": lacagua,
                "laen": laen,
                "lacen": lacen,
                "lant": lant,
                "lact": lact,
                "otras": otras,
                }

        stdic = js.dumps(dic)

        # Send message to server
        client_socket.sendto(stdic.encode("utf-8"),(serverName, serverPort))

        print('*******************************')
        print("Respuesta guardada con exito! ")
        print('*******************************')
 
        
        modifiedMessage, serverAddress = client_socket.recvfrom(2048)

        dic = js.loads(modifiedMessage)

        print("********Estadisticas**********")
        print("Codigo: ", dic['codigo'])
        print("Aseo: ", abs(dic['aseo']))
        print("Agua: ", abs(dic['agua']))
        print("Energia: ", abs(dic['energia'])
        print("Telefono", abs(dic['telefono']))
        print("Total", dic['total'])
        print("Otros", dic['otras'])

        print('******************************')

        
    # Menu    
    print("""            *******************************************
            *                                         *
            *      Bienvenido al menu principal       *  
            *                                         *
            *******************************************

            Porfavor introduzca el numero de la opcion que desea seleccionar:
            
            1) Ingresar un registro
            
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


