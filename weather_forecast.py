import requests
import json

APIKEY = ''
LATTITUDE = '31.678975'
LONGITUDE = '75.638266'

url = 'https://api.forecast.io/forecast/%s/%s,%s' % (APIKEY, LATTITUDE, LONGITUDE)
response = requests.get(url)

data = json.loads(response.content)
print data["currently"]["icon"]

F = data["currently"]["temperature"]
C = 5*(F-32)/9
print "Temperature: "+str(C)+" degrees Celcius"
