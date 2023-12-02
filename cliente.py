import socket
import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

# Configuración del lector PN532
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, reset=DigitalInOut(board.D6))
pn532.SAM_configuration()

# Configuración del cliente
server_address = 'ip_del_servidor'  # Reemplaza con la IP del servidor
server_port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_address, server_port))

print(f"Conectado al servidor en {server_address}:{server_port}")
while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is not None:
        uid_str = ''.join([hex(i)[2:] for i in uid])
        print("Tarjeta detectada con UID:", uid_str)

        # Enviar el UID al servidor
        client_socket.send(uid_str.encode())