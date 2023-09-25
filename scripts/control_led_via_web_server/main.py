from Led import *
from Lcd import *
from LcdApi import *
from I2cLcd import *
from NetworkConnection import *

import urequests as requests
import socket

DEBUG = True

led = Led(16, True)
lcd = Lcd(0, 1)

connection = NetworkConnection('pawelinternet', 'internetpawla')
status = connection.connect()
ip = status[0]
port = 44445


addr = socket.getaddrinfo(ip, port)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)


while True:
    try:
        cl, addr = s.accept()
        print('Client connected from', addr)
        r = cl.recv(1024)
        
        r = str(r)
        led_on = r.find('?led=on')
        led_off = r.find('?led=off')
        print(r)
        if led_on > -1:
            print('LED ON')
            led.value(1)
            lcd.clear()
            lcd.write('ON')
            
        if led_off > -1:
            print('LED OFF')
            led.value(0)
            lcd.clear()
            lcd.write('OFF')
            
        # cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.close()
            

        
    except OSError as e:
        cl.close()
        print('Connection closed')
        print('error: ' + str(e))