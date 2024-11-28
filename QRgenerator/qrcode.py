import pyqrcode
from tkinter import *
from PIL import Image, ImageTk


def generate():
    name = entry_name.get()
    link = entry_link.get()
    file_name = name + '.png'
    qr = pyqrcode.create(link)
    qr.png(file_name, scale=5)
    img = Image.open(file_name)  # Corrected 'Image' instantiation
    img = ImageTk.PhotoImage(img)
    qr_label = Label(root, image=img)
    qr_label.image = img  # Keep a reference to the image to prevent garbage collection
    qr_label.pack(padx=10, pady=10)


root = Tk()
root.geometry('300x300')  # Increased the height to accommodate the QR code image

Label(root, text="QR Code Generator", fg="blue", font=("Arial", 14)).pack(padx=20, pady=15)

Label(root, text="Enter QR name :").pack(padx=20)

entry_name = Entry(root)  # Corrected the width
entry_name.pack(padx=20)

Label(root).pack(pady=13)

Label(root, text="Enter Link :").pack(padx=20)

entry_link = Entry(root, width=30)  # Corrected the width
entry_link.pack(padx=20)

btn = Button(root, text="Generate", fg="green", command=generate)
btn.pack(padx=20, pady=10)

root.mainloop()
