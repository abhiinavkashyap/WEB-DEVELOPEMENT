import time
import threading
def one(name):
    print(name)
    print(time.ctime())
    time.sleep(4)
    #print(time.ctime())
def two(name):
    print(name)
    print(time.ctime())
t1 = threading.Thread(target=one, args=["dhoni"])
t2 = threading.Thread(target=one, args=["kohli"])
t1.start()
t2.start()
t1.join()
t2.join()
