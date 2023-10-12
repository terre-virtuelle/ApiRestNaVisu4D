import requests

#HOST_NAME="localhost"
HOST_NAME = "93.90.200.21"
PORT = "3003"
CONTROL = "nmea"
ORIGIN = "TV"
CMD = "display"
DATA = '$IIRMC,121458.60,A,4823.44,N,00425.55,W,49.43,125.51,050422,0.00,W*0A\r\n'

request = 'http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd='+CMD+'&origin='+ORIGIN+'&data='+DATA
print(request)
r = requests.put(request)
print(r)


