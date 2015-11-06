import socket
import platform
from functions import _get
from functions import rec_all

# The port on which to listen
listenPort = 1234

# Create a welcome socket.
welcomeSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
welcomeSock.bind(('', listenPort))

# Start listening on the socket
welcomeSock.listen(1)

# Determine the operating system that the server is running on
currentSystem = platform.system()

print currentSystem

# Accept connections forever
while True:
    print "Waiting for connections..."

    # Accept connections
    clientSock, addr = welcomeSock.accept()

    print "Accepted connection from client: ", addr
    print "\n"

    clientSock.send("Connection has been established")

    command = clientSock.rec_all(clientSock, 4)

    command = command.strip()

    while command != "QUIT":

        if command == "PUT":
            print "PUT"
        elif command == "GET":
            print "GET"
        elif command == "LIST":
            print "PRINT"
        else:
            clientSock.send("Undefined")













