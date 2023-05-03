import threading
import random
import time
import tkinter as tk


PARKING_LOT_SIZE = 12

ADD_CAR_FREQ = 0.5

REMOVE_CAR_FREQ = 0.5

parking_lot = [None] * PARKING_LOT_SIZE

add_car_running = True

remove_car_running = True

def add_car():
    global parking_lot
    global add_car_running
    while add_car_running:
        time.sleep(random.uniform(1, 2) / ADD_CAR_FREQ)
        if None in parking_lot:
            index = parking_lot.index(None)
            parking_lot[index] = "car"
            print("Car parked in spot", index)
        else:
            print("Parking lot is full")

def remove_car():
    global parking_lot
    global remove_car_running
    while remove_car_running:
        time.sleep(random.uniform(1, 2) / REMOVE_CAR_FREQ)
        if "car" in parking_lot:
            index = parking_lot.index("car")
            parking_lot[index] = None
            print("Car removed from spot", index)
        else:
            print("No cars in the parking lot")

def update_display():
    global parking_lot
    while True:
        canvas.delete("all")
        for i in range(PARKING_LOT_SIZE):
            if parking_lot[i] is not None:
                canvas.create_rectangle(50 * i, 0, 50 * (i+1), 50, fill="red")
            else:
                canvas.create_rectangle(50 * i, 0, 50 * (i+1), 50, fill="green")
        root.update()
        time.sleep(0.1)

def add_car_button():
    global ADD_CAR_FREQ
    ADD_CAR_FREQ += 0.1
    print("Added car frequency:", ADD_CAR_FREQ)

def remove_car_button():
    global REMOVE_CAR_FREQ
    REMOVE_CAR_FREQ += 0.1
    print("Removed car frequency:", REMOVE_CAR_FREQ)

def stop_button():
    global add_car_running
    global remove_car_running
    add_car_running = False
    remove_car_running = False
    print("Process stopped")

def reduce_freq_button():
    global ADD_CAR_FREQ
    global REMOVE_CAR_FREQ
    ADD_CAR_FREQ -= 0.1
    REMOVE_CAR_FREQ -= 0.1
    print("Reduced car frequencies:", ADD_CAR_FREQ, REMOVE_CAR_FREQ)


root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=50)
canvas.pack()

add_car_button = tk.Button(root, text="Increase Add Car Frequency", command=add_car_button)
add_car_button.pack(side="left")
remove_car_button = tk.Button(root, text="Increase Remove Car Frequency", command=remove_car_button)
remove_car_button.pack(side="left")
stop_button = tk.Button(root, text="Stop Process", command=stop_button)
stop_button.pack(side="left")
reduce_freq_button = tk.Button(root, text="Reduce Frequencies", command=reduce_freq_button)
reduce_freq_button.pack(side="left")

parking_lot_thread = threading.Thread(target=update_display)
parking_lot_thread.start()

add_car_thread = threading.Thread(target=add_car)
add_car_thread.start()

remove_car_thread = threading.Thread(target=remove_car)
remove_car_thread.start()

root.mainloop()
