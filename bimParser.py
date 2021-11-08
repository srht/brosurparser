import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import os
from pathlib import Path
from PIL import Image
from ocr import Ocr
from static import static

class BimParser:
    def __init__(self, response, group):
        self.response = response
        self.group = group
    def getCampaign(self):
        source = BeautifulSoup(self.response.content,"html.parser")
        #print(source.find("div",attrs={"class":self.group}))
        allgroups=source.findAll("div",attrs={"class":self.group})
        bimCampaigns=[]
        #C:/inetpub/wwwroot/marketbrosuru.com/wwwroot
        os.chdir(static.appPath+"img/bros-img")
        ocr=Ocr()
        if os.path.isdir('bim')==False:
            os.mkdir('bim')
        os.chdir(static.appPath+"img/bros-img/bim")
        for number, group in enumerate(allgroups, start=1):
            title=group.select("a>span")[0].text
            hrefs=group.select("div.row>div.imageArea>div.row>div.smallArea>a")
            texts=[]
            Path(str(number)).mkdir(parents=True, exist_ok=True)
            for imgx, href in enumerate(hrefs, start=1):
                urllib.request.urlretrieve("http://www.bim.com.tr/"+urllib.parse.quote(href.get('data-bigimg')), static.appPath+'img/bros-img/bim/'+str(number)+'/'+str(imgx)+".jpg")
                imgContent=ocr.read(static.appPath+'img/bros-img/bim/'+str(number)+'/'+str(imgx)+".jpg")
                texts.append(imgContent)
                openedImage= Image.open(static.appPath+'img/bros-img/bim/'+str(number)+'/'+str(imgx)+".jpg")
                openedImage.thumbnail([810,810])
                openedImage.save(static.appPath+'img/bros-img/bim/'+str(number)+'/'+str(imgx)+"thumb.jpg")
            bimCampaigns.append({"title":title, "text":texts})
        
        return bimCampaigns
