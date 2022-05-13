from tkinter import *
from PIL import ImageTk, Image , ImageEnhance

window = Tk()
window.title("Image gama manipulator")
window = Canvas(window, width=1200, height=1200)
window.pack()
theImage = Image.open("camera_man.png")
reImage= theImage.resize((300,300))
enhancer = ImageEnhance.Brightness(reImage)
factor = 1.3 , 1.75 , 0.65 , 0.25
bright1 = enhancer.enhance(factor[0])
bright2 = enhancer.enhance(factor[1])
darken1 = enhancer.enhance(factor[2])
darken2 = enhancer.enhance(factor[3])



tk_image = ImageTk.PhotoImage(reImage)
tk_image2 = ImageTk.PhotoImage(bright1)
tk_image3 = ImageTk.PhotoImage(bright2)
tk_image4 = ImageTk.PhotoImage(darken1)
tk_image5 = ImageTk.PhotoImage(darken2)


window.create_image(0, 0, anchor=NW, image=tk_image)
window.create_image(300, 0, anchor=NW, image=tk_image2)
window.create_image(600, 0, anchor=NW, image=tk_image3)
window.create_image(300, 300, anchor=NW, image=tk_image4)
window.create_image(600, 300, anchor=NW, image=tk_image5)


window.mainloop()
