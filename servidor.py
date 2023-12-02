import socket
# Configuración del servidor
host = '0.0.0.0'  # Escuchar en todas las interfaces de red
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
