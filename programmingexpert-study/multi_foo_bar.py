from threading import Thread, Lock

def foo(n, foo_lock, bar_lock):
    for _ in range(n):
        foo_lock.acquire()
        print(end="foo")
        bar_lock.release()


def bar(n, foo_lock, bar_lock):
    for _ in range(n):
        bar_lock.acquire()
        print(end="bar")
        foo_lock.release()


foo_lock = Lock()
bar_lock = Lock()
bar_lock.acquire()

n = int(input("Enter a positive integer: "))

thread1 = Thread(target=foo, args=(n, foo_lock, bar_lock))
thread2 = Thread(target=bar, args=(n, foo_lock, bar_lock))

thread1.start()
thread2.start()

thread1.join()
thread2.join()