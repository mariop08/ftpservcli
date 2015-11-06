__author__ = 'Mario Pena'

from ephemeral import generate_ephemeral


# Client requests file from server
def _get(control_socket, message_rec):
    # Grab the size of the file in a buff
    file_name_size_buff = rec_all(control_socket, 10)

    # Convert file name size into int
    file_name_size = int(file_name_size_buff)

    # Recieve the file name+extension
    file_name = rec_all(control_socket, file_name_size)

    # Generate ephemeral port
    eport = generate_ephemeral()

    # Get ephemeral port address
    eport_address = eport.getsockname()[1]

    # Get the length of the ephemeral port address
    eport_address_len = str(len(eport_address))

    # Prepend 0's to the size string
    # until the size is 10 bytes
    while len(eport_address_len) < 10:
        eport_address_len = "0" + eport_address_len

    # Put together length of port and port number
    eport_info = eport_address_len + eport_address

    # Send port info to client
    control_socket.send(eport_info)

    # Recieve confirmation information was received and status code
    status_buff = rec_all(control_socket, 10)

    status = status_buff.strip()

    if status == "200":
        # Open file to be sent
        fileObj = open(file_name, "rb")

        while True:
            # Read 65536 bytes of data
            fileData = fileObj.read(10000000)

            if fileData:

                # Get the size of the data read
                # and convert it to string
                dataSizeStr = str(len(fileData))

                # Prepend 0's to the size string
                # until the size is 10 bytes
                while len(dataSizeStr) < 10:
                    dataSizeStr = "0" + dataSizeStr

                num_sent = 0

                while len(fileData) > num_sent:
                    num_sent += eport.send(fileData[num_sent:])
            else:
                break

    # check if file transfer was successful
    status = rec_all(control_socket, 10)

    # close and destroy ephemeral port
    eport.close()


def _put(control_socket, message_rec):
    return 0


def _list(control_socket, message_rec):
    return 0;


def _quit(control_socket, message_rec):
    return 0;


def rec_all(sock, num_bytes):
    # The buffer
    recv_buff = ""

    # The temporary buffer
    temp_buff = ""

    # Keep receiving till all is received
    while len(recv_buff) < num_bytes:
        # Attempt to receive bytes
        temp_buff = sock.recv(num_bytes)

        if not temp_buff:
            break

    recv_buff += temp_buff

    return recv_buff
