import socket
    
def main(host, port, reply):
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Serveur en attente de connexion...")    
    conn, address = server_socket.accept()
    print(f"Connexion établie avec {address}")
    
    data = conn.recv(1024).decode()
    print("Données reçues : " + data)

    conn.send(reply.encode())
    
    
if __name__ == "__main__":
    host = '0.0.0.0'    
    port = 3333
    reply = "Hello client"
    main(host, port, reply)
    