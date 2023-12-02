import socket
import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

# Configuración del lector PN532
i2c = busio.I2C(board.SCL, board.SDA)