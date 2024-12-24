import threading
# solution use RLock()
lock_obj = threading.Lock()

print('Acquaire 1st time')
lock_obj.acquire()

print('Acquaire 2st time')
lock_obj.acquire()

print('Release')
lock_obj.release()

# infinite recursia


def boom():
    lock_obj = threading.Lock()
    print('Start')
    lock_obj.acquire()
    print('End')
    boom()


boom()
