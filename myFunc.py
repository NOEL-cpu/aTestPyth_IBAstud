import socket
def tlen(str):
    return len(str)

def hypotenuse(a,b):
    c=(a**2+b**2)**0.5
    return c

def ipadress():
   # print(socket.gethostbyname(socket.gethostname()))
    return str(socket.gethostbyname(socket.gethostname()))



