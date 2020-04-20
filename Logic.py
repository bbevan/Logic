# Primitive Element
def Nand(a,b):
    # return 0 only if a == b
    if (a == 1) and b == 1:
        return 0
    else:
        return 1


# Combinational Logic
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


# ---------------------------------------------
# Sequential Logic
#----------------------------------------------


class SRLatch:
    def __init__(self):

        # let q and nq be the outputs
        self.q = 0
        self.nq = 1

    def circuit(self,s,r):
        nots = Not(s)
        notr = Not(r)

        temp = self.q

        # Q = NS NAND NQ
        self.q = Nand(self.nq, nots)

        # NQ = NR NAND Q
        self.nq = Nand(temp, notr)

    def set(self):
        self.circuit(1,0)

    def reset(self):
        self.circuit(0,1)
    
