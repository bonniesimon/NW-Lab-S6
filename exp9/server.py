import os, socket
from signal import signal, SIGPIPE, SIG_DFL
from datetime import datetime
host="127.0.0.1"
port=7000
sock=socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

sock.bind((host, port))
sock.listen(10)

def handle_client(sock, addr, i):
    while True:
        data =sock.recvfrom(1024)
        
        if not data:
            print("\nconnection with client " + str(i) + " broken\n")
            break
        now = str(datetime.now())
        sock.sendto(now,(host, port))
        signal(SIGPIPE, SIG_DFL)

       

                

def server():
    i=1
    while i<=10:
        c, addr=sock.accept()
        child_pid=os.fork()
        if child_pid==0:
                print("\nconnection successful with client " + str(i) + str(addr) + "\n")
                handle_client(c, addr, i)
                break
        else:
                i+=1

server()