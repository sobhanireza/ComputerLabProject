from PIL import Image
import sys
import os
from tkinter import messagebox
import ShowImage


def do_sketch(path):
    # path = pathString.get()
    if path:
        try:
            threshold = 9

            if len(sys.argv) == 2:
                try:
                    threshold = int(sys.argv[1])
                except ValueError:
                    path = sys.argv[1]
            elif len(sys.argv) == 3:
                path = sys.argv[1]
                threshold = int(sys.argv[2])

            img = Image.open(path)
            img = sketch(img, threshold)
            img.save(os.path.splitext(path)[0] + '_Sketch.jpg', 'JPEG')
            messagebox.showinfo("Successful", "Successfully Done")

            ShowImage.show_Image(os.path.splitext(path)[0] + '_Sketch.jpg')
        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")


def sketch(img, threshold):
    if threshold < 0: threshold = 0
    if threshold > 100: threshold = 100

    width, height = img.size
    img = img.convert('L')  # convert to grayscale mode
    pix = img.load()  # get pixel matrix

    for w in range(width):
        for h in range(height):
            if w == width - 1 or h == height - 1:
                continue

            src = pix[w, h]
            dst = pix[w + 1, h + 1]

            diff = abs(src - dst)

            if diff >= threshold:
                pix[w, h] = 0
            else:
                pix[w, h] = 255

    return img
