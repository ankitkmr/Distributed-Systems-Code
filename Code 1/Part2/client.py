import xmlrpclib
import random
from heapq import *

numberServers = int(raw_input("Enter the number of Servers Available. For Default Number (5) - Simply press Enter: ") or "5")
print "Number of Servers Available: ", numberServers

#Registry of Servers
servers = []

for i in xrange(numberServers):
	servers.append((xmlrpclib.ServerProxy('http://localhost:800'+str(i+1)),i))

arraySize = random.randrange(0,100,numberServers)
numbers = [random.randrange(1,100) for i in xrange(arraySize)]
print "ArraySize: ", arraySize
print "Array to be sorted: \n", numbers

#Sending the pieces of numbers array to the servers
#Each Server Automatically sorts the array piece that it receives
workload = [server[0].setInstance(numbers[server[1]*arraySize/numberServers:(server[1]+1)*arraySize/numberServers]) for server in servers]

FinalArray = []
minheap = []
count = numberServers
index = 0
i=0

if all(signal=="Done" for signal in workload):
	print "All servers Completed Sorting"
	for server in servers:
		temp1 = server[0].get_smallest()
		print "Getting smallest number from Server ID-", "\b",server[1], "::", temp1
		heappush(minheap,(temp1,server[1]))
	
	while True:
		if count ==numberServers:
			temp1=heappop(minheap)
			FinalArray.append(temp1[0])
			index+=1
			count-=1
			i = temp1[1]
		else:
			server = servers[i] 
			temp2 = server[0].get_smallest()

			if temp2=="Empty" and index<arraySize:
				temp1=heappop(minheap)
				FinalArray.append(temp1[0])
				index+=1
				count-=1
				i = temp1[1]
			else:
				print "Getting smallest number from Server ID-", "\b",server[1], "::", temp2
				heappush(minheap,(temp2,i))
				count+=1

		if index == arraySize:
			break

print "\nThe Sorted Array is :\n", FinalArray


