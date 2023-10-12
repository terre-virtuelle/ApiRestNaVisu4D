import requests

#HOST_NAME="localhost"
HOST_NAME = "93.90.200.21"
PORT = "3003"
CONTROL = "control"
CMD = "response"
TARGET = "r1"
ORIGIN = "TV"
request=""

time = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
request = 'http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd='+CMD+'&origin='+ORIGIN=+'&target='+TARGET+'&timestamp=' + time 
print(request)
r = requests.put(request)


