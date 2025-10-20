from machine import Pin, PWM, SoftI2C, UART
import ssd1306
import micropyGPS


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


class RGBLED:

    def __init__(self,
        red_pin_number=0,
        green_pin_number=0,
        blue_pin_number=0,
        freq_hz=1000,
        max_duty=1023,
    ):
        self.freq_hz = freq_hz      # 1000Hz is standard for PWN
        self.max_duty = max_duty    # ESP32 uses 10bit PWM (0-1023)
        self._red = PWM(Pin(red_pin_number))
        self._red.freq(self.freq_hz)
        self._green = PWM(Pin(green_pin_number))
        self._green.freq(self.freq_hz)
        self._blue = PWM(Pin(blue_pin_number))
        self._blue.freq(self.freq_hz)
        self.set_color(0, 0, 0)

    def _calc_duty_cycle(self, color_value):
        # expects a color value from 0 - 255
        # converts to duty cycle for PWM
        return int((color_value / 255) * self.max_duty)

    def set_color(self, red, green, blue):
        self._red.duty(self._calc_duty_cycle(red))
        self._blue.duty(self._calc_duty_cycle(blue))
        self._green.duty(self._calc_duty_cycle(green))

    def off(self):
        self.set_color(0, 0, 0)

    def red(self):
        self.set_color(255, 0, 0)

    def white(self):
        self.set_color(255, 255, 255)

    def green(self):
        self.set_color(0, 255, 0)

    def blue(self):
        self.set_color(0, 0, 255)


class Button:

    def __init__(self, pin_number, pull_up=True):
        if pull_up:
            self.pin = Pin(pin_number, Pin.IN, Pin.PULL_UP)
            self.press_value = 0
        else:
            self.pin = Pin(pin_number, Pin.IN, Pin.PULL_DOWN)
            self.press_value = 1

    @property
    def pressed(self):
        return self.pin.value() == self.press_value

    def callback(self, callback_func):
        # wrap the callback function in a handler function to handle argument
        # this allows the callback function to disregard the argument
        def handler(pin):
            callback_func()
        # handler is a function that accepts an argument
        trigger = Pin.IRQ_FALLING if self.press_value == 0 else Pin.IRQ_RISING
        self.pin.irq(trigger=trigger, handler=handler)


class OLED:

    def __init__(self,
        scl_pin_number, 
        sda_pin_number,
        oled_width=128,
        oled_height=64,
    ):
        self.i2c = SoftI2C(
            scl=Pin(scl_pin_number),
            sda=Pin(sda_pin_number),
        )
        self.oled = ssd1306.SSD1306_I2C(
            oled_width,
            oled_height,
            self.i2c,
        )

    def text(self, message, x, y):
        self.oled.text(message, x, y)

    def pixel(self, x, y, color=1):
        # color is 0 = black, 1 = white
        self.oled.pixel(x, y, color)

    def show(self):
        self.oled.show()

    def clear(self):
        self.oled.fill(0)
        self.oled.show()


class GPS:

    def __init__(self,
        tx_pin_number,
        rx_pin_number,
        baudrate=9600,
    ):
        self.serial = UART(2, baudrate=baudrate, 
            tx=tx_pin_number,
            rx=rx_pin_number,
        )

    def get_parser(self, location_formatting='dd'):
        return micropyGPS.MicropyGPS(
            location_formatting=location_formatting,
        )

    def get_location(self):
        try:
            parser = self.get_parser()
            data = self.serial.read()
            for byte in data:
                stat = parser.update(chr(byte))
                if stat is not None:
                    latitude = parser.latitude
                    longitude = parser.longitude
                    return latitude, longitude
        except Exception as e:
            pass
