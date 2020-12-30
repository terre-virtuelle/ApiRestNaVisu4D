import requests
import time
import random


i = 0
sign = -1
range = 0
while i < 10:
 lat = str(48.00 + range)
 lon = str(-4.50 - range)
 r = requests.put('http://93.90.200.21:3003/control?cmd=flyTo&origin=SMAUG&target=camera&latitude='+ lat +'&longitude='+lon+'&altitude=300000&heading=0.0&pitch=-80.0&roll=0.0')
 str(r);
 sign *= sign
 range = sign * random.randint(0, 50) 
 time.sleep(1)
 i = i + 0.5 


