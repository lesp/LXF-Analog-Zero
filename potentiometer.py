from gpiozero import MCP3008, LED
from time import sleep

pot = MCP3008(channel=0)
led = LED(17)

while True:
    blink = round(pot.value,1)
    print(blink)
    led.toggle()
    sleep(blink*5)
