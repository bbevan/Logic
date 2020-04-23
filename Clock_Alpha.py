from Logic import And
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


def ClockedAnd():
    bit = cl.state
    result = And(1, bit)

    print(str(result))

# run it



if __name__ == '__main__':
    # spawn a clock
    cl = Clock()
    
    # just run the ClockedAnd once
    ClockedAnd()

    # update the clock's state
    cl.update_state()

    # run the ClockedAnd again
    ClockedAnd()