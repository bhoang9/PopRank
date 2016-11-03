#Difference squared, only best posts


def residualBest(postList, moduleArray):
        length = len(postList)

        if(length >= 25):
                topTwentyFive = sorted(range(len(postList)), key=lambda i: postList[i])[-25:]
                for module in moduleArray:
                    sum = 0
            
                    for i in topTwentyFive:
                        sum += (postList[i] - module.redis.zscore("rating",i)) ** 2

                    print(module.__name__, sum)
                    
        else:
                print("Less than 25 posts. Cannot run metric.")

     
                
