import socket

def client():
    host="127.0.0.1"
    port=7000
    sock=socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendto("Send time",(host, port))
    print("The system time\n")
    res= sock.recvfrom(1024)
    print(res)
    
    

client()