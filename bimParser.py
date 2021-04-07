import requests
from bs4 import BeautifulSoup
import urllib.request
import os
from pathlib import Path

class BimParser:
    def __init__(self, response, group):
        self.response = response
        self.group = group
    def getCampaign(self):
        source = BeautifulSoup(self.response.content,"html.parser")
        #print(source.find("div",attrs={"class":self.group}))
        allgroups=source.findAll("div",attrs={"class":self.group})
        bimCampaigns=[]
        os.chdir("C:/inetpub/wwwroot/marketbrosuru.com/wwwroot/img/bros-img")
        if os.path.isdir('bim')==False:
            os.mkdir('bim')
        os.chdir("C:/inetpub/wwwroot/marketbrosuru.com/wwwroot/img/bros-img/bim")
        for number, group in enumerate(allgroups, start=1):
            title=group.select("a>span")[0].text
            hrefs=group.select("div.row>div.imageArea>div.row>div.smallArea>a")
            
            Path(str(number)).mkdir(parents=True, exist_ok=True)
            for imgx, href in enumerate(hrefs, start=1):
                urllib.request.urlretrieve("http://www.bim.com.tr/"+href.get('data-bigimg'), 'C:/inetpub/wwwroot/marketbrosuru.com/wwwroot/img/bros-img/bim/'+str(number)+'/'+str(imgx)+".jpg")

            bimCampaigns.append(title)
        
        return bimCampaigns
