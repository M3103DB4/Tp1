# Tp1-Client/Serveur UDP en Python Franck Durville

## I)Code Client
=====
- Pour que ce programme codé en langage Python fonctionne , il a fallut le copié dans un editeur linux, rectifier quelques lignes de code puis l'enregistrer en .py pour pouvoir le lancer dans le terminal . Il est l'émeteur du message que l'on souhaite envoyé au serveur .

###Programme :

	from socket import *                                           
                                                                
	 serverName = 'hostname’  
	 serverPort = 12000                                             
	 clientSocket = socket(AF_INET, SOCK_DGRAM)                     
	 message = raw_input('Input lowercase sentence:’)               
	 clientSocket.sendto(message,(serverName, serverPort))          
	 modifiedMessage, serverAddress = clientSocket.recvfrom(2048)   
	 print modifiedMessage                                         
	 clientSocket.close()                                           


## II)Code Serveur
=====
- Pour que ce programme codé en langage Python fonctionne , il a fallut le copié dans un editeur linux, rectifier quelques lignes de code puis l'enregistrer en .py pour pouvoir le lancer dans le terminal . Il est le récepteur du message envoyé par le client .

###Programme :

	from socket import *
	serverPort = 12000
	serverSocket = socket(AF_INET, SOCK_DGRAM)
	serverSocket.bind(('localhost', serverPort))
	print "The server is ready to receive"

	while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.upper()
	print modifiedMessage 
	serverSocket.sendto(modifiedMessage, clientAddress)

## III)Commande netcat en mode client(resp. serveur)
=====

La commande Net cat est une commande pratique et assez simple. En UDP dans le terminal client il sufit de taper la commande
"nc -u localhost 12000".  En détail : nc = Netcat ; -u = UDP ; localhost= nom de la machine ; 12000=port

En ce qui concerne la partie Serveur il faut taper dans le Terminal la commande ""nc -l -u localhost 12000". On rajoute -l pour listen .

Pour communiquer avec d'autres machines il suffit de remplacer le "localhost" par l'adresse ip de la machine concerné .On l'obtient grâce à la commande ifconfig dans le terminal.
