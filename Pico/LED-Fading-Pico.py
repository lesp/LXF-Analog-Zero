from gpiozero import PWMLED
from time import sleep
import serial
import struct

led = PWMLED(17)
port = "/dev/ttyACM0"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

while True:
    brightness = s.readline()
    brightness = (brightness)
    brightness = brightness[2:5]
    brightness = float(brightness)
    brightness = brightness/10
    print(brightness)
    led.value = brightness
    sleep(0.1)
