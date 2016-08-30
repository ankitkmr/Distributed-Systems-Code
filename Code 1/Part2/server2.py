from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from collections import deque

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8002),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

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

server.register_instance(Sorting())

# Run the server's main loop
server.serve_forever()