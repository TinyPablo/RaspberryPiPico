import utime
import network
import socket
from machine import Pin

ssid = 'pawelinternet'
password = 'internetpawla'

ap = network.WLAN(network.STA_IF)
ap.config(ssid=ssid, password=password)
ap.active(True)

# Wait for Wi-Fi to become active
wait_counter = 0
while not ap.active():
    print("Waiting " + str(wait_counter))
    utime.sleep(0.5)

print('WiFi active')
status = ap.ifconfig()
pico_ip = status[0]
print('IP = ' + status[0])

# Open a socket
addr = (pico_ip, 35555)
s = socket.socket()
s.bind(addr)
s.listen(1)
print('Listening on', addr)

led = Pin(28, Pin.OUT)
led.off()
led_state = False

# Main loop
while True:
    client, client_addr = s.accept()
    raw_request = client.recv(1024)
    # Translate byte string to a normal string variable
    raw_request = raw_request.decode("utf-8")
    print(raw_request)

    # Break the request into words (split at spaces)
    request_parts = raw_request.split()
    http_method = request_parts[0]
    request_url = request_parts[1]

    if request_url.find("/ledon") != -1:
        # Turn the LED on
        led_state = True
        led.on()
    elif request_url.find("/ledoff") != -1:
        # Turn the LED off
        led_state = False
        led.off()
    else:
        # Do nothing
        pass

    led_state_text = "OFF"
    if led_state:
        led_state_text = "ON"

    try:
        with open("simpleled.html", "r") as file:
            html = file.read()
    except OSError as e:
        print("Error opening or reading 'simpleled.html':", e)
        html = "Error loading the HTML file"

    html = html.replace('**ledState**', led_state_text)
    client.send(html)
    client.close()
