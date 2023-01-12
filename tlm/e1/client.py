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

    def datos():
        identificacion = input("Introduzca su cedula: ")
        pnombre = input("Introduzca su nombre: ")
        snombre = input("Introduzca su segundo nombre: ")
        categoria = input("Introduzca la categoria a inscribirse: ")
        cilindraje = input("Introduzca el cilindraje de su moto: ")
        

        cat = categoria

        cil = int(cilindraje)

        if cil > 1 and cil <= 100 :
            categoria = "Primera"

        elif cil >= 101 and cil <= 250 : 
            categoria = "Segunda" 

        elif cil >= 251 and cil <= 350 :
            categoria = "Tercera" 

        elif cil >= 351 and cil <= 500 :
            categoria = "Cuarta" 

        elif cil > 500 :
            categoria = "Quinta" 


        if cat == categoria :
            print("la categoria corresponde")
            print('')
            print('')

        else:
            categoria = categoria
            print("la categoria no corresponde, se ha ajustado a la que le corresponde: ", categoria) 
            print('')
            print('')

        dic = {
                "id": identificacion,
                "pnom": pnombre,
                "snom": snombre,
                "cat": categoria,
                "cil": cilindraje
                }

        stdic = js.dumps(dic)


        client_socket.sendto(stdic.encode("utf-8"),(serverName, serverPort))

        print('*******************************')
        print("Registrado con exito con Cedula: " ,identificacion )
        print("Registrado con exito con Nombre: " , pnombre)
        print('Estadisticas de los participantes: ')
        print('')




    # Menu    
    print("""            *******************************************
            *                                         *
            *      Bienvenido al menu principal       *  
            *                                         *
            *******************************************
            
            Porfavor ingrese el numero 1 para realizar las siguientes funciones:

            1) Ingresar una motocicleta
            2) Ver la cantidad de participantes por categoria
            3) Ver el total de participantes""")
    

    message = input("Introduzca el numero 1: ")



    if(message == '1'):
        print('seleccionado 1')
        datos()

    else:
        print('Ingrese un numero uno')



    #Se envia por el cliente socket el texto cargado a la variable message y se
    #decodifica en formato uft-8
    #client_socket.sendto(message.encode("utf-8"),(serverName, serverPort))
    #La variable modifiedMessage extrae del cliente socket el mensaje
    modifiedMessage, serverAddress = client_socket.recvfrom(2048)
    #El mensaje es mostrado por pantalla
    print (modifiedMessage)
    #Se cierra la conexión al socket
    client_socket.close()


