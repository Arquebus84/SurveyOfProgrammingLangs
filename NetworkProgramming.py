import socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Make stream-based socket that goes across the internet
mySocket.connect(('data.pr4e.org', 80)) # Extend this socket across and connect to a web server (sockets and Port 80)

# Request
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n' .encode() # Get the URL and return the HTTP/1.0\n\n and use .encode() to prepare the data to go across the internet
mySocket.send(cmd) # Send the data

while True: # While the character count is > 0
    data = mySocket.recv(512)   # Receive these 512 characters at a time
    if(len(data) < 1):         # Until the entire socket is closed, read this data
        break
    print(data.decode())       # decode the data, because it is coming from
mySocket.close()
