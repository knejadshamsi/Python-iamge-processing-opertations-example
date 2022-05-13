from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Iamge flipper")
window = Canvas(window, width=1200, height=1200)
window.pack()
theImage = Image.open("camera_man.png")
Image_flip_hor = theImage.transpose(Image.FLIP_LEFT_RIGHT)
Image_flip_ver = theImage.transpose(Image.FLIP_TOP_BOTTOM)
Image_flip_ver_hor = Image_flip_ver.transpose(Image.FLIP_LEFT_RIGHT)

tk_image = ImageTk.PhotoImage(theImage)
tk_image_flip_hor = ImageTk.PhotoImage(Image_flip_hor)
tk_image_flip_ver = ImageTk.PhotoImage(Image_flip_ver)
tk_Image_flip_ver_hor = ImageTk.PhotoImage(Image_flip_ver_hor)

window.create_image(0, 0, anchor=NW, image=tk_image)
window.create_image(520, 0, anchor=NW, image=tk_image_flip_hor)
window.create_image(0, 520, anchor=NW, image=tk_image_flip_ver)
window.create_image(520, 520, anchor=NW, image=tk_Image_flip_ver_hor)


window.mainloop()
