import socket 
import threading 

port =5058
buffer=16
format= "utf-8"
disconnect = "end"

hostname= socket.gethostname()
host_ip= socket.gethostbyname(hostname)
server_address=(host_ip,port)

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server.setsockopt(socket.SOl_socket, socket.SO_REUSEADDR,1)
server.bind(server_address)
server.listen()
print("Server is listening")

def calc_sal(hr):
    if hr<=40:
        return hr*200
    else:
        return 8000+(hr-40)*300
    
def client_handle(conn,addr):
    connected= True
    while connected:
        msg_len=conn.recv(buffer).decode(format).strip()
        if msg_len:
            msg_len=int(msg_len)
            msg= conn.recv(msg_len).decode(format)

            if msg== disconnect:
                conn.send("Goodbye".encode(format))
                connected=False

            else:
                    hr=float(msg)
                    sal=calc_sal(hr)
                    if hr <=40:
                         response=(f"Hours Worked: {hr}\n"
                                   f"Rate: TK200/hr\n"
                                   f"Total Salary: tk {calc_sal(hr):.2f}")
                         
                    else:
                         overtime=hr-40
                         response=(f"Hours Worked: {hr}\n"
                                   f"Base pay: tk 8000(first 40 hr) \n)"
                                   f"Overtime pay: {overtime * 300:.2f}\n"
                                   f"Total Salary: tk {calc_sal(hr):.2f}")
                         
                    conn.send(response.encode(format))
    conn.close()


while True:
     conn, addr= server.accept()
     thread= threading.Thread(target=client_handle, args=(conn,addr))
     thread.start()


                      

             


