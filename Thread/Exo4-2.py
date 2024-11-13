from multiprocessing import Process
import time

def countdown_process1():
    for i in range(5, 0, -1):
        print(f"processus 1 : {i}")
        time.sleep(0.5)

def countdown_process2():
    for i in range(3, 0, -1):
        print(f"processus 2 : {i}")
        time.sleep(0.5)

if __name__ == '__main__':
    p1 = Process(target=countdown_process1)
    p2 = Process(target=countdown_process2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()