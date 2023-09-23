import time
from NetworkConnection import NetworkConnection
from Led import Led
import urequests

led = Led(0, True)

led.value(1)
time.sleep(.2)
led.value(0)

connection = NetworkConnection('pawelinternet', 'internetpawla')
connection.connect()

while True:
    res = urequests.get('http://192.168.1.109:33003/get_seconds')
    json = res.json()
    seconds = int(json.get('seconds'))
    print(seconds)
    if 0 < seconds < 30:
        led.value(1)
    else:
        led.value(0)
    time.sleep(.5)
