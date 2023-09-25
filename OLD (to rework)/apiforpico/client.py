import time

import requests

res = requests.get('http://192.168.1.106:33005')
data = res.json()

print(data)
time.perf_counter()