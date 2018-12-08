from PIL import Image
import sys
import os
from tkinter import messagebox
import ShowImage


def do_darkness(path):
    if path:
        try:
            if len(sys.argv) == 2:
                path = sys.argv[1]

            img = Image.open(path)
            img = darkness(img)
            img.save(os.path.splitext(path)[0] + '_Darkness.jpg', 'JPEG')
            messagebox.showinfo("Successful", "Successfully Done")
            ShowImage.show_Image(os.path.splitext(path)[0] + '_Darkness.jpg')
        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")


def darkness(img):
    return img.point(lambda i: int(i ** 2 / 255))
