import numpy as np
from PIL import ImageGrab, Image
import cv2
import pytesseract
import math


class Process:
    def __init__(self):
        self.currentHealth = 100
        self.ocrErr = False

    def processImg(self, greyImg):
        self.currentHealth
        txt = pytesseract.image_to_string(greyImg)
        print(txt)
        if txt == 'Accept' or txt == '|1oo':
            return True
        try:        
            health = int(txt)
            self.ocrErr = False
        except:
            health = self.currentHealth
            if not self.ocrErr:
                health = self.currentHealth - 1
                self.ocrErr = True

        if health < self.currentHealth:
            self.currentHealth = health
            return True
        return False



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