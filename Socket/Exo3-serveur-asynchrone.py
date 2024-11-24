import socket
import threading

def handle_client(conn, address):
    print(f"Connexion établie avec {address}")
    conn_active = True  # Indicateur pour vérifier si la connexion est active
    
    def receive_messages():
        nonlocal conn_active
        while conn_active:
            try:
                message = conn.recv(1024).decode()
                if not message:
                    print("Client déconnecté.")
                    conn_active = False
                    break
                print(f"Message reçu : {message}")
                
                if message.lower() == "bye":
                    print("Le client a quitté la conversation.")
                    conn.send("Déconnexion du client.".encode())
                    conn_active = False
                    break
                elif message.lower() == "arrete":
                    print("Arrêt du serveur demandé.")
                    conn.send("Arrêt du serveur.".encode())
                    conn.close()
                    server_socket.close()
                    conn_active = False
                    return

            except (ConnectionResetError, ConnectionAbortedError):
                print("Connexion perdue avec le client.")
                conn_active = False
                break
            except Exception as e:
                print(f"Erreur inattendue lors de la réception : {e}")
                conn_active = False
                break
        conn.close()  # Fermer la connexion après la fin de la boucle
    
    def send_messages():
        nonlocal conn_active
        while conn_active:
            try:
                reply = input("")
                conn.send(reply.encode())
            except (BrokenPipeError, ConnectionResetError):
                print("Connexion fermée ou perdue, impossible d'envoyer des messages.")
                conn_active = False
                break
            except Exception as e:
                print(f"Erreur inattendue lors de l'envoi : {e}")
                conn_active = False
                break

    # Lancer les threads pour l'envoi et la réception des messages en parallèle
    threading.Thread(target=receive_messages, daemon=True).start()
    send_messages()  # Ce thread principal attend les entrées utilisateur

def start_server(host, port):
    global server_socket
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Serveur en attente de connexion...")

    while True:
        try:
            conn, address = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, address), daemon=True).start()
        except ConnectionAbortedError:
            print("Serveur arrêté.")
            break
        except Exception as e:
            print(f"Erreur inattendue dans le serveur : {e}")
            break

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 3333
    start_server(host, port)
