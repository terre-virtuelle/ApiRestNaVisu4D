import requests

#HOST_NAME="localhost"
HOST_NAME = "93.90.200.21"
PORT = "3003"
CONTROL = "control"
ORIGIN = "TV"
CMD = "scenario"
TARGET = "scenarioCN"
EXT = "json"

request = 'http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd='+CMD+'&origin='+ORIGIN+'&target='+TARGET+'&ext='+EXT
print(request)
r = requests.get(request)
print(r)
print(r.json())

