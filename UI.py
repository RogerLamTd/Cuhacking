import tkinter as tk
from PIL import ImageTk, Image

from tkinter import filedialog as fd

class MainApp:
    def __init__(self, parent):
        
        self.parent = parent
        self.frame = tk.Frame(self.parent, pady = 25)

        '''
        self.cols = []
        col1 = tk.Frame(self.parent, padx = 25, pady = 25)
        col2 = tk.Frame(self.parent, padx = 25, pady = 25)
        self.cols.append(col1)
        self.cols.append(col2)
        '''

        self.images = []
        self.image1 = tk.Frame(self.frame, height = 250, width = 250, padx = 25)
        self.image1.grid(row = 0, column = 0)
        self.image2 = tk.Frame(self.frame, height = 250, width = 250, padx = 25)
        self.image2.grid(row = 0, column = 1)
        buffer = tk.Label(self.image1, bg = "gray", height = 10, width = 25, text = "Image 1")
        buffer.pack()
        buffer = tk.Label(self.image2, bg = "gray", height = 10, width = 25, text = "Image 2")
        buffer.pack()


        self.images.append(self.image1)
        self.images.append(self.image2)

      

        #add photo buttons
        self.photoButton1 = tk.Button(self.frame, pady = 10, text = "Select Photo 1", command = lambda : self.putPhoto(0))
        self.photoButton1.grid(row = 1, column = 0)
        self.photoButton2 = tk.Button(self.frame, pady = 10, text = "Select Photo 2", command = lambda : self.putPhoto(1))
        self.photoButton2.grid(row = 1, column = 1)
        '''
        self.cols[0].pack(side = tk.LEFT)
        self.cols[1].pack(side = tk.LEFT)
        '''
        self.frame.pack()


    def putPhoto(self, curr_photo):
        filename = fd.askopenfilename()
       
        
        image = Image.open(filename)
        image = image.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        
        self.images[curr_photo].grid_forget()
        self.images[curr_photo] = tk.Label(self.frame, image = img)
        self.images[curr_photo].image = img
        self.images[curr_photo].grid(row = 0, column = curr_photo, padx = 25)
        
        


        

def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
    
   
    
   

if __name__ == '__main__':
    main()
