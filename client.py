import socket
from functions import _get, _put, _list, rec_all

# Server address
server_address = "localhost"

# Server port
serverPort = 1234

# Create a TCP socket
connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
#connSock.connect((server_address, serverPort))

while True:
    command = raw_input("ftp>")

    if len(command.split()) == 1:
        if command.split()[0] == "LIST":
            _list(connSock)
        elif command.split()[0] == "QUIT":
            break
        else:
            print "Incorrect Command"
    elif len(command.split()) == 2:
        if command.split()[0] == "GET":
            _get(connSock)

            # Get the length of the ephemeral port number
            len_eport_num = rec_all(connSock,10)

            # Get the actual ephemeral port number
            eport_num = rec_all(connSock, len_eport_num)

            esocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            esocket.connect(server_address, int(eport_num))

            file_size_buff = rec_all(esocket, 10)

            file_size = int(file_size_buff)

            f = open(command.split()[1], 'wb')

            file_data = rec_all(eport_num, file_size)

            f.write(file_data)

            f.close()
            esocket.close()
        elif command.split()[0] == "PUT":
            _put(connSock)
        else:
            print "Incorrect Command"
    else:
        print "Incorrect Command!"


