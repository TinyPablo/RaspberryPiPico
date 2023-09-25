from Lcd import *
from NetworkConnection import *
import socket

lcd = Lcd(0, 1)

connection = NetworkConnection('pawelinternet', 'internetpawla')
status = connection.connect()
ip = status[0]
port = 44449

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
        text_start = r.find('?text=')
        
        if text_start != -1:
            text_end = r.find('&', text_start)  # Find the end of the text parameter
            if text_end == -1:
                text_end = len(r)  # If there's no '&' symbol, use the end of the string
            text_value = r[text_start + 6:text_end]  # Extract the text value
            print("Received text:", text_value)
            lcd.clear()
            lcd.write(text_value)
            
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.close()
            
    except OSError as e:
        cl.close()
        print('Connection closed')
        print('Error: ' + str(e))
