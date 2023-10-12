import requests

#HOST_NAME="localhost"
HOST_NAME = "93.90.200.21"
PORT = "3003"
CONTROL = "image"
ORIGIN = "TV"
CMD = "scenario"
PATH = "scenarios/media/images/"
TARGET = "img1.png"

request = 'http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd='+CMD+'&origin='+ORIGIN+'&path='+PATH+'&target='+TARGET
print(request)
r = requests.get(request)
print(r)


