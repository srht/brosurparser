import requests
import numpy as np
import os
import pathlib
import sys
import shutil
from bimParser import BimParser
from a101Parser import A101Parser
from sokParser import SokParser
from market import Market
from campaign import Campaign
import json


response = requests.get('https://www.bim.com.tr/Categories/680/afisler.aspx')
jsonCampaigns=[]
bimParser=BimParser(response, 'grup2')
print(bimParser)
#with open('bros3.json', 'w') as outfile:
 #   json.dump(["bim", "a101", "sok"], outfile)
#with open('bros.json') as json_file:
#    data = json.load(json_file)

#for b in data:
#    if b['Code']=='bim':
#        print(b['Campaigns'])
        

#print('Name: ' + data[0]['Campaigns'][0]['Title'])
