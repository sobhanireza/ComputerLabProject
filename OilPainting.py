from PIL import Image
import sys
import os
from tkinter import messagebox
import ShowImage



def do_oil_painting(path):
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
            ShowImage.show_Image(os.path.splitext(path)[0] + '_OilPainting.png')
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