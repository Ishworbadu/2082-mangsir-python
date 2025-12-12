#DAY 1

import socket

# to print hostname and hostip
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)
print("your hostname:",hostname)
print("your ip address",ip)


import socket
domain=input("enter domain")
ip=socket.gethostbyname(domain)
print("ip is:",ip)