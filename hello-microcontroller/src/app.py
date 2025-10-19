import time
from components import Button, RGBLED


class ColorCycleButton:

    def __init__(self,
        button_pin_number,
        red_pin_number,
        green_pin_number,
        blue_pin_number,
    ):

        # setup the button
        self.button = Button(button_pin_number)

        # setup the rgb led
        self.led = RGBLED(
            red_pin_number,
            green_pin_number,
            blue_pin_number,
        )

        # sequence of functions to call on button press
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
