import time
from NetworkConnection import NetworkConnection
from Led import Led
from Lcd import Lcd
import urequests

debug = True

led = Led(16, debug)
lcd = Lcd(0, 1, debug)

connection = NetworkConnection('pawelinternet', 'internetpawla')
connection.connect()

led.value(1)
time.sleep(.2)
led.value(0)

while True:
    res = urequests.get('http://192.168.1.109:33003/get_seconds')
    json = res.json()
    seconds = int(json.get('seconds'))
    print(seconds)
    lcd.clear()
    lcd.write(str(seconds))
    time.sleep(1)

