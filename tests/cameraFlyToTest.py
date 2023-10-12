import requests
from datetime import datetime, timezone
import random

#HOST_NAME="localhost"
HOST_NAME = "93.90.200.21"
PORT = "3003"
CONTROL = "control"
CMD = "flyTo"
TARGET = "camera"

lat = str(48.34395)
lon = str(-4.49241)
r = requests.put('http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd='+CMD+'&origin='+ORIGIN+'&target='+TARGET+'&latitude='+ lat +'&longitude='+lon+'&altitude=100&heading=0&pitch=0.0&roll=0.0')

