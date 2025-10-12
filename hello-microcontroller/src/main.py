
# make the LED on the board blink

# from machine import Timer
# from components import OnboardLED

# led = OnboardLED()

# timer = Timer(0)

# def handler(*args):
#     led.toggle()

# timer.init(freq=2, mode=Timer.PERIODIC, callback=handler)


# toggle the LED on the board with the button

# import time
# from components import Button, OnboardLED

# led = OnboardLED()

# def handler():
#     led.toggle()

# button = Button(4, pull_up=False)
# button.callback(handler)

# while True:
#     time.sleep(1)


# cycle LED red/blue/green/off when pressing the button

from app import ColorCycleButton

color_cycle_button_app = ColorCycleButton()
color_cycle_button_app.run()
