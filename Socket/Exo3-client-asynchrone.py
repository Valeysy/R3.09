import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            reply = client_socket.recv(1024).decode()
            if not reply:
                print("\nConnexion fermée par le serveur.")
                break
            print("\nServeur :", reply)
        except (ConnectionResetError, ConnectionAbortedError):
            print("\nConnexion perdue avec le serveur.")
            break
        except Exception as e:
            print(f"")
            break
    client_socket.close() 

def start_client(host, port):
    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
    except ConnectionRefusedError:
        print("Impossible de se connecter au serveur.")
        return
    
    print("Connexion au serveur établie. Tapez 'bye' pour quitter ou 'arrete' pour arrêter le serveur.")
    
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    
    while True:
        try:
            message = input("")
            client_socket.send(message.encode())
            
            if message.lower() == "bye":
                print("Déconnexion du client.")
                client_socket.close()
                break
            elif message.lower() == "arrete":
                print("Arrêt du serveur.")
                client_socket.close()
                break
        except (BrokenPipeError, ConnectionResetError):
            print("Connexion fermée, impossible d'envoyer des messages.")
            break
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            break

if __name__ == "__main__":
    host = 'localhost'
    port = 3333
    start_client(host, port)
