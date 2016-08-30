#!/usr/bin/python

import ConfigParser
import sys
import socket
import random
import time

if len(sys.argv)>4:
    raise TypeError("3 arguments are required - program_file, config_file, line_no :: " + str(len(sys.argv)) +" arguments given !!" )

configParser = ConfigParser.RawConfigParser()   
configFilePath = sys.argv[1]
configParser.read(configFilePath)

clientsNum=int(sys.argv[3])
try:
    client = configParser.get('file', sys.argv[2])
except:
    raise ValueError("Only "+ str(clientsNum) +" clients available currently.")

UDP_IP = client[:client.index(":")]
UDP_PORT = int(client[client.index(":")+1:])

sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(0)

output = open("output"+sys.argv[2]+".txt","w")
eventCount=0
timejump = random.randint(1,10)
timestamp=0

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.bind((UDP_IP, UDP_PORT+1))
sock1.listen(1000)

while True:
    try:
        #Receive Event
        dataPipe = []
        while True:
            dataPipe.append(sock.recvfrom(1024)) # buffer size is 1024 bytes
    except:
        pass
    finally:
        for (data,addr) in dataPipe:
            timestamp = max(timestamp,int(data[data.index(":")+1:]))+1
            output.write("r "+data[:data.index(":")]+" "+data[data.index(":")+1:]+" "+str(timestamp)+"\n")

    if eventCount==50:
        print "I am "+sys.argv[2]+", I completed my 50 events, I am retiring now. Bye !!"
        output.write("Exiting")
        break

    event = random.randint(1,2)
    if event == 1:
        #Local Event
        eventCount+=1
        timestamp+=timejump
        output.write("l "+str(timestamp)+"\n")
    else:
        #Send Event
        time.sleep(0.02)
        eventCount+=1
        timestamp+=timejump

        clientID = random.randint(1,clientsNum)
        while clientID==int(sys.argv[2]):
            clientID = random.randint(1,clientsNum)

        ID = configParser.get('file', str(clientID))
        ID_IP = ID[:ID.index(":")]
        ID_PORT = int(ID[ID.index(":")+1:])

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.sendto(sys.argv[2] + ":"+str(timestamp),(ID_IP,ID_PORT))
            output.write("s "+str(clientID)+" " +str(timestamp)+"\n")
            s.connect((ID_IP,ID_PORT+1))
        except:
            print "I am "+sys.argv[2]+" It seems my partner "+str(clientID)+" has retired, I am going with it. Bye !!"
            output.write("I am "+sys.argv[2]+" It seems my partner "+str(clientID)+" has retired, I am going with it. Bye !!")
            break
        finally:
            s.close()
            

sock.close()
sock1.close()
