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

response = requests.get('your_json_url')

if response.status_code == 200:
    json_data = response.json()
    print(json_data)
