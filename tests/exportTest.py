import requests

#HOST_NAME="localhost"
HOST_NAME = "93.90.200.21"
PORT = "3003"
CONTROL = "export"
ORIGIN = "TV"
CMD = "scenario"
TARGET = "scenarioCN"

request = 'http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd='+CMD+'&origin='+ORIGIN+'&target='+TARGET
print(request)
r = requests.put(request)
print(r)


