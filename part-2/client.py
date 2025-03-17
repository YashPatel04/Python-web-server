#import socket module
from socket import *
import sys # In order to terminate the program

clientSocket = socket(AF_INET, SOCK_STREAM)

#Establish the connection
print('Trying to connect...')
clientSocket.connect(('localhost', 5000))      
print('Connected to the server successfully.')  

try:
    request = "GET /HelloWorld.html HTTP/1.1\r\n"
    request += "Host: localhost\r\n"
    request += "\r\n"  # Empty line to end headers

    clientSocket.send(request.encode())
    # response
    data = ""
    while True:
        temp = clientSocket.recv(8192).decode()
        if not temp:
            break
        data += temp
    
    print("Recieved response")

    array = data.split("\r\n\r\n", 1)
    if len(array) > 1:
        body = array[1]
        print(body)
    print("connection closed !!")

except Exception as e:
    print(f"Error: {e}")
finally:
    clientSocket.close()
sys.exit()