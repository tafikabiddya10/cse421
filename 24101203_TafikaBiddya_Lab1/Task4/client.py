import socket

port =5058
buffer=16
format= "utf-8"
disconnect = "end"

hostname= socket.gethostname()
host_ip= socket.gethostbyname(hostname)
server_address=(host_ip,port)

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(server_address)

def mesegges(msg):
    msg= msg.encode(format)
    msg_length= str(len(msg)).encode(format)
    msg_length+=b" "*(buffer- len(msg_length))

    client.send(msg_length)
    client.send(msg)
    response= client.recv(2049).decode(format)
    print(response)
while True:
    inp= input("Enter hours worked or 'end' to disconnect: ").strip()

    if inp == disconnect:
        mesegges(inp)
        client.close()
        break
    else:
        mesegges(inp)