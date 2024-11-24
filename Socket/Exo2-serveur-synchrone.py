import socket

def start_server(host, port):
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Serveur en attente de connexion...")

    while True:
        conn, address = server_socket.accept()
        print(f"Connexion établie avec {address}")

        while True:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"Message reçu : {message}")
            
            if message.lower() == "bye":
                print("Le client a quitté la conversation.")
                conn.send("Déconnexion du client.".encode())
                conn.close()
                break  
            elif message.lower() == "arrete":
                print("Arrêt du serveur demandé.")
                conn.send("Arrêt du serveur.".encode())
                conn.close()
                server_socket.close()
                return  

            reply = f"Message reçu : {message}"
            conn.send(reply.encode())

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 3333
    start_server(host, port)
