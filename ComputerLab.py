#Reza Sobhani (93990218)
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import sys
import os
import cv2

root = Tk()
root.title('Image Processing')
root.geometry("500x500")
pathString = StringVar()


def do_oil_painting():
    path = pathString.get()
    if path:
        try:
            brush_size = 2
            roughness = 100

            if len(sys.argv) >= 3:
                brush_size = int(sys.argv[1])
                roughness = int(sys.argv[2])
            if len(sys.argv) == 4:
                path = sys.argv[3]

            img = Image.open(path)
            img = oil_painting(img, brush_size, roughness)
            img.save(os.path.splitext(path)[0] + '_OilPainting.png', 'PNG')
            messagebox.showinfo("Successful", "Successfully Done")
            show_Image(os.path.splitext(path)[0] + '_OilPainting.png')
        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")


def oil_painting(img, brush_size, roughness):
    if brush_size < 1: brush_size = 1
    if brush_size > 8: brush_size = 8

    if roughness < 1: roughness = 1
    if roughness > 255: roughness = 255

    width, height = img.size

    gray_img = img.convert("L")
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    dst_img = Image.new("RGBA", (width, height))

    gray_pix = gray_img.load()
    pix = img.load()
    dst_pix = dst_img.load()

    arr_len = roughness + 1
    count = [0 for i in range(arr_len)]
    A = [0 for i in range(arr_len)]
    R = [0 for i in range(arr_len)]
    G = [0 for i in range(arr_len)]
    B = [0 for i in range(arr_len)]

    def reset():
        for arr in (count, A, R, G, B):
            for i in range(arr_len):
                arr[i] = 0

    for w in range(width):
        left = w - brush_size
        if left < 0:
            left = 0

        right = w + brush_size
        if right > width - 1:
            right = width - 1

        for h in range(height):
            top = h - brush_size
            if top < 0:
                top = 0

            bottom = h + brush_size
            if bottom > height - 1:
                bottom = height - 1

            reset()

            for i in range(left, right + 1):
                for j in range(top, bottom + 1):
                    intensity = int(gray_pix[i, j] * roughness / 255)
                    count[intensity] += 1
                    p = pix[i, j]
                    A[intensity] += p[3]
                    R[intensity] += p[0]
                    G[intensity] += p[1]
                    B[intensity] += p[2]

            max_ins_count = max(count)
            max_idx = count.index(max_ins_count)

            dst_pix[w, h] = int(R[max_idx] / max_ins_count), \
                            int(G[max_idx] / max_ins_count), \
                            int(B[max_idx] / max_ins_count), \
                            int(A[max_idx] / max_ins_count)

    return dst_img


def do_aqua():
    path = pathString.get()
    if path:
        try:
            if len(sys.argv) == 2:
                path = sys.argv[1]

            img = Image.open(path)
            img = aqua(img)
            img.save(os.path.splitext(path)[0] + '_Aqua.jpg', 'JPEG')
            messagebox.showinfo("Successful", "Successfully Done")
            show_Image(os.path.splitext(path)[0] + '_Aqua.jpg')
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


def do_darkness():
    path = pathString.get()
    if path:
        try:
            if len(sys.argv) == 2:
                path = sys.argv[1]

            img = Image.open(path)
            img = darkness(img)
            img.save(os.path.splitext(path)[0] + '_Darkness.jpg', 'JPEG')
            messagebox.showinfo("Successful", "Successfully Done")
            show_Image(os.path.splitext(path)[0] + '_Darkness.jpg')
        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")


def darkness(img):
    return img.point(lambda i: int(i ** 2 / 255))


def do_face_identification():
    path = pathString.get()
    if path:
        try:
            messagebox.showerror("Error", "Please wait for library to download")

        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")


def do_face_detection():
    path = pathString.get()
    if path:
        try:
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
            img = cv2.imread(path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray,
                                                  scaleFactor=2,
                                                  minNeighbors=5,
                                                  minSize=(30, 30)
                                                  )

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                im_gray = gray[y:y + h, x:x + w]
                im_color = img[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(im_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(im_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # show_Image()

            cv2.imwrite(os.path.splitext(path)[0] + '_Face.jpg', img)
            # cv2.imshow('image', img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            messagebox.showinfo("Successful", "Successfully Done")
            show_Image(os.path.splitext(path)[0] + '_Face.jpg')

        except:
            messagebox.showerror("Error", "Error in image processing")
    else:
        messagebox.showerror("Error", "Please load an image")


def do_sepia():
    path = pathString.get()
    if path:
        try:
            if len(sys.argv) > 1:
                path = sys.argv[1]
            img = Image.open(path)
            img = sepia(img)
            img.save(os.path.splitext(path)[0] + '_Sepia.jpg', 'JPEG')
            messagebox.showinfo("Successful", "Successfully Done")
            show_Image(os.path.splitext(path)[0] + '_Sepia.jpg')

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

            R = (25756 * cr_p[0] + 50397 * cr_p[1] + 12386 * cr_p[2]) >> 16
            G = (22872 * cr_p[0] + 44958 * cr_p[1] + 11010 * cr_p[2]) >> 16
            B = (17826 * cr_p[0] + 34996 * cr_p[1] + 8585 * cr_p[2]) >> 16

            if R < 0: R = 0
            if R > 255: R = 255

            if G < 0: G = 0
            if G > 255: G = 255

            if B < 0: B = 0
            if B > 255: B = 255

            pix[w, h] = R, G, B

    return img


def do_comic():
    path = pathString.get()
    if path:
        try:
            path = pathString.get()
            if len(sys.argv) == 2:
                path = sys.argv[1]

            img = Image.open(path)
            img = comic(img)
            img.save(os.path.splitext(path)[0] + '_Comic.jpg', 'JPEG')
            messagebox.showinfo("Successful", "Successfully Done")
            show_Image(os.path.splitext(path)[0] + '_Comic.jpg')
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


def do_ice():
    path = pathString.get()
    if path:
        try:
            if len(sys.argv) == 2:
                path = sys.argv[1]

            img = Image.open(path)
            img = ice(img)
            img.save(os.path.splitext(path)[0] + '_Ice.jpg', 'JPEG')
            messagebox.showinfo("Successful", "Successfully Done")
            show_Image(os.path.splitext(path)[0] + '_Ice.jpg')
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


def do_sketch():
    path = pathString.get()
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
            show_Image(os.path.splitext(path)[0] + '_Sketch.jpg')
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


def show_Image(path):
    # imgs = cv2.imread("D:/University/Term 8 (97-98 P1)/Kargah Computer/Project/2/images/lam.sketch.jpg", 1)
    # cv2.namedWindow('jpg', cv2.WINDOW_AUTOSIZE)
    # image = cv2.imread(path)
    # cv2.resize(image, (500, 500))
    # cv2.imshow('image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # image = Image.open(path)
    # image.show()

    # im = cv2.imread(path)
    # plt.imshow(im)
    # plt.show()

    os.system("powershell -c "+path)


pick_btn = Button(root, text="Pick Image", command=pickImage, width=20, bg="green")
pick_btn.pack()

sketch_btn = Button(root, text="Sketch", command=do_sketch, width=15)
sketch_btn.pack()

ice_btn = Button(root, text="Ice", command=do_ice, width=15)
ice_btn.pack()

comic_btn = Button(root, text="Comic", command=do_comic, width=15)
comic_btn.pack()

sepia_btn = Button(root, text="Sepia", command=do_sepia, width=15)
sepia_btn.pack()

face_detection_btn = Button(root, text="Face Detection", command=do_face_detection, width=15)
face_detection_btn.pack()

face_identication_btn = Button(root, text="Face Identification", command=do_face_identification, width=15)
face_identication_btn.pack()

darkness_btn = Button(root, text="Darkness", command=do_darkness, width=15)
darkness_btn.pack()

aqua_btn = Button(root, text="Aqua", command=do_aqua, width=15)
aqua_btn.pack()

oil_painting_btn = Button(root, text="Oil Painting", command=do_oil_painting, width=15)
oil_painting_btn.pack()

root.mainloop()
