from machine import Timer
from components import OnboardLED, Button, RGBLED


# make the LED on the board blink
# led = OnboardLED()
# timer = Timer(0)
# timer.init(freq=2, mode=Timer.PERIODIC, callback=led.toggle)


# cycle red/blue/green/off led when pressing the button
from app import ColorCycleButton

color_cycle_button_app = ColorCycleButton()
color_cycle_button_app.run()


# cycle red / green / blue / off with button and rgb led
# rgb_led = RGBLED(13, 12, 14)

# rgb_sequence = ['red']
# sequence_index = 0
# sequence_colors = [
#     (0, 0, 0)
# ]

# def handler(pin):



#     led.toggle()
#     print('button pressed')
#     print(pin)

# button = Button(4, pull_up=False)
# button.callback(handler)


# import time

# while True:
#     time.sleep(1)




