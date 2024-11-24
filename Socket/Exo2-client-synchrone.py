import socket

def start_client(host, port):
    client_socket = socket.socket()
    client_socket.connect((host, port))
    
    print("Connexion au serveur établie. Tapez 'bye' pour quitter ou 'arrete' pour arrêter le serveur.")

    while True:
        message = input("Vous : ")
        client_socket.send(message.encode())
        
        # Recevoir la réponse du serveur
        reply = client_socket.recv(1024).decode()
        print("Serveur :", reply)
        
        # Vérifie les messages de protocole pour arrêter le client
        if message.lower() == "bye":
            print("Déconnexion du client.")
            client_socket.close()
            break
        elif message.lower() == "arrete":
            print("Arrêt du serveur.")
            client_socket.close()
            break

if __name__ == "__main__":
    host = 'localhost'
    port = 3333
    start_client(host, port)
