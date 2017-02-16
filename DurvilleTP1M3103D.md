# Tp1-Client/Serveur UDP en Python Franck Durville

## 1)Code Client
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)


## 2)Code Serveur


