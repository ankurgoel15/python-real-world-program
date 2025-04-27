import PIL
from PIL import ImageTk
from tkinter import *
from qrcode import *
import qrcode

def generate_qr():

    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"

    qr = qrcode.QRCode(version=1, error_correction= ERROR_CORRECT_L)
    qr.add_data(link)

    img = qr.make_image(file_color="black", back_color="white")
    qr.make(fit=True)
    img.save(file_name)

    image_open = PIL.Image.open(file_name)
    image = ImageTk.PhotoImage(image_open)

    image_label = Label(root, image=image)
    image_label.image = image
    canvas.create_window(330, 350, window=image_label)

root = Tk()
root.title('QR Code Generator')

canvas = Canvas(root, width=700, height=700)
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg="blue", font=('Arial', 30))
canvas.create_window(330, 50, window=app_label)

name_label = Label(root, text="Link name")
canvas.create_window(330, 100, window=name_label)
name_entry = Entry(root)
canvas.create_window(330, 120, window=name_entry)

link_label = Label(root, text="Link")
canvas.create_window(330, 160, window=link_label)
link_entry = Entry(root)
canvas.create_window(330, 180, window=link_entry)

button = Button(text="Generate QR", command=generate_qr)
canvas.create_window(330, 230, window=button)

root.mainloop()