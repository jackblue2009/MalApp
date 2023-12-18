import tkinter as tk
import cv2
from PIL import Image, ImageTk

def update_frame():
    ret, frame = cap.read()

    if ret:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resized_frame = cv2.resize(rgb_frame, (640, 480))
        image = Image.fromarray(resized_frame)
        photo = ImageTk.PhotoImage(image)

        image_label.configure(image=photo)
        image_label.image = photo
    
    image_label.after(10, update_frame)

window = tk.Tk()

window.title("Merraj Agent Console")

image_label = tk.Label(window)
image_label.pack()

cap = cv2.VideoCapture(0)

update_frame()

window.mainloop()

cap.release()
cv2.destroyAllWindows()