from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Multimedia Application")

image = Image.open('eren.jpeg')
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.pack()
label.image = photo

root.mainloop()
