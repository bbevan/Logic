from Clock_Alpha import ClockedAnd, Clock
from Logic import And
import threading
import time

class EventedThreadedClock(Clock, threading.Thread):

    def __init__(self, event):
        self.state = Clock.__init__(self)
        threading.Thread.__init__(self)
        self.event = event

    def run(self):
        while(1):
            self.update_state()
            self.event.set()
            self.event.clear()
            time.sleep(1)


def EventedClockedAnd(bit1, clockstate, event):
    print("About to wait.")
    event.wait()
    print("And'ing.")
    result = And(bit1, clockstate)
    print(str(result))

class EventedClockedAndObject(threading.Thread):
    def __init__(self, event):
        self.event = event
        threading.Thread.__init__(self)

    def run(self):
        while(1):
            self.event.wait()
            result = And(1,1)
            print(result)



if __name__ == '__main__':
    print("In main.")

    Clock_Ready = threading.Event()


    # spawn an EventedThreadedClock
    etc = EventedThreadedClock(Clock_Ready)
    etc.start()

    #EventedClockedAnd(1, 1, Clock_Ready)
    cl = EventedClockedAndObject(Clock_Ready)
    cl.start()


