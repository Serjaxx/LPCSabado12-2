import socket

hostname = socket.gethostname()
print("hostname: " ,hostname)

ip1 = socket.gethostbyname(hostname)
print("ip: " ,ip1)
