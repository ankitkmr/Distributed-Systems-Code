#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

import random

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))

arraySize = random.randrange(10,31)
print "ArraySize:",arraySize,"\n"
numbers = [random.randrange(10,100) for i in xrange(arraySize)]
print "Array to be sorted:",numbers,"\n"
i=0

if s.recv(1024) == "Thank you for connecting. Please send your arraySize":
		s.send(str(arraySize))
		print "Sending arraySize:", arraySize

while(i<arraySize):
	if s.recv(1024) == "next":
		s.send(str(numbers[i]))
		print "Sending index",i,":", numbers[i]
		i+=1

print "\nThe Sorted Array is :\n",s.recv(1024),"\n"
s.close                     # Close the socket when done