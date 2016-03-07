import urllib2
import json
lan,lon=input("balte suntetagmenes sti morfi lat,lon: ")
urlData="http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=fe027d49c1d62e4bd358bf941a3f9d45"
urlData= urlData%(lan,lon)
webUrl = urllib2.urlopen(urlData)
data = webUrl.read()
theJSON = json.loads(data)
json_obj=(urllib2.urlopen(urlData))
data = json.load(json_obj)
for item in data['weather']:
    if item['main']== "Rain":
        print "I'm singing in the rain!"


if "temp" in theJSON["main"]:
    if theJSON["main"]["temp"]>293:
        print "nice..."
            
if "temp" in theJSON["main"]:
    if theJSON["main"]["temp"]<278.15:
        print "brrrr"
            
