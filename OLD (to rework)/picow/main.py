from machine import Pin
import time
import random
import socket as s
import urequest
import network

# LED
led = Pin(0, Pin.OUT)
led_state = False
led.value(led_state)

# WI-FI
SSID = 'pawelinternet'
PASSWORD = 'internetpawla'

# CONNECTION
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(SSID, PASSWORD)

connecting_counter = 10
while True:
    connecting_counter -= 1
    if connecting_counter > 10:
        print('connection failed')
    elif network.isconnected():
        print('connection established')
        break
    else:
        print('connecting ' + str(connecting_counter))

status = wlan.ifconfig()
IP = status[0]

ADDRESS = IP, 33003

server_socket = s.socket()
server_socket.bind(ADDRESS)
server_socket.listen(1)

while True:
    client_socket, client_address = server_socket.accept()
    raw_request = client_socket.recv(1024)
    print(raw_request)

    led_state_text = 'ON' if led_state else 'OFF'

    with open('index.html') as f:
        html = f.read()

    html = html.replace('**ledState**', led_state_text)
    client_socket.send(html)
    client_socket.close()