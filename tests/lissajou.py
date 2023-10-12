#Python Turtle - Lissajous Curve - www.101computing.net/python-turtle-lissajous-curve/
import requests
import turtle
from math import cos,sin
from time import sleep
from datetime import datetime, timezone

#HOST_NAME="localhost"
HOST_NAME = "93.90.200.21"
PORT = "3003"
CONTROL = "control"
ORIGIN = "SMAUG"
CMD_1 = "start"
CMD_2 = "track"
TARGET = "ship"

A = 250
B = 150
a = 5 
b = 4
delta = 3.14/2
t=0

time = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
#r = requests.put('http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd='+CMD_1+'&origin='+ORIGIN+'&timestamp=' + time)

for i in range(0,10000):
    t+=0.01
    #Apply Lissajous Parametric Equations
    x = A * sin(a*t + delta) 
    y = B * sin(b*t) 
    lat = str(48.34 + y/50000)
    lon = str(-4.50 + x/25000)
    time = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
    #print(time)
    r = requests.put('http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd='+CMD_2+'&origin='+ORIGIN+'&target='+TARGET+'&timestamp=' + time + '&latitude='+ lat +'&longitude=' + lon + '&altitude=0&heading=511&pitch=0.0&roll=0.0')
    sleep(0.5)

