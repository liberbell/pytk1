
def writeToScroll(inst):
    print('Hi from queue', inst)
    inst.createThread(6)
