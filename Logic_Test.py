from Logic import *

set_print = lambda bit : print("Bit set to 1") if myFF.q == bit else print("Set is not working.")
reset_print = lambda bit : print("Reset successful.") if myFF.q == bit else print("Reset is not working.")

def set_test(bit):
    myFF.set(bit)
    set_print(bit)

def reset_test(bit):
    myFF.reset()
    reset_print(bit)


# Not test
print("Not Test")
print(Not(0) == 1)
print(Not(1) == 0)

# Nand test
print("\nNand Test")
print(Nand(0,0) == 1)
print(Nand(0,1) == 1)
print(Nand(1,0) == 1)
print(Nand(1,1) == 0)

# FlipFlop Test
print("\nSRLatch Test")
myFF = SRLatch()

# set it
set_test(1)

# reset it
reset_test(0)

print("\nTest Again")
# set it
set_test(1)

print("\nSet 1 then set 1 again.")
set_test(1)
set_test(1)
reset_test(0)

# reset it many times
print("\n10 resets.")
i = 0
while(1):
    reset_test(0)

    i+=1

    if i == 10:
        break


# Register tests
myReg = Register()

print("\nShifting in bit 1.")
myReg.shift_in(1)
print("Shifted in bit 1. Actual value is " + str(myReg.register[0].q))

print("Shifting in the next value.")
print("Shifting in bit 0.")
myReg.shift_in(0)
print("Shifted in 0. Actual value is " + str(myReg.register[0].q))

print("\nShifting in bit 1.")
myReg.shift_in(1)
print("Shifted in bit 1. Actual value is " + str(myReg.register[0].q))

print("Shifting in the next value.")
print("Shifting in bit 0.")
myReg.shift_in(0)
print("Shifted in 0. Actual value is " + str(myReg.register[0].q))

print("\nLatches so far.")
for i in range(0,7):
    print( str(myReg.register[i].q) )

print("\nLoading Register via functions...")

myReg.load([1,0,1,0,1,0,1])
print("Shifted [1,0,1,0,1,0,1] via the load function.\n")

print("Latches: ")
for i in range(0,7):
    print( str(myReg.register[i].q) )
