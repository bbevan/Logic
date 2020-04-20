from Logic import *

# Not test
print("Not Test")
print(Not(0))
print(Not(1))

# Nand test
print("Nand Test")
print(Nand(0,0))
print(Nand(0,1))
print(Nand(1,0))
print(Nand(1,1))

# FlipFlop Test
myFF = SRLatch()

# set it
myFF.set()
print("Bit set to 1") if myFF.q == 1 else print("Set is not working.")

# reset it
myFF.reset()
print("Bit set to 0") if myFF.q == 0 else print("Reset is not working.")

print("Test Again")
# set it
myFF.set()
print("Bit set to 1") if myFF.q == 1 else print("Set is not working.")

# reset it
myFF.reset()
print("Bit set to 0") if myFF.q == 0 else print("Reset is not working.")