import socket
import threading

host = 'localhost'
port = 5050

connections = []

def handle_client(conn: socket.socket, addr: str) -> None:
    first_message = f"You {addr} have connected to the server..."

    conn.send(first_message.encode('utf-8'))

    conneciton = True
    while conneciton:
        try:
            recievedMsg = conn.recv(1024).decode('utf-8')

            if recievedMsg == "cls":
                connections.remove(conn)
                conneciton = False

            elif recievedMsg == None:
                pass

            else:
                print("Server side msg..: ", recievedMsg)
                broadcast(addr, recievedMsg)

        except Exception as E:
            print("hata...: " + str(E))
            conn.close()


def broadcast(addr: str, msg: str) -> None:
    
    fullMessage = "<" + str(addr) + "> " + msg
    for client in connections:
        client.send(fullMessage.encode('utf-8'))
    print("Server side..: ", fullMessage)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    print("Socket has been created.")
    socket.bind((host, port))
    socket.listen(2)
    
    while True:
        conn, addr = socket.accept()
        connections.append(conn)
        threading.Thread(target = handle_client, args = [conn, addr]).start()

        
        

