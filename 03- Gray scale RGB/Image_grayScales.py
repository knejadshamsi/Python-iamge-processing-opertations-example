from tkinter import *
from PIL import ImageTk, Image , ImageEnhance


window = Tk()
window.title("Image grayscale")
window = Canvas(window, width=1200, height=1200)
window.pack()
theImage = Image.open("colorfullBalls.png")
reImage= theImage.resize((300,300))
img = Image.Image.split(reImage)

tk_image = ImageTk.PhotoImage(reImage)
tk_image2 = ImageTk.PhotoImage(img[0])
tk_image3 = ImageTk.PhotoImage(img[1])
tk_image4 = ImageTk.PhotoImage(img[2])


window.create_image(0, 0, anchor=NW, image=tk_image)
window.create_image(310, 0, anchor=NW, image=tk_image2)
window.create_image(620, 0, anchor=NW, image=tk_image3)
window.create_image(0, 310, anchor=NW, image=tk_image4)


window.mainloop()
