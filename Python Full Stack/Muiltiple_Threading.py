#1. By Explicitly using a Function
'''
from threading import current_thread, Thread

def fun(start, stop, step):
    for i in range(start, stop, step):
        print(i, current_thread().name)

evens = Thread(target = fun, args = (2,11,2))
odds = Thread(target = fun, args = (1,11,2))

evens.start()
odds.start()
'''

#2. Without Inheriting the Thread Class
'''
from threading import Thread

class Num():
    def eot(self, start, stop, step):
        for i in range(start, stop, step):
            print(i)

obj = Num()

t1 = Thread(target = obj.eot, args = (1,11,2))
t2 = Thread(target = obj.eot, args = (2,11,2))

t1.start()
t2.start()
'''

#3. By Inheriting the Thread Class
'''
from threading import Thread

class Num(Thread):
    def __init__(self, startt, stop, step):
        Thread.__init__(self)
        self.startt = startt
        self.stop = stop
        self.step = step

    def run(self):
        for i in range(self.startt, self.stop, self.step):
            print(i)

e = Num(2,11,2)
o = Num(1,11,2)

e.start()
o.start()
'''

#RACE Condition

#1. By Using JOIN Method
'''
from threading import Thread

def m1(msg):
    print('[[')
    print(msg)
    print(']]')

t1 = Thread(target = m1, args = ('JAVA', ))
t2 = Thread(target = m1 , args = ('PYTHON', ))
t3 = Thread(target = m1, args = ('Cloud', ))

t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
'''

#2. By Using locking Mechanism

from threading import Thread, Lock

l = Lock()

def m1(msg):
    l.acquire()
    print('[[')
    print(msg)
    print(']]')
    l.release()

t1 = Thread(target = m1, args = ('JAVA', ))
t2 = Thread(target = m1 , args = ('PYTHON', ))
t3 = Thread(target = m1, args = ('Cloud', ))

t1.start()
t2.start()
t3.start()







