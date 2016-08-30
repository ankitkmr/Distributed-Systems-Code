import sys

with open("config.txt","w") as f:
	f.write("[file]\n")
	for i in xrange(1,2*int(sys.argv[1]),2):
		f.write(str((i+1)/2)+" = 127.0.0.1:"+str(8050+i)+"\n")

with open("Makefile","w") as f:
	f.write("all:\n")
	for i in xrange(1,int(sys.argv[1])+1):
		f.write("\tpython clock.py config.txt "+str(i)+" "+sys.argv[1]+" &\n")