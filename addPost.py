import random

def postTime(postTimeInterval, currentTime, endTime, moduleArray):   

    for module in moduleArray:
        index = int(currentTime / postTimeInterval)
            
        if(postTimeCheck(postTimeInterval, currentTime)):
            #index += 1
            module.addPost(index, currentTime)        
        
        
    

#Checking if it's time to post
def postTimeCheck(postTimeInterval, currentTime):
    if (currentTime % postTimeInterval == 0):
        return True
    else:
        return False
