import time
from socket import *

# get destination ip address from user.
valid = False
while not valid:
    ip = input("Please enter destination IP Address: ")
    try:
        inet_pton(AF_INET,ip)
        break
    except error:
        print("\nEntered IP is not valid. ")
    

# the loop in which packets are sent to the destination is here
for pings in range(10):
    client = socket(AF_INET, SOCK_DGRAM)
    client.settimeout(1)
    message = 'dummy'
    
    addr = (ip, 25000)

    # we memorize the sent time here
    start = time.time()
    # we send the dummy bytes to destination here
    client.sendto(str.encode(message), addr)
    try:
        # we listen to receive packets from the destination here
        data, server = client.recvfrom(1024)
        # memorize the received time
        end = time.time()
        # calculate the difference between send time and receive time
        took = end - start
        print ("PING "+server[0] + " took "+ str(round(took*1000))+"ms")    
    except timeout:
        print ('REQUEST TIMED OUT')