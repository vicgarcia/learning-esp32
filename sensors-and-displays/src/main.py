
# from machine import Pin, SoftI2C
# import ssd1306

# # ESP32 Pin assignment 
# i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# oled_width = 128
# oled_height = 64
# oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# oled.text('Hello, World 1!', 0, 0)
# oled.text('Hello, World 2!', 0, 10)
# oled.text('Hello, World 3!', 0, 20)
        
# oled.show()


# from components import OLED

# oled = OLED(22, 21)
# oled.text('hello Vic!', 0, 5)
# oled.text('welcome to esp32', 0, 25)
# oled.show()


from components import OLED, GPS
import time

oled = OLED(22, 21)

oled.text('hello Vic!', 0, 5)
oled.show()
time.sleep(3)


gps = GPS(17, 16)

while True:
    oled.clear()
    oled.text('doing gps', 0, 5)
    oled.show()
    time.sleep(2)

    oled.clear()

    location = gps.get_location()
    if location is not None:
        latitude, longitude = location
        oled.text(f"LAT {latitude[0]} {latitude[1]}", 0, 15)
        oled.text(f"LON {longitude[0]} {longitude[1]}", 0, 25)
        oled.show()
        time.sleep(5)

    else:
        oled.text('no reading', 0, 5)
        oled.show()
        time.sleep(5)

# >>> import micropyGPS
# >>> from machine import Pin, PWM, SoftI2C, UART
# >>> 
# '''
# from components import GPS
# gps = GPS(17, 16)
# loc = gps.get_lat_lon()
# print(loc)
# '''

# # >>> import micropyGPS

# '''
# from machine import Pin, PWM, SoftI2C, UART
# serial = UART(2, baudrate=9600, tx=17, rx=16)
# serial.read()
# ''''

# >>> from components import GPS
# >>> gps = GPS(17, 16)
# >>> gps.get_lat_lon()
