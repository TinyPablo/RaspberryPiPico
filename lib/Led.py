from machine import Pin

class Led:
    def __init__(self, pin: int, debug=False):
        self.pin = pin
        self.debug = debug
        self.led = Pin(self.pin, Pin.OUT)

    def print_led_state(self):
        print('led on pin ' + str(self.pin) + ' is ' + ('ON' if self.led.value() else 'OFF'))

    def value(self, __value: bool):
        self.led.value(__value)
        if self.debug:
            self.print_led_state()

    def toggle(self):
        self.led.toggle()
        if self.debug:
            self.print_led_state()
