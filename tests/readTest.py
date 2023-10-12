import requests

#HOST_NAME="localhost"
HOST_NAME = "93.90.200.21"
PORT = "3003"
CONTROL = "read"
ORIGIN = "TV"
CMD = "scenario"
PATH = "scenarios/scenarioCN/"
TARGET = "scenarioCN.json"

request = 'http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd='+CMD+'&origin='+ORIGIN+'&path='+PATH+'&target='+TARGET
print(request)
r = requests.get(request)
print(r)


