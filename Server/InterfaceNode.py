import socket, time, threading

#This is the type of node a client will initially connect to when connecting to this service. 
#It is responsible for taking client connection requests, and then sending their requests to appropriate nodes

mode = "Interface"

class Interface:
    #Broadcast settings
    broadcastAddr="255.255.255.255" 
    broadcastPort=50000
    broadcastMsg = "Looking for Host".encode("utf-8")

    broadcastSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcastSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    broadcastSocket.sendto(broadcastMsg, (broadcastAddr, broadcastPort))

    responseBuffer_Size = 1024

    while True:
        try :
            response, senderAddress = broadcastSocket.recvfrom(responseBuffer_Size)
        except socket.timeout as e:
            print("The socket timed out with this message:" +e)
            pass
        time.sleep(1)