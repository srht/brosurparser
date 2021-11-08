import urllib.request
import os
from PIL import Image
from pdf2image import convert_from_path
from pathlib import Path
from ocr import Ocr

from static import static
class SokParser:
    def getCampaign(self):
        os.chdir(static.appPath+"img/bros-img")
        if os.path.isdir('sok')==False:
            os.mkdir('sok')
        os.chdir(static.appPath+"img/bros-img/sok")
        haftaUrl="https://kurumsal.sokmarket.com.tr/firsatlar/carsamba/"
        haftaSonuUrl="https://kurumsal.sokmarket.com.tr/firsatlar/hafta-sonu/"
        Path('haftanin-firsatlari').mkdir(parents=True, exist_ok=True)
        Path('haftasonu-firsatlari').mkdir(parents=True, exist_ok=True)
        Path('temp').mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(haftaUrl, 'temp/hafta.pdf')
        urllib.request.urlretrieve(haftaSonuUrl, 'temp/haftaSonu.pdf')
        images = convert_from_path('temp/hafta.pdf', poppler_path='C:\\Program Files\\poppler\\Library\\bin')
        ocr=Ocr()
        texts=[]
        for i, image in enumerate(images, start=1):
            image.save(static.appPath+'img/bros-img/sok/haftanin-firsatlari/'+str(i)+'.jpg')
            haftaText=ocr.read(static.appPath+'img/bros-img/sok/haftanin-firsatlari/'+str(i)+'.jpg')
            openedImage= Image.open(static.appPath+'img/bros-img/sok/haftanin-firsatlari/'+str(i)+'.jpg')
            openedImage.thumbnail([810,810])
            openedImage.save(static.appPath+'img/bros-img/sok/haftanin-firsatlari/'+str(i)+'thumb.jpg')

        
        images = convert_from_path('temp/haftaSonu.pdf', poppler_path='C:\\Program Files\\poppler\\Library\\bin')
        for i, image in enumerate(images, start=1):
            image.save(static.appPath+'img/bros-img/sok/haftasonu-firsatlari/'+str(i)+'.jpg')
            haftaSonuText=ocr.read(static.appPath+'img/bros-img/sok/haftasonu-firsatlari/'+str(i)+'.jpg')
            openedImage= Image.open(static.appPath+'img/bros-img/sok/haftasonu-firsatlari/'+str(i)+'.jpg')
            openedImage.thumbnail([810,810])
            openedImage.save(static.appPath+'img/bros-img/sok/haftasonu-firsatlari/'+str(i)+'thumb.jpg')

        return { 
            'Brand':'ŞOK', 
            'Code':'sok', 
            'Campaigns':
                [
                    {'title':'Haftanın Fırsatları', 'contents':'haftanin-firsatlari', 'texts':haftaText},
                    {'title':'Haftasonu Fırsatları', 'contents':'haftasonu-firsatlari', 'texts':haftaSonuText}
                ] 
            }


