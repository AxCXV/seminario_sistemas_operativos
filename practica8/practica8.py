import threading
import time
import random

current_num = 0
lock = threading.Lock()

def writer(filename, frequency):
    global current_num
    while True:
        with lock:
            current_num += 1
            with open(filename, 'a') as f:
                f.write(str(current_num) + '\n')
        time.sleep(random.uniform(frequency*0.5, frequency*2.0))

def reader(filename, frequency):
    while True:
        with lock:
            with open(filename, 'r') as f:
                lines = f.readlines()
            print(''.join(lines))
        time.sleep(random.uniform(frequency*1.0, frequency*2.0))

writer1 = threading.Thread(target=writer, args=('threads.txt', 0.5,))
writer2 = threading.Thread(target=writer, args=('threads.txt', 1.0,))
writer3 = threading.Thread(target=writer, args=('threads.txt', 2.0,))

reader1 = threading.Thread(target=reader, args=('threads.txt', 1.0,))
reader2 = threading.Thread(target=reader, args=('threads.txt', 1.5,))
reader3 = threading.Thread(target=reader, args=('threads.txt', 2.0,))

writer1.start()
writer2.start()
writer3.start()
reader1.start()
reader2.start()
reader3.start()

writer1.join()
writer2.join()
writer3.join()
reader1.join()
reader2.join()
reader3.join()