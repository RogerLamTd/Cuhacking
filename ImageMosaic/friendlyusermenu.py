import tkinter as tk
from PIL import ImageTk, Image

class MainApp:
    def __init__(self, parent):
        self.parent = parent
        self.pressed = False
        self.start = tk.Button(self.parent, height = 10, width = 50, text = "start", command = lambda : self.toggle())
        self.start.pack(fill = tk.BOTH)
        self.parent.winfo_toplevel().title("League Q Popper")
    
    def toggle(self):
        self.pressed = not self.pressed
        while self.pressed:
            self.start.configure(text="stop")
            self.pressed = popper()
        

def popper():
    try:
        box = pyautogui.locateOnScreen("C:/Users/Bryan/Documents/GitHub/Cuhacking/decline.png", confidence = 0.55)
        loc = pyautogui.center(box)
        print(loc)
        pyautogui.click(loc.x, loc.y)
        return False
    except:
        return True
        
def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
    
   
    
   

if __name__ == '__main__':
    main()