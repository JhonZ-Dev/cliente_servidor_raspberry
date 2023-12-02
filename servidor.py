import socket
# Configuración del servidor
host = '0.0.0.0'  # Escuchar en todas las interfaces de red
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)  # Permitir hasta 5 conexiones simultáneas


print(f"Esperando conexiones en {host}:{port}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida desde {client_address}")

