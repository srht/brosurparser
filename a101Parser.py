import requests
from bs4 import BeautifulSoup
import os
import urllib.request
from pathlib import Path

class A101Parser:
    def __init__(self, response):
        self.response = response
    def getCampaign(self,campaignNo):
        source = BeautifulSoup(self.response.content,"html.parser")
        #print(source.find("div",attrs={"class":self.group}))
        
        title= source.select("ul.brochures-actions-list>li")[campaignNo-1].find('a').select('div.dates')[0].get('data-date')

        images=source.select("div.brochure-tabs>div.contents>div.content")[0].findAll('img', attrs={"class":"image0"})

        a101Campaigns=[]
        a101Campaigns.append(title)
        os.chdir("C:/inetpub/wwwroot/marketbrosuru.com/wwwroot/img/bros-img")
        if os.path.isdir('a101')==False:
            os.mkdir('a101')
        os.chdir("C:/inetpub/wwwroot/marketbrosuru.com/wwwroot/img/bros-img/a101")
        for number, image in enumerate(images, start=1):
            Path(str(campaignNo)).mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(image.get('src'), 'C:/inetpub/wwwroot/marketbrosuru.com/wwwroot/img/bros-img/a101/'+str(campaignNo)+'/'+str(number)+".jpg")
                
         
        
        return a101Campaigns
