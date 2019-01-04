
def writeToScroll(inst):
    print('Hi from queue', inst)
    for idx in range(10):
        inst.guiQueue.put('Message from a Queue:' + str(idx))
    inst.createThread(6)
