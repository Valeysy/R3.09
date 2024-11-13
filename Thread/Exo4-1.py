from multiprocessing import Process
import time

def process1():
    for _ in range(5):
        print("Je suis le processus 1")
        time.sleep(0.5)

def process2():
    for _ in range(5):
        print("Je suis le processus 2")
        time.sleep(0.5)

if __name__ == '__main__':

    p1 = Process(target=process1)
    p2 = Process(target=process2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()