import random

def intrinsicArray(endTime, interval):

    length = int(endTime/interval) + 1 
    intrArray = [0] * length

    for i in range (length):
        x = random.uniform(-1,1)
        intrArray[i] = x

    return intrArray
