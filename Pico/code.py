import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.A0)


def get_voltage(pin):
    return (round(pin.value / 65536,1))


while True:
    print(get_voltage(analog_in))
    time.sleep(0.1)
