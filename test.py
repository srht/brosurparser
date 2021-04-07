import requests
import json


with open('bros3.json', 'w') as outfile:
    json.dump(["bim", "a101", "sok"], outfile)
#with open('bros.json') as json_file:
#    data = json.load(json_file)

#for b in data:
#    if b['Code']=='bim':
#        print(b['Campaigns'])
        

#print('Name: ' + data[0]['Campaigns'][0]['Title'])
