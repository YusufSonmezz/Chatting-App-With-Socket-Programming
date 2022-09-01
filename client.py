from email import message
from pickle import FALSE
import socket
import threading

theSocket = socket.socket()

#####################
host = "localhost"
port = 5050
#####################

# Beggining Message
print("You have been accepted to the server. Please wait for the other user...")
#

def getMessage(connection: socket.socket)->None:
    loop = True
    while loop:
        recievedMessage = connection.recv(1024).decode('utf-8')

        if recievedMessage != None:
            print(recievedMessage)


def sendMessage(msg: str, connection: socket.socket)->None:
    connection.send(msg.encode('utf-8'))

theSocket.connect((host, port))

connection = True

while connection == True:
    threading.Thread(target = getMessage, args = [theSocket]).start()

    while True:
        message = input()

        sendMessage(message, theSocket)

        if message == 'cls':
            connection = False
            break

theSocket.close()
