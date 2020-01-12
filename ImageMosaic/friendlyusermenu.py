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
        if self.pressed:
            self.start.configure(text="stop")
        else:
            self.start.configure(text="start")


def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
    
   
    
   

if __name__ == '__main__':
    main()