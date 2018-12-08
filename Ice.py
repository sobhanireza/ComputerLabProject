from PIL import Image
import sys
import os
from tkinter import messagebox
import ShowImage

def do_ice(path):
    if path:
        try:
            if len(sys.argv) == 2:
                path = sys.argv[1]

            img = Image.open(path)
            img = ice(img)
            img.save(os.path.splitext(path)[0] + '_Ice.jpg', 'JPEG')
            messagebox.showinfo("Successful", "Successfully Done")
            ShowImage.show_Image(os.path.splitext(path)[0] + '_Ice.jpg')
        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")


def ice(img):
    if img.mode != "RGB":
        img.convert("RGB")

    width, height = img.size
    pix = img.load()

    for w in range(width):
        for h in range(height):
            r, g, b = pix[w, h]

            pix[w, h] = min(255, int(abs(r - g - b) * 3 / 2)), \
                        min(255, int(abs(g - b - r) * 3 / 2)), \
                        min(255, int(abs(b - r - g) * 3 / 2))

    return img