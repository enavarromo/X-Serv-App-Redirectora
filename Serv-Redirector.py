#!/usr/bin/python
import socket
import random
import Cookie

# -------------- Global Variables --------------


# -------------- Port Set Up --------------
host = socket.gethostname()
port = 1234

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((host, port))  # Socket LoopBack Host
mySocket.listen(2) # 5 TPC Cons cap

# -------------- Main --------------
try:
    num = 0
    while True:
        (recvSocket, address) = mySocket.accept()
        Rx = recvSocket.recv(1024);
        print Rx
#        num = num + 1                      # Incremental
        num = random.randint(1, 1000) # Aleatorio

        recvSocket.send('HTTP/1.1 303 See Other\r\n'+
        "Location: http://ubuntu:1234/"+str(num)+"\r\n\r\n"        
        "</body></html>\r\n")

            
        recvSocket.close()
except KeyboardInterrupt:
    mySocket.close()
    print("\nExiting Ok")


# al 20 intento muere el navegador


# funciona con: http://ubuntu:1234/7
# lanzable con: http://ubuntu:1234
#        "Location: http://google.com\r\n\r\n"




 
