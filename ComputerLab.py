# Reza Sobhani (93990218)
from tkinter import *
from tkinter import filedialog
import Sketch
import Ice
import Comic
import Sepia
import Darkness
import Aqua
import OilPainting
import Molten
import FaceDetection

root = Tk()
root.title('Image Processing')
root.geometry("500x500")
pathString = StringVar()


def pickImage():
    file = filedialog.askopenfilename(title="Choose an Image File")
    print(file)
    # Using try in case user types in unknown file or closes without choosing a file.
    try:
        if file:
            pathString.set(file)
            return file
    except:
        print("error in loading image")


pick_btn = Button(root, text="Pick Image", command=pickImage, width=20, bg="green")
pick_btn.pack()

sketch_btn = Button(root, text="Sketch", command=lambda: Sketch.do_sketch(pathString.get()), width=15)
sketch_btn.pack()

ice_btn = Button(root, text="Ice", command=lambda: Ice.do_ice(pathString.get()), width=15)
ice_btn.pack()

comic_btn = Button(root, text="Comic", command=lambda: Comic.do_comic(pathString.get()), width=15)
comic_btn.pack()

sepia_btn = Button(root, text="Sepia", command=lambda: Sepia.do_sepia(pathString.get()), width=15)
sepia_btn.pack()

darkness_btn = Button(root, text="Darkness", command=lambda: Darkness.do_darkness(pathString.get()), width=15)
darkness_btn.pack()

aqua_btn = Button(root, text="Aqua", command=lambda: Aqua.do_aqua(pathString.get()), width=15)
aqua_btn.pack()

oil_painting_btn = Button(root, text="Oil Painting", command=lambda: OilPainting.do_oil_painting(pathString.get()),
                          width=15)
oil_painting_btn.pack()

molten_btn = Button(root, text="Molten", command=lambda: Molten.do_molten(pathString.get()), width=15)
molten_btn.pack()

face_detection_btn = Button(root, text="Face Detection",
                            command=lambda: FaceDetection.do_face_detection(pathString.get()), width=15)
face_detection_btn.pack()

root.mainloop()
