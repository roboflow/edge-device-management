import socket
from time import time

msgFromClient       = str(time())
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 8080)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while(True):
    start_time = time()
    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])

    print(msg)
    print("time to execute ==> ", time() - start_time)

'''
AGX Stats:
- prediction speed internal = 22 miliseconds
- total end-to-end = 45 miliseconds
TODO:
- deploy script
- headless mode deployment
- port forwarding to camera controller application
'''
