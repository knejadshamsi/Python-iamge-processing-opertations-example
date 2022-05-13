from tkinter import *
from PIL import ImageTk, Image , ImageEnhance
import numpy as np
from numpy.core.fromnumeric import shape

window = Tk()
window.title("image saturation")
window = Canvas(window, width=1200, height=1200)
window.pack()
theImage = Image.open("colorfullBalls.png")
reImage= theImage.resize((300,300))

hsv_img = reImage.convert('HSV') # 'HSV' is the same as 'HSI'
hsv = np.array(hsv_img) # gives us a 3 dementional array ( here it will be (300,300,3) )
hsv[:,:,1] = (hsv[:,:,1]+ 1000) % 360 
new_img = Image.fromarray(hsv, 'HSV')
new_img.convert('RGB')

tk_image = ImageTk.PhotoImage(reImage)
tk_image2 = ImageTk.PhotoImage(new_img)

window.create_image(0, 0, anchor=NW, image=tk_image)
window.create_image(310, 0, anchor=NW, image=tk_image2)

window.mainloop()
