from socket import *
import time
import sys
from datetime import date
def ping(host, port):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    
   
    
    resps = []
    for seq in range(1,11):
        startingtime = time.time()
        message = 'ping'  + " " + str(seq) + " " + str(startingtime)
        
        
        try:
            
            print(message)
            clientSocket.sendto(message.encode(),(host,port))
            receivedmessage,server = clientSocket.recvfrom(4096)
            reply= receivedmessage.decode()
            endtime = time.time()
            RTT = endtime - startingtime
            reply1=str(reply)
            finalRTT=float(RTT)
            resps.append((seq, reply1, finalRTT))
        except:
            resps.append((seq, 'Request timed out', 0))
    clientSocket.close()
    return resps
if __name__ == '__main__':
	resps = ping('www.inria.fr', 9500)
	print(resps)


