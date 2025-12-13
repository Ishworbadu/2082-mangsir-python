#DAY2


# task1
# import socket 

# domain = input( "enter the doamin name")

# try:
#     ip=socket.gethostbyname(domain)
#     print(f"domain:{domain}")
#     print(f"ip:{ip}")

# except socket.gaierror:
#     print("invalid domain or dns issue")



#PORT SCANNER
#task 2
import socket
target=input("enter ip or domain:")
# porty=0
# port=porty+1

for porty in range(1000):
    port=porty

    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(3)

    result=sock.connect_ex((target,port))

    if result==0:
        print(f"port {port} is open")
    else:
        print(f"port {port } is closed")

    sock.close()