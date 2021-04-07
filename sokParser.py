import urllib.request
import os
from pdf2image import convert_from_path
from pathlib import Path
class SokParser:
    def getCampaign(self):
        os.chdir("C:/inetpub/wwwroot/marketbrosuru.com/wwwroot/img/bros-img")
        if os.path.isdir('sok')==False:
            os.mkdir('sok')
        os.chdir("C:/inetpub/wwwroot/marketbrosuru.com/wwwroot/img/bros-img/sok")
        haftaUrl="https://kurumsal.sokmarket.com.tr/firsatlar/carsamba/"
        haftaSonuUrl="https://kurumsal.sokmarket.com.tr/firsatlar/hafta-sonu/"
        Path('haftanin-firsatlari').mkdir(parents=True, exist_ok=True)
        Path('haftasonu-firsatlari').mkdir(parents=True, exist_ok=True)
        Path('temp').mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(haftaUrl, 'temp/hafta.pdf')
        urllib.request.urlretrieve(haftaSonuUrl, 'temp/haftaSonu.pdf')
        images = convert_from_path('temp/hafta.pdf', poppler_path='C:\\Program Files\\poppler\\Library\\bin')
        for i, image in enumerate(images, start=1):
            image.save('haftanin-firsatlari/'+str(i)+'.jpg')
        
        images = convert_from_path('temp/haftaSonu.pdf', poppler_path='C:\\Program Files\\poppler\\Library\\bin')
        for i, image in enumerate(images, start=1):
            image.save('C:/inetpub/wwwroot/marketbrosuru.com/wwwroot/img/bros-img/sok/haftasonu-firsatlari/'+str(i)+'.jpg')

        return { 'Brand':'ŞOK', 'Code':'sok', 'Campaigns':[{'Title':'Haftanın Fırsatları', 'Contents':'haftanin-firsatlari'},{'Title':'Haftasonu Fırsatları', 'Contents':'haftasonu-firsatlari'}] }


