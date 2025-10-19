
## What You Need

The kit instructions provide some insight into the components. It has good information on the ESP32 and series of tutorials using the various components in the kit.

https://www.dropbox.com/scl/fo/6znlij3eb23ih4jxcpv2w/AKvB1t9CCUgoVRVtGen8Yrw?rlkey=z84anl0hs940qf9fpl7l8q8q2

## Getting Started

The first thing that needs to be done is to flash the micropython firmware to the board.

This is done with the [esptool.py]().

Install `esptool` in a virtual environment.

```
python3 -m venv .venv
.venv/bin/pip install esptool
```

https://docs.espressif.com/projects/esptool/en/latest/esp32/installation.html

Then download the appropriate MicroPython firmware

https://micropython.org/download/?port=esp32

The firmware for the board in the recommended kit

https://micropython.org/download/ESP32_GENERIC/

Install the firmware.

```
.venv/bin/esptool --baud 460800 write_flash 0x1000 ESP32_BOARD_NAME-DATE-VERSION.bin
```

Reboot the board with the boot button.

Then enter the REPL

```
picocom /dev/ttyUSB0 -b115200
```

You can exit with `ctrl` + `a` then `ctrl` + `x`

https://docs.micropython.org/en/latest/esp32/quickref.html

MPY Workbench extension for VS Code

### What You'll Need

### Installing


## Projects

### Hello Microcontroller

