from socket import *
import sys 

serverSocket = socket(AF_INET, SOCK_STREAM)
port = 5000
serverSocket.bind( ("",port))
serverSocket.listen(1)
print("Yash's server is listening on port: ", port)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message =  connectionSocket.recv(4096).decode()  
        filename = message.split()[1]
        f = open(filename[1:])                        
        outputdata = f.read();          
        # print("sending data: \n"+ outputdata)
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
    except IOError:
        connectionSocket.send("HTTP/1.1 404 NOT FOUND\r\n".encode())
    finally:
        connectionSocket.close()
serverSocket.close()
sys.exit()                                  