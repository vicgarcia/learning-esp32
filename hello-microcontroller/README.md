
Let's start the hello world, An LED.

```
from machine import Pin

class LED:

    # the onboard LED is on GPIO pin 2
    def __init__(self, pin_number=2):
        self.pin = Pin(pin_number, Pin.OUT)
        self.state = 0
        self._update()

    def _update(self):
        self.pin.value(self.state)

    def on(self):
        self.state = 1
        self._update()

    def off(self):
        self.state = 0
        self._update()

    def toggle(self):
        self.state = 1 if self.state == 0 else 0
        self._update()
```

GPIO pins are numbered. The pin can accept input or provide output.

In the constructor, `Pin` is created and set for output with `Pin.OUT`. The output is set with the `value` method. Setting this value to `1` or `0` toggles the LED on and off.

There's one block that's interesting.

```
    # the onboard LED is on GPIO pin 2
    def __init__(self, pin_number=2):
        self.pin = Pin(pin_number, Pin.OUT)
```

On ESP32 boards, the GPIO 2 pin will have an onboard LED. For our implementation, we'll default to `2` for the pin number is not specified, which gives easy access to the onboard LED.

In the micropython REPL

```
>>> from components import LED
>>> led = LED()
>>> led.toggle()
>>> led.toggle()
>>> led.toggle()
```

The output being toggling of the onboard LED.

On boot, the micropython firmware executes `boot.py` then `main.py`.

In `main.py`, the `LED` is created along with a `Timer`. This is used to execute the `handler` function at 2-second intervals to make the onboard LED blink.

```
from machine import Timer
from components import LED

led = LED()

def handler(*args):
    led.toggle()

timer = Timer(0)
timer.init(freq=2, mode=Timer.PERIODIC, callback=handler)
```

A RGB LED is essentially 3 LEDs in one; red, green, and blue.

Pulse wave modulation (PWM)

In `app.py`, the `ColorCycleButton` class

