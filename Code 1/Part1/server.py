import socket               # Import socket module

class Thread(object):
	def __init__(self,(client,addr)):
		self.client = client
		self.addr = addr
		self.arraySize = 0
		self.array = []
		self.k=0
		self.flag = 0


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

numberClients = int(raw_input("Enter the Number of Clients to be registered:  "))
s.listen(numberClients)                 # Now wait for client connection.
client_num = 0
clients = []
while True:
	clients.append(Thread(s.accept()))     # Establish connection with client.
	client_num+=1
	print 'Got connection from', clients[-1].addr
	clients[-1].client.send('Thank you for connecting. Please send your arraySize')


	if client_num == numberClients:
		#All Clients have registered
		sorted(clients, key=lambda c:c.addr)	#Sorting Clients by their IP address
		
		#Registering all clients arraySize 
		for c in clients:
			c.arraySize = int(c.client.recv(1024))
			print "Received arraySize :",c.arraySize,"from :", c.addr
	
		while True:
			for c in clients:
				if c.arraySize>c.k:
					c.client.send("next")
					num = int(c.client.recv(1024))
					print "Got ", num, "from :", c.addr
					c.array.append(num)
					c.k+=1
				else:
					if c.flag==0:
						c.array.sort()
						print "Last Item Received from :", c.addr
						print "Sorting Array"
						c.client.send(str(c.array))
						print "Sending Sorted Array to:", c.addr
						c.flag = 1
						print "Closing Connection with:", c.addr
						c.client.close()		#close the connection

			if all(c.flag==1 for c in clients):
				clients = []
				client_num = 0
				numberClients = int(raw_input("Enter the Number of New Clients to be registered:  "))
				print "Server Reset"
				break


