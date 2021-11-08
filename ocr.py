import cv2
import re
import pytesseract
from pytesseract import Output

class Ocr:
    def read(self,url):
        img = cv2.imread(url)
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        ocrTexts=[]
        for text in d['text']:
            if text!='' and text.isalnum() and len(text)>2:
                ocrTexts.append(text)

        joinedTexts = ', '.join(map(str, ocrTexts))

        return joinedTexts
