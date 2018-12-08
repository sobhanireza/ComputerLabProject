from PIL import Image
import sys
import os
from tkinter import messagebox
import ShowImage


def do_comic(path):
    if path:
        try:
            if len(sys.argv) == 2:
                path = sys.argv[1]

            img = Image.open(path)
            img = comic(img)
            img.save(os.path.splitext(path)[0] + '_Comic.jpg', 'JPEG')
            messagebox.showinfo("Successful", "Successfully Done")
            ShowImage.show_Image(os.path.splitext(path)[0] + '_Comic.jpg')
        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")


def comic(img):
    width, height = img.size

    if img.mode != 'RGB':
        img = img.convert('RGB')

    pix = img.load()

    for w in range(width):
        for h in range(height):
            r, g, b = pix[w, h]

            pix[w, h] = tuple(map(lambda i: min(255, i),
                                  [int(abs(g - b + g + r) * r / 256),
                                   int(abs(b - g + b + r) * r / 256),
                                   int(abs(b - g + b + r) * r / 256)]))

    return img.convert('L')
