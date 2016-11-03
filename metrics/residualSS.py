#Difference squared


def residualSS(postList, moduleArray):
        length = len(postList)

        for module in moduleArray:
            sum = 0
            
            for i in range(length):
                sum += (postList[i] - module.redis.zscore("rating",i)) ** 2

            print(module.__name__, sum)
                
