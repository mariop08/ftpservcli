# *************************************************************
# This program illustrates how to generate an emphemeral port
# *************************************************************

import socket

def generate_ephemeral():
    # Create a socket
    generated_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to port 0
    generated_socket.bind(('', 0))
    
    # Retrieve the ephemeral port number
    return generated_socket



