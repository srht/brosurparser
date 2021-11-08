from PIL import Image
import requests
from bs4 import BeautifulSoup
import os
import urllib.request
from pathlib import Path
from ocr import Ocr

from static import static

class A101Parser:
    def __init__(self, response):
        self.response = response
    def getCampaign(self,campaignNo):
        source = BeautifulSoup(self.response.content,"html.parser")
        #print(source.find("div",attrs={"class":self.group}))
        
        title= source.select("ul.brochures-actions-list>li")[campaignNo-1].find('a').select('div.dates')[0].get('data-date')

        images=source.select("div.brochure-tabs>div.contents>div.content")[0].findAll('img', attrs={"class":"image0"})
        ocr=Ocr()
        a101Campaigns=[]
       
        os.chdir(static.appPath+"img/bros-img")
        if os.path.isdir('a101')==False:
            os.mkdir('a101')
        os.chdir(static.appPath+"img/bros-img/a101")
        texts=[]
        for number, image in enumerate(images, start=1):
            Path(str(campaignNo)).mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(image.get('src'), static.appPath+'img/bros-img/a101/'+str(campaignNo)+'/'+str(number)+".jpg")
            imgContent=ocr.read(static.appPath+'img/bros-img/a101/'+str(campaignNo)+'/'+str(number)+".jpg")
            texts.append(imgContent)
            openedImage= Image.open(static.appPath+'img/bros-img/a101/'+str(campaignNo)+'/'+str(number)+".jpg")
            openedImage.thumbnail([810,810])
            openedImage.save(static.appPath+'img/bros-img/a101/'+str(campaignNo)+'/'+str(number)+"thumb.jpg")
                
        a101Campaigns.append({"title":title, "text":texts})
        
        return a101Campaigns
