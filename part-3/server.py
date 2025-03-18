from socket import *
import sys
import threading
import time

array = []

def handleConnect(sckt, addr):
    print(f"Accepted connection from {addr}")

    try:
        message = sckt.recv(4096).decode()  
        filename = message.split()[1]
        f = open(filename[1:])                        
        outputdata = f.read()

        sckt.send("HTTP/1.1 200 OK\r\n".encode())
        sckt.send("Content-Type: text/html\r\n".encode())
        sckt.send("\r\n".encode())

        sckt.send(outputdata.encode())
        sckt.send("\r\n".encode())

    except IOError:
        sckt.send("HTTP/1.1 404 NOT FOUND\r\n".encode())

    finally:
        sckt.close()

def main():
    mainServer = socket(AF_INET, SOCK_STREAM)
    port = 5000
    mainServer.bind(("", port))
    mainServer.listen()
    print(f"Yash's server is listening on port: {port}")

    while len(array) < 5:
        try:
            connection, addr = mainServer.accept()            
            newThread = threading.Thread(target=handleConnect, args=(connection, addr), name=f't{len(array)}')
            print(f"New Thread: {newThread.name}")
            array.append(newThread)
            newThread.start()
            array[:] = [t for t in array if t.is_alive()]

        except KeyboardInterrupt:
            print("Server Shutting down!")
            break

    mainServer.close()
    sys.exit()

if __name__ == "__main__":
    main()
