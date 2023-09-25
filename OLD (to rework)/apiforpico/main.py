from flask import Flask
import psutil
from waitress import serve

app = Flask(__name__)


@app.route('/')
def api():
    cpu_percent = psutil.cpu_percent(False)
    virtual_memory = psutil.virtual_memory()
    # small
    payload = {
        "cpu": cpu_percent,
        "ram": round(virtual_memory.percent, 3)
    }

    # payload = {
    #     "cpu_usage": cpu_percent,
    #     "ram": {
    #         "available": round(virtual_memory.available / (pow(1024, 3)), 3),
    #         "used": round(virtual_memory.used / (pow(1024, 3)), 3),
    #         "usage_percent": round(virtual_memory.percent, 3)
    #     }
    # }

    return payload


if __name__ == '__main__':
    serve(app, host='192.168.1.106', port=33005)
