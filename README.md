# Readme.md

Este es un proyecto de Python que utiliza un lector de tarjetas PN532 para leer los identificadores únicos (UID) de tarjetas NFC y enviarlos a un servidor a través de una conexión TCP. El servidor espera conexiones y recibe los UID de los clientes.

## Configuración del Lector PN532

El código utiliza la biblioteca `adafruit_pn532` para interactuar con el lector de tarjetas PN532 a través de la interfaz I2C. Asegúrate de tener instalada esta biblioteca antes de ejecutar el código. Puedes instalarla usando el siguiente comando:

```bash
pip install adafruit-circuitpython-pn532
```

La configuración del lector PN532 se realiza de la siguiente manera:

```python
import socket
import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

# Configuración del lector PN532
i2c = busio.I2C(board.SCL, board.SDA)  # Configurar la interfaz I2C
pn532 = PN532_I2C(i2c, reset=DigitalInOut(board.D6))  # Crear instancia del lector PN532
pn532.SAM_configuration()  # Configurar el lector para la lectura de tarjetas
```

## Configuración del Cliente

Antes de ejecutar el cliente, asegúrate de conocer la dirección IP del servidor al que te conectas y reemplaza `'ip_del_servidor'` con la dirección IP correspondiente. El código del cliente se encarga de conectar al servidor a través de una conexión TCP:

```python
# Configuración del cliente
server_address = 'ip_del_servidor'  # Reemplaza con la IP del servidor
server_port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crear un socket TCP
client_socket.connect((server_address, server_port))  # Conectar al servidor
```

## Configuración del Servidor

El servidor espera conexiones en todas las interfaces de red (`'0.0.0.0'`) en el puerto `12345`. Asegúrate de tener el puerto correctamente configurado y accesible. El código del servidor se configura de la siguiente manera:

```python
import socket

# Configuración del servidor
host = '0.0.0.0'  # Escuchar en todas las interfaces de red
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)  # Permitir hasta 5 conexiones simultáneas
```

## Ejecución del Proyecto

1. Configura el servidor con la dirección IP y el puerto deseados.
2. Ejecuta el servidor antes que el cliente.
3. Ejecuta el cliente y observa las conexiones y datos recibidos en la consola.

¡Listo! Ahora deberías estar recibiendo los UID de las tarjetas NFC en el servidor cuando se detectan en el lector PN532.
