import os
from tkinter import messagebox


def show_Image(path):
    try:
        os.startfile(path)
    except:
        messagebox.showerror("Error", "Error in opening Image")
