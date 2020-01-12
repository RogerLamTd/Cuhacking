import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog as fd
import grayscale
import mosaic

class MainApp:
    def __init__(self, parent):
        
        self.parent = parent
        self.frame = tk.Frame(self.parent, pady = 25, padx = 25)
        self.ratios=[0,0]
       
        self.photoconfirm = [False, False]
        #add photo place holders
        self.imagepathes = ["", ""]
        self.images = []
        self.image1 = tk.Frame(self.frame, height = 250, width = 250, padx = 25, pady = 10)
        self.image1.grid(row = 0, column = 0)
        self.image2 = tk.Frame(self.frame, height = 250, width = 250, padx = 25, pady = 10)
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
      
        #user inputs
        self.inputFrame1 = tk.Frame(self.frame)
        self.ratioLabel = tk.Label(self.inputFrame1, text = "Input number of pepes")
        self.ratioLabel.pack()
        self.enter1 = tk.Entry(self.inputFrame1)
        self.enter1.insert(10,10, )
        self.enter1.pack()
        self.ratioLabel = tk.Label(self.inputFrame1, text = "Input number of pepes2")
        self.ratioLabel.pack()
        self.enter2 = tk.Entry(self.inputFrame1)
        self.enter2.insert(10,10, )
        self.enter2.pack()
        self.submitButton = tk.Button(self.inputFrame1, text = "OK", command = lambda : self.submitEntry())
        self.submitButton.pack()
        self.inputFrame1.grid(row = 0, column = 3)



        self.frame.pack()
        


    def putPhoto(self, curr_photo):
        self.photoconfirm[curr_photo] = True
        filename = fd.askopenfilename()
        self.imagepathes[curr_photo] = filename
        image = Image.open(filename)
        ## fix formatting afterwards
        image = image.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        
        self.images[curr_photo].grid_forget()
        self.images[curr_photo] = tk.Label(self.frame, image = img)
        self.images[curr_photo].image = img
        self.images[curr_photo].grid(row = 0, column = curr_photo, padx = 25)
        
    def submitEntry(self):
     
        self.ratios[0] = int(self.enter1.get())
        self.ratios[1] = int(self.enter2.get())
        if self.photoconfirm[0] and self.photoconfirm[1]:
           
            finishImage = mosaic.partition(self.imagepathes[0], grayscale.grayscaleArray(self.imagepathes[1]), self.ratios)
            newWindow = tk.Toplevel(self.parent)
            finalImage = tk.Label(newWindow, image = finishImage)
            finalImage.image = finishImage
        else:
            print("NOOOO")
            

    



        

def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
    
   
    
   

if __name__ == '__main__':
    main()
