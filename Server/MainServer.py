import socket
import Server.ServerLib as ServerLib

class Server:
    def __init__(self, host="127.0.0.1", port=50000):
        self.HOST=host
        self.PORT=port
        
