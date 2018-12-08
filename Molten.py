from PIL import Image
import sys
import os
from tkinter import messagebox
import ShowImage


def do_molten(path):
    if path:
        try:
            if len(sys.argv) == 2:
                path = sys.argv[1]

            img = Image.open(path)
            img = molten(img)
            img.save(os.path.splitext(path)[0] + '_Molten.jpg', 'JPEG')
            messagebox.showinfo("Successful", "Successfully Done")
            ShowImage.show_Image(os.path.splitext(path)[0] + '_Molten.jpg')
        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")


def molten(img):
    if img.mode != "RGB":
        img.convert("RGB")

    width, height = img.size
    pix = img.load()

    for w in range(width):
        for h in range(height):
            r, g, b = pix[w, h]

            pix[w, h] = min(255, int(abs(r * 128 / (g + b + 1)))), \
                        min(255, int(abs(g * 128 / (b + r + 1)))), \
                        min(255, int(abs(b * 128 / (r + g + 1))))

    return img
