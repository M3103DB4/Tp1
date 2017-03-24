from socket import *

serverPortIN = 12000
serverPortOUT = 13000
serverName = "localhost"


serverSocket1 = socket(AF_INET,SOCK_STREAM)
serverSocket2 = socket(AF_INET,SOCK_STREAM)
serverSocket1.bind(('',serverPortIN))
serverSocket2.bind(('',serverPortOUT))
serverSocket1.listen(1)
serverSocket2.listen(1)
while 1:
	connectionSocket1, addr = serverSocket1.accept()
	sentence1 = connectionSocket1.recv(1024)
	modifiedSentence = sentence1.upper()
	connectionSocket1.send(modifiedSentence)
	connectionSocket1.close()
	connectionSocket2, addr = serverSocket2.accept()
	connectionSocket2.send(modifiedSentence)
	connectionSocket2.close()
	print "reussir"

