import pytesseract
import PIL.Image
import cv2
import os

myconfig = r"--psm 6 --oem 3"
imageDir = 'D:\\Newfolder\\Freelancing\\Upwork\\testExtText\\images'
pytesseract.pytesseract.tesseract_cmd = 'D:\\Installation\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "D:\\Installation\\Tesseract-OCR\\tessdata"'

for filename in os.listdir(imageDir):
    if filename.endswith('.jpg'):
        with open(os.path.join(imageDir, filename)) as f:
            print('--- filename --- ' + filename)
            #print(f.read())
            #print('--- filename --- ' + filename )
            print(pytesseract.image_to_string(PIL.Image.open(imageDir + '\\' + filename), lang='eng', config=tessdata_dir_config))
    print("***************************************************************************")


#print(pytesseract.image_to_string(PIL.Image.open('img1.jpg'), lang='eng', config = tessdata_dir_config))
