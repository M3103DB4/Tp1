# Tp1-Client/Serveur UDP en Python Franck Durville

## 1)Code Client
=====
- Pour que ce programme codé en langage Python fonctionne , il a fallut le copié dans un editeur linux, rectifier quelques lignes de code puis l'enregistrer en .py pour pouvoir le lancer dans le terminal . Il est l'émeteur du message que l'on souhaite envoyé au serveur .

	from socket import *                                           
                                                                
	 serverName = 'hostname’  
	 serverPort = 12000                                             
	 clientSocket = socket(AF_INET, SOCK_DGRAM)                     
	 message = raw_input('Input lowercase sentence:’)               
	 clientSocket.sendto(message,(serverName, serverPort))          
	 modifiedMessage, serverAddress = clientSocket.recvfrom(2048)   
	 print modifiedMessage                                         
	 clientSocket.close()                                           


## 2)Code Serveur
=====
- Pour que ce programme codé en langage Python fonctionne , il a fallut le copié dans un editeur linux, rectifier quelques lignes de code puis l'enregistrer en .py pour pouvoir le lancer dans le terminal . Il est le récepteur du message envoyé par le client .

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)

## 3)Commande netcat en mode client(resp. serveur). 
=====
