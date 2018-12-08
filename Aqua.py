from PIL import Image
import sys
import os
from tkinter import messagebox
import ShowImage


def do_aqua(path):
    if path:
        try:
            if len(sys.argv) == 2:
                path = sys.argv[1]

            img = Image.open(path)
            img = aqua(img)
            img.save(os.path.splitext(path)[0] + '_Aqua.jpg', 'JPEG')
            messagebox.showinfo("Successful", "Successfully Done")
            ShowImage.show_Image(os.path.splitext(path)[0] + '_Aqua.jpg')
        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")


def aqua(img):
    if img.mode != "RGB":
        img.convert("RGB")

    width, height = img.size
    pix = img.load()

    for w in range(width):
        for h in range(height):
            r, g, b = pix[w, h]

            pix[w, h] = min(255, int((g - b) ** 2 / 128)), \
                        min(255, int((r - b) ** 2 / 128)), \
                        min(255, int((r - g) ** 2 / 128))
    return img
