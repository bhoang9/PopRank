#Print difference between each module Determined Intrinsic Value
#and the Intrinsic Value


def simpleDifference(postList, moduleArray):
        length = len(postList)

        for module in moduleArray:
            sum = 0
            
            for i in range(length):
                sum += abs(postList[i] - module.redis.zscore("rating",i))

            print(module.__name__, sum)
                
