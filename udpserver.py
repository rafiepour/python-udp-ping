print ("Please ALLOW this app in your firewall",end="\r")
#import the necessary libraries
import random
from socket import *
#defining the socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
#openning the socket
serverSocket.bind(('', 25000))
print ("Server is running on port 25000           ")
while True:
    #looking to receive packets
    message, address = serverSocket.recvfrom(1024)
    print("Packed Received: "+address[0])
    #sending a response for the received packet
    serverSocket.sendto(message, address) 