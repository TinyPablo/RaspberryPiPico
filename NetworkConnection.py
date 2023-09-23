import time
import network

class NetworkConnection:
    def __init__(self, _ssid: str, _password: str):
        self.ssid = _ssid
        self.password = _password
        self.wlan: network.WLAN = None
        self.status = None
        self.ip = None

    def connect(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)

        max_wait = 10
        while max_wait > 0:
            max_wait -= 1
            if self.wlan.status() == 3:
                break
            time.sleep(1)
        else:
            print('connection failed')
        print('connection established')

        self.status = self.wlan.ifconfig()
        self.ip = self.status[0]
        print('IP: ' + self.ip)
