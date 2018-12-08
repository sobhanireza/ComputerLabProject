import os
from tkinter import messagebox
import ShowImage
import cv2


def do_face_detection(path):
    if path:
        try:
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            img = cv2.imread(path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray,
                                                  scaleFactor=2,
                                                  minNeighbors=5,
                                                  minSize=(30, 30)
                                                  )

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imwrite(os.path.splitext(path)[0] + '_FaceDetection.jpg', img)
            messagebox.showinfo("Successful", "Successfully Done")
            ShowImage.show_Image(os.path.splitext(path)[0] + '_FaceDetection.jpg')

        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")

