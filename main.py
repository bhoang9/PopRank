import redis
import fakeredis
from userfunctions import addPosts, makeVotes
from initfunctions.intrinsicArray import intrinsicArray
from module.AverageSort import AverageSort
from module.WilsonSort import WilsonSort

        

        print('Initializing Configurations')

        #Testing Range
        endTime = 200
        postTimeInterval = 2
        voteTimeInterval = 1

        #Environment Configs
        testing = True

        print('Configurations Initiliazed')



        print('Initilizing Simulation Subfunctions')

        #Module Inits
        AverageSort.init(fakeredis,redis,testing)
        WilsonSort.init(fakeredis,redis,testing, 1.96)

        moduleArray = [AverageSort, WilsonSort]

        print('Simulation Subfunctions Initialized')



        print('Starting Simulation')

        #Simulation Init
        postList = intrinsicArray(endTime, postTimeInterval);
        currentTime = 0

        #Simulation Start
        while currentTime <= endTime :
            #Posts
              addPosts.postTime(postTimeInterval, currentTime, endTime, moduleArray)

                #Votes
                  makeVotes.voteTime(postList, voteTimeInterval, currentTime, moduleArray)

                    #increment counter
                      currentTime += 1

                      #Simulation End
                      print("Intrinsic Value","Determined Intrinsic Value")
                      length = int(endTime/postTimeInterval) + 1
                      for i in range(length):
                          print(postList[i], AverageSort.redis.zscore("rating",i), WilsonSort.redis.zscore("rating",i))

                          #postList
                          print(sorted(range(len(postList)), key=lambda i: postList[i])[-10:])

                          print(AverageSort.topN(10))

                          print(WilsonSort.topN(10))



