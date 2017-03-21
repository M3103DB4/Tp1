from socket import *

serverPortIN = 12000
serverPortOUT = 13000
serverName = "localhost"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPortOUT))

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPortIN))
serverSocket.listen(1)

while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	modifiedSentence = sentence.upper()
	clientSocket.send(modifiedSentence)
	connectionSocket.close()

clientSocket.close()

   

