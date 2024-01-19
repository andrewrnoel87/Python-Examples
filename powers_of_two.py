import threading

RANGE_START = 0
RANGE_END = 1000

"""
At the end of the program, this variable needs to contain all of the powers
of 2 within the interval [RANGE_START, RANGE_END).
"""
powers_of_two = set()
set_lock = threading.Lock()


def is_power_of_two(x):
    if x == 0:
        return False
    return (x & (x - 1)) == 0


def find_powers_of_two(iter):
    for item in iter:
        if is_power_of_two(item):
            set_lock.acquire()  #  protect our set data structure with locks
            powers_of_two.add(item)
            set_lock.release()


# create threads
thread1 = threading.Thread(target=find_powers_of_two, args=(range(RANGE_START, 200),))
thread2 = threading.Thread(target=find_powers_of_two, args=(range(200, 400),))
thread3 = threading.Thread(target=find_powers_of_two, args=(range(400, 600),))
thread4 = threading.Thread(target=find_powers_of_two, args=(range(600, 800),))
thread5 = threading.Thread(target=find_powers_of_two, args=(range(800, RANGE_END),))

# start threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

# wait for threads to finish
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()