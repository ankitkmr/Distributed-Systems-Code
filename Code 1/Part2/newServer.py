from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from collections import deque
import os


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').
class Sorting:
	def setInstance(self,array):
		self.array = deque(array)
		self.sort()
		return "Done"

	def sort(self):
		 numbers = list(self.array)
		 numbers.sort()
		 self.array = deque(numbers)

	def get_smallest(self):
		if self.array:
			return self.array.popleft()
		else:
			return "Empty" 


def child(port):
	print('\nA new child server',  os.getpid())
	
	# Create server
	server = SimpleXMLRPCServer(("localhost", int(port)),
	                        requestHandler=RequestHandler)
	server.register_introspection_functions()
	server.register_instance(Sorting())
	# Run the server's main loop
	server.serve_forever()
	os._exit(0)  

def parent(numberServers):
	global PORT
	PORT = 8080
	while numberServers>0:
		newpid = os.fork()
		if newpid == 0:
			print "Starting Server on PORT:: " + str(PORT) + " !! \n"
			child(PORT)
		else:
			PORT+=1
			pids = (os.getpid(), newpid)
			print("Parent Server PID: %d, Child Server PID: %d\n" % pids)
		numberServers-=1
		
numberServers = int(raw_input("Enter the Number of Servers Available :: "))
parent(numberServers)


