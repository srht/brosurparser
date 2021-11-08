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

from static import static

os.chdir("img")

try:
    if os.path.isdir('bros-img'):
        shutil.rmtree('bros-img')
   
    os.mkdir('bros-img')
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))

response = requests.get('https://www.bim.com.tr/Categories/680/afisler.aspx')
jsonCampaigns=[]
bimParser=BimParser(response, 'grup2')
bimCampaigns= bimParser.getCampaign()
for number,bimCampaign in enumerate(bimCampaigns, start=1):
    jsonCampaigns.append({ 'Title':bimCampaign["title"], 'Contents':str(number), 'Texts':bimCampaign["text"] })

bimParser=BimParser(response, 'grup3')
bimCampaigns= bimParser.getCampaign()

for number,bimCampaign in enumerate(bimCampaigns, start=1):
    jsonCampaigns.append({ 'Title':bimCampaign["title"], 'Contents':str(number), 'Texts':bimCampaign["text"] })

bimParser=BimParser(response, 'grup4')
bimCampaigns= bimParser.getCampaign()

for number,bimCampaign in enumerate(bimCampaigns, start=1):
    jsonCampaigns.append({ 'Title':bimCampaign["title"], 'Contents':str(number), 'Texts':bimCampaign["text"] })
    
bim={ 'Brand':'BİM', 'Code':'bim', 'Campaigns':jsonCampaigns }
#print(json.dumps(bim))

jsonCampaigns=[]
response = requests.get('https://www.a101.com.tr/afisler-haftanin-yildizlari')
a101Parser=A101Parser(response)
a101Campaign=a101Parser.getCampaign(1)
jsonCampaigns.append({ 'Title':a101Campaign[0]["title"], 'Contents':'1', 'Texts':a101Campaign[0]["text"] })

response = requests.get('https://www.a101.com.tr/aldin-aldin-gelecek-hafta-brosuru/')
a101Parser=A101Parser(response)
a101Campaign=a101Parser.getCampaign(2)
jsonCampaigns.append({ 'Title':a101Campaign[0]["title"], 'Contents':'2', 'Texts':a101Campaign[0]["text"] })

response = requests.get('https://www.a101.com.tr/aldin-aldin-bu-hafta-brosuru/')
a101Parser=A101Parser(response)
a101Campaign=a101Parser.getCampaign(3)
jsonCampaigns.append({ 'Title':a101Campaign[0]["title"], 'Contents':'3', 'Texts':a101Campaign[0]["text"] })

a101={ 'Brand':'A101', 'Code':'a101', 'Campaigns':jsonCampaigns }

SokParser=SokParser()
sok=SokParser.getCampaign()


with open(static.appPath+'/Data/bros.json', 'w') as outfile:
    json.dump([bim, a101, sok], outfile)
#with open('bros.json') as json_file:
#    data = json.load(json_file)

#for b in data:
#    if b['Code']=='bim':
#        print(b['Campaigns'])
        

#print('Name: ' + data[0]['Campaigns'][0]['Title'])
