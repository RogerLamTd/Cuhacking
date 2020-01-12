import numpy as np
from PIL import ImageGrab, Image
import cv2
import pytesseract
import math



class Process:
    def __init__(self):
        self.target = "decline"
        self.ocrErr = False

    def processImg(self, greyImg):
        txt = pytesseract.image_to_string(greyImg)
        print(txt)
        if self.target in txt:
            print('fu')
        try:        
            print('fu')
        except:
            print('fu')


def main():
    process = Process()
    while(True):
        x = 760
        y = 968

        offx = 50
        offy = 22
        img = ImageGrab.grab(bbox=(x, y, x + offx, y + offy)).convert('L')
        
        img = np.array(img)
        cv2.imshow('window', img)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):  
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
