import machine
from machine import I2C
from I2cLcd import I2cLcd
from LcdApi import LcdApi


class Lcd:
    def __init__(self, sda_pin: int, scl_pin: int, rows=4, columns=20, debug=False):
        sda = machine.Pin(sda_pin)
        scl = machine.Pin(scl_pin)
        self.debug = debug
        self.i2c = I2C(0, sda=sda, scl=scl, freq=400000)
        self.lcd = I2cLcd(self.i2c, self.get_address(), rows, columns)

        if debug:
            print('Lcd connected')

    def get_address(self):
        address = int(hex(self.i2c.scan()[0]), 16)
        if self.debug:
            print('I2C address: ' + str(address))
        return address

    def write(self, *args, **kwargs):
        self.lcd.putstr(*args, **kwargs)
        if self.debug:
            print('written: ' + str(args[0]))

    def clear(self):
        self.lcd.clear()
        if self.debug:
            print('cleared')
            
    def set_backlight(self, __value: bool):
        if __value:
            self.lcd.backlight_on()
        if not __value:
            self.lcd.backlight_off()
        if self.debug:
            print('backlight value: ' + __value)

