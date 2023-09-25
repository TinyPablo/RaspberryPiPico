# new project


from machine import Pin
import time

def int_to_bin(val, length):
    bin_str = str(bin(val))[2:]
    return "{0:0>{1}}".format(bin_str, length)


leds = [Pin(l, Pin.OUT) for l in range(2, 16)]

delay = .45
  
print('h:', 2 ** len(leds) / 3600 * delay)
print('m:', 2 ** len(leds) / 60 * delay)
print('s:', 2 ** len(leds) * delay)
for i in range(2 ** len(leds)):
    for x, b in enumerate(int_to_bin(i, len(leds))):
        leds[x].value(int(b))
    time.sleep(delay)



