from Logic import *

#Clock tests
print("Begin clock tests.")
print("\nClock Test.")

class ClockedAnd(Clock):
    
    def run(self):
        while(1):
            print("In the And." + str(self.bit))
            e = self.get_e()
            e.wait()
        

cl = Clock()
cl.run()

ca = ClockedAnd()
ca.run()
