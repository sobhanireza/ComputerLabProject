import os
from tkinter import messagebox
import ShowImage
import cv2


def do_cartoonize(path):
    if path:
        try:
            img = cv2.imread(path)

            # 1) Edges
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

            # 2) Color
            color = cv2.bilateralFilter(img, 9, 300, 300)

            # 3) Cartoon
            cartoon = cv2.bitwise_and(color, color, mask=edges)

            cv2.imwrite(os.path.splitext(path)[0] + '_Cartoon.jpg', cartoon)
            messagebox.showinfo("Successful", "Successfully Done")
            ShowImage.show_Image(os.path.splitext(path)[0] + '_Cartoon.jpg')

        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")
