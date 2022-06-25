from gpiozero import PWMLED, MCP3008
from time import sleep

pot = MCP3008(channel=0)
led = PWMLED(17)

while True:
    brightness = round(pot.value,1)
    print(brightness)
    led.value = brightness
    sleep(0.1)
