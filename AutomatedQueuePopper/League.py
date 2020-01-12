import PIL
import pyautogui 


def popper():
   while True:
        try:
            box = pyautogui.locateOnScreen("C:/Users/Bryan/Documents/GitHub/Cuhacking/decline.png", confidence = 0.55)
            loc = pyautogui.center(box)
            print(loc)
            pyautogui.click(loc.x, loc.y)
            break
        except:
            print("bropkebobuo")
        

