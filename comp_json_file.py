
from deepdiff import DeepDiff
import requests
import json


url1 = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
url2 = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"

r1 = requests.get(url=url1) # response 
r2 = requests.get(url=url1) # response 


#r1 = {'a': 1, 'b': 2} 
#r2 = {'a': 1, 'b': 2, 'c':12}

"""
with open('file1.json') as json_file1:
    r1 = json.load(json_file1)
#print(r1)

with open('file2.json') as json_file2:
#with open('file3.json') as json_file2:
    r2 = json.load(json_file2)
#print(r2)
"""

diff = DeepDiff(r1, r2, ignore_order=True) # compare the dictionaries

#assert not diff, f"difference in response: {diff}"
#print (diff)


#If any difference diff is Not Empty

if len(diff) == 0:
    print("Json files are Similar")
else:
    print("Json files are Different : " , diff )
