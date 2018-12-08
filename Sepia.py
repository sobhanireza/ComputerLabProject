from PIL import Image
import sys
import os
from tkinter import messagebox
import ShowImage


def do_sepia(path):
    if path:
        try:
            if len(sys.argv) > 1:
                path = sys.argv[1]
            img = Image.open(path)
            img = sepia(img)
            img.save(os.path.splitext(path)[0] + '_Sepia.jpg', 'JPEG')
            messagebox.showinfo("Successful", "Successfully Done")
            ShowImage.show_Image(os.path.splitext(path)[0] + '_Sepia.jpg')

        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")


def sepia(img):
    width, height = img.size

    pix = img.load()

    for w in range(width):
        for h in range(height):
            cr_p = pix[w, h]

            r = (25756 * cr_p[0] + 50397 * cr_p[1] + 12386 * cr_p[2]) >> 16
            g = (22872 * cr_p[0] + 44958 * cr_p[1] + 11010 * cr_p[2]) >> 16
            b = (17826 * cr_p[0] + 34996 * cr_p[1] + 8585 * cr_p[2]) >> 16

            if r < 0: r = 0
            if r > 255: r = 255

            if g < 0: g = 0
            if g > 255: g = 255

            if b < 0: b = 0
            if b > 255: b = 255

            pix[w, h] = r, g, b

    return img
