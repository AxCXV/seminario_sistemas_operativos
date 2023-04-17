import tkinter as tk
from PIL import Image, ImageTk
import threading
import time

class MoveImageThread(threading.Thread):
    def __init__(self, canvas, img_id, x_step, y_step, steps, delay):
        threading.Thread.__init__(self)
        self.canvas = canvas
        self.img_id = img_id
        self.x_step = x_step
        self.y_step = y_step
        self.steps = steps
        self.delay = delay
    
    def run(self):
        for i in range(self.steps):
            self.canvas.move(self.img_id, self.x_step, self.y_step)
            self.canvas.update()
            time.sleep(self.delay)

class ImageAnimator:
    def __init__(self, canvas):
        self.canvas = canvas
        self.img1 = Image.open("practica6\pato1.jpg").resize((200, 200))
        self.img2 = Image.open("practica6\si.jpg").resize((200, 200))
        self.tk_img1 = ImageTk.PhotoImage(self.img1)
        self.tk_img2 = ImageTk.PhotoImage(self.img2)
        self.img_id1 = self.canvas.create_image(0, 100, anchor=tk.NW, image=self.tk_img1)
        self.img_id2 = self.canvas.create_image(200, 0, anchor=tk.NW, image=self.tk_img2)
        self.move_thread1 = MoveImageThread(self.canvas, self.img_id1, 0, -2, 200, 0.01)
        self.move_thread2 = MoveImageThread(self.canvas, self.img_id2, -2, 0, 200, 0.01)
        self.is_running = False

    def start_animation(self):
        if not self.is_running:
            self.is_running = True
            self.move_thread1.start()
            self.move_thread2.start()
    
    def stop_animation(self):
        if self.is_running:
            self.is_running = False
            self.move_thread1 = MoveImageThread(self.canvas, self.img_id1, 0, 2, 200, 0.01)
            self.move_thread2 = MoveImageThread(self.canvas, self.img_id2, 2, 0, 200, 0.01)
            self.move_thread1.start()
            self.move_thread2.start()

root = tk.Tk()

root.geometry("600x600")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

animator = ImageAnimator(canvas)

button = tk.Button(root, text="Start", command=animator.start_animation)
button.pack()

root.bind("<Escape>", lambda event: animator.stop_animation())

root.mainloop()
