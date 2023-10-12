import requests
from datetime import datetime, timezone

#HOST_NAME="localhost"
HOST_NAME = "93.90.200.21"
PORT = "3003"
CONTROL = "control"
CMD = "stop"
ORIGIN = "TV"

time = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
r = requests.put('http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd='+CMD+'&origin='+ORIGIN+'&timestamp=' + time)

