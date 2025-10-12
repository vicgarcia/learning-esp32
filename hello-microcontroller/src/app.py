import time
from components import Button, RGBLED


class ColorCycleButton:

    def __init__(self):
        # button is on GPIO 4
        self.button = Button(4)
        # rgb led is on 13 (R), 12 (G), 14, (B)
        self.led = RGBLED(13, 12, 14)
        # sequence of functions to call
        self.sequence_index = 0
        self.sequence = [
            self.led.off,
            self.led.red,
            self.led.green,
            self.led.blue,
        ]

    def handler(self):
        if self.sequence_index < len(self.sequence) - 1:
            self.sequence_index += 1
        else:
            self.sequence_index = 0
        self.sequence[self.sequence_index]()

    def run(self):
        self.button.callback(self.handler)
        while True:
            time.sleep(1)
