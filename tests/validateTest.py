import requests

#HOST_NAME="localhost"
HOST_NAME = "93.90.200.21"
PORT = "3003"
CONTROL = "control"
CMD = "validate"
TARGET = "true"

r = requests.put('http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd='+CMD+'&origin='+ORIGIN+'&target='+TARGET

