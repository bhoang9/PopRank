def rankDifference(postList,moduleArray):
    length = len(postList)

    if(length >= 25):
            topTwentyFive = sorted(range(len(postList)), key=lambda i: postList[i])[-25:]
            for module in moduleArray:
                sum = 0
                
                moduleTopTwentyFive = map(int,module.popN(25))
                for i in range(0,24):
                    if (topTwentyFive[i] in moduleTopTwentyFive):
                        sum += 25 - i
                        
                print(module.__name__, sum)
            
    else:
            print("Less than 25 posts. Cannot run metric.")        

