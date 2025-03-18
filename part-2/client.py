from socket import *
import sys 

clientSocket = socket(AF_INET, SOCK_STREAM)

print('Trying to connect...')
clientSocket.connect(('localhost', 5000))      
print('Connected to the server successfully.')  

try:
    request = "GET /HelloWorld.html HTTP/1.1\r\n"
    request += "Host: localhost\r\n"
    request += "\r\n"  

    clientSocket.send(request.encode())
    # response
    data = ""
    while True:
        temp = clientSocket.recv(8192).decode()
        if not temp:
            break
        data += temp
    
    print("Recieved response")

    status_line = data.split('\r\n')[0]
    print(f"Status: {status_line}")

    if status_line.__contains__("200"):
        array = data.split("\r\n\r\n", 1)
        if len(array) > 1:
            body = array[1]
            print(body)
        print("connection closed !!")
    else:
        print("404: object not found.")
    

except Exception as e:
    print(f"Error: {e}")
finally:
    clientSocket.close()
sys.exit()