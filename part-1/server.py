from socket import *
import sys 

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
port = 5000
serverSocket.bind( ("",port))
serverSocket.listen()
print("Yash's server is listening on port: ", port)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message =  connectionSocket.recv(4096).decode()  
        filename = message.split()[1]
        f = open(filename[1:])                        
        outputdata = f.read();          
        # print("sending data: \n"+ outputdata)
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 NOT FOUND\r\n".encode())
        #Close client socket
        connectionSocket.close()
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data                                    