import threading
import time

def countdown1():
    for i in range(5, 0, -1):
        print(f"thread 1 : {i}")
        time.sleep(0.5)
        
def countdown2():
    for i in range(3, 0, -1):
        print(f"thread 2 : {i}")
        time.sleep(0.5)
        
t1 = threading.Thread(target=countdown1)
t2 = threading.Thread(target=countdown2)

t1.start()
t2.start()

t1.join()
t2.join()