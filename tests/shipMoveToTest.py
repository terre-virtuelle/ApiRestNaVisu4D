import requests
from time import sleep
from datetime import datetime, timezone
import random

#HOST_NAME="localhost"
HOST_NAME = "93.90.200.21"
PORT = "3003"
CONTROL = "control"
CMD = "moveTo"
TARGET = "ship"

i = 0
sign = -1
rangeLat = 0
rangeLon = 0
while i < 100:
 lat = str(48.34395 + rangeLat)
 lon = str(-4.49241 + rangeLon)
 timestamp = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
 r = requests.put('http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd='+CMD+'&origin='+ORIGIN=+'&target='+TARGET+'&timestamp=' + timestamp + '&latitude='+ lat +'&longitude='+lon+'&altitude=0&heading=511&pitch=-90.0&roll=0.0')
 sign *= sign
 rangeLat = sign * random.uniform(0.0, 0.01) 
 rangeLon = sign * random.uniform(0.0, 0.01) 
 sleep(0.5)
 i = i + 0.5 

 print(r.text)
