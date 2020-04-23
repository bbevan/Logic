# Primitive Elements & Such ---------------------------------------------------------------------
def Nand(a,b):
    # return 0 only if a == b == 1
    if (a == 1) and b == 1:
        return 0
    else:
        return 1

# Clock
import threading
import time
class Clock(threading.Thread):
    def __init__(self):
        self.e = threading.Event()
        self.bit = 0

    def run(self):
        while(1):
            print("In the Clock.")
            self.state()
            self.e.set()
            time.sleep(1)
            self.e.clear()

    def move_forward(self):
        if self.bit == 0:
            self.bit = 1
        else:
            self.bit = 0

    def get_e(self):
        return self.e

# Evented Logic Element
from threading import Thread
class EventedElement(threading.Thread):
    def __init__(self, event):
        self.event = event
        threading.Thread.__init__(self)

    def run(self):
        while(1):
            self.event.wait()
            result = logic()
            print(result)

    def logic(self):
        pass

# Clock base class
class Clock:
    def __init__(self):
        # states
        self.state = 0

    def update_state(self):
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0

        return 0

# Evented Threaded Clock
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

class EventedElement(threading.Thread):
    def __init__(self, event):
        self.event = event
        threading.Thread.__init__(self)

    def run(self):
        while(1):
            self.event.wait()
            result = logic()
            print(result)

    def logic(self):
        pass


# Combinational Logic -----------------------------------------------------------------
def Not(a):
    # Working now
    return Nand(a,1)

def And(a,b):
    # invert the output of nand
    return Not(Nand(a,b))

def Or(a,b):
    # invert both inputs, nand the outputs together
    nota = Not(a)
    notb = Not(b)
    return Nand(nota, notb)

def Nor(a,b):
    return Not(Or(a,b))

def Xor(a,b):
    # xor = ab + ~a~b
    notA = Not(a)
    notB = Not(b)

    aAndB = And(a,b)
    naAndnB = And(notA, notB)

    return Or(aAndB, naAndB)

def Multiplexor(a,b,s):
    # mux = a~s + bs
    notS = Not(s)

    aNotS = And(a,notS)
    bAndS = And(b,s)

    return Or(aNotS, bAndS)

# The Demux may require an object (?)
# how am i connecting things together?

# TODO: Decimal to Binary Converter



# ---------------------------------------------
# Sequential Logic
#----------------------------------------------

# SR Latch Class
class SRLatch:
    def __init__(self):

        # let q and nq be the outputs
        # and also the state variables
        self.q = 0
        self.nq = 1

    def circuit(self,s,r):
        nots = Not(s)
        notr = Not(r)

        # Hold the last state in variable temp
        temp = self.q

        # Run the next state
        if (s == 1 and r == 0):
            # set state
            # in this case, run the circuit one way
            self.q = Nand(self.nq, nots)
            self.nq = Nand(temp, notr)
        elif (s == 0 and r == 1):
            # reset state
            # in this case, run the circuit the other way
            self.nq = Nand(temp, notr)
            self.q = Nand(self.nq, nots)
        
        # edge cases
        # not sure what to do here (!)
        # these are cases where the circuit method
        # is called outside of the API.
        elif (s == 0 and r== 0):
            pass
        else:
            pass
            

    # API: set(self, bit) , reset(self, bit)
    # Both ensure proper operation of the latch.
    def set(self, bit):
        self.circuit(1,0) if bit == 1 else self.circuit(0,0)

    def reset(self):
        #self.circuit(0,1)
        self.circuit(0,1)

# Clocked SR Latch
class EventedClockedSRLatch(threading.Thread):
    def __init__(self, event):
        self.q1 = 1
        self.nq1 = 0
        self.q2 = 1
        self.nq2 = 0
        self.clockstate = 0

        threading.Thread.__init__(self)
        self.event = event

    #API
    def set(self, bit):
        pass

    def reset(self):
        pass

    def run(self):
        while(1):
            self.event.wait()
            self.logic(1,0)
            print(self.q2)

    def update_clockstate(self, state):
        self.clockstate = state
    
    # Circuit
    def logic(self, s, r):

        temp1 = self.q2
        temp2 = self.nq2
        
        # run the next state
        if self.clockstate == 1:

            self.q1 = Nand(s, self.clockstate)
            self.nq1 = Nand(self.clockstate, r)

            # Run the next state
            if (s == 1 and r == 0):                
                self.q2 = Nand(self.q1, temp2)
                self.nq = Nand(temp1, self.nq2)
            elif (s == 0 and r == 1):
                # reset state
                # in this case, run the circuit the other way
                Nand(temp1, self.nq2)
                self.q = Nand(self.q1, temp2)
            


# Register Class
# defines an 8-bit shift register
# Watch out for endianess (!)
# NOTE: It does not use the circuit
# abstraction. 
class Register:
    def __init__(self):
        self.register = []

        for i in range(0,7):
            self.register.append(SRLatch())

    def shift_in(self, bit):
        
        # shift first
        for i in range(1,7):
            self.register[7-i].reset()
            self.register[7-i].set( self.register[7-i-1].q )

        # set the new value for the first bit
        self.register[0].reset()
        self.register[0].set(bit)

    def shift_out(self):
        return self.register[7]

    def load(self, binary):
        for i in range(0,7):
            self.shift_in(binary[i])

# TODO: Write the Register class with clocked RS Latches.
# TODO: Write the Clocked RS Latch class.
# TODO: Write the Clock class.

if __name__ == '__main__':
    print("In main.")

    Clock_Ready = threading.Event()


    # spawn an EventedThreadedClock
    etc = EventedThreadedClock(Clock_Ready)
    etc.start()

    #EventedClockedAnd(1, 1, Clock_Ready)
    cl = EventedClockedSRLatch(Clock_Ready)
    cl.start()