import threading
import tkinter as tk
from PIL import Image, ImageTk

class ImageMoveThread(threading.Thread):
    def __init__(self, canvas, image_id, delta_x=0, delta_y=0, sleep_time=0.01):
        threading.Thread.__init__(self)
        self.canvas = canvas
        self.image_id = image_id
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.sleep_time = sleep_time
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            x, y = self.canvas.coords(self.image_id)
            new_x = x + self.delta_x
            new_y = y + self.delta_y
            self.canvas.coords(self.image_id, new_x, new_y)
            self.canvas.update()
            self.stop_event.wait(self.sleep_time)
    
    def stop(self):
        self.stop_event.set()

class ImageMoveApp:
    def __init__(self, master):
        self.master = master
        self.master.wm_attributes('-fullscreen', True)
        self.canvas = tk.Canvas(master)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.image1 = Image.open("pato1.jpg")
        self.image2 = Image.open("si.jpg")
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.image1_id = self.canvas.create_image(0, 0, image=self.photo1, anchor="nw")
        self.image2_id = self.canvas.create_image(0, 0, image=self.photo2, anchor="nw")
        self.move_thread1 = None
        self.move_thread2 = None
        self.button = tk.Button(master, text="Start", command=self.start_animation)
        self.button.pack()
    
    def start_animation(self):
        if self.move_thread1 is None:
            self.move_thread1 = ImageMoveThread(self.canvas, self.image1_id, delta_x=2)
            self.move_thread1.start()
        if self.move_thread2 is None:
            self.move_thread2 = ImageMoveThread(self.canvas, self.image2_id, delta_y=2)
            self.move_thread2.start()
    
    def stop_animation(self):
        if self.move_thread1 is not None:
            self.move_thread1.stop()
            self.move_thread1 = None
        if self.move_thread2 is not None:
            self.move_thread2.stop()
            self.move_thread2 = None

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageMoveApp(root)
    root.title("Threads")
    root.mainloop()
