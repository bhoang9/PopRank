import redis
import fakeredis
from userfunctions import addPosts, makeVotes
from initfunctions.intrinsicArray import intrinsicArray
from module.AverageCoolingSort import AverageCoolingSort
from module.AverageHackerSort import AverageHackerSort
from module.WilsonCoolingSort import WilsonCoolingSort
from module.WilsonHackerSort import WilsonHackerSort
from metrics.rankDifference import rankDifference
        

print('Initializing Configurations')

#Testing Range
endTime = 1000 # Number of seconds, 100,000 for a day
postTimeInterval = 2
voteTimeInterval = 1

#Environment Configs
testing = True

print('Configurations Initiliazed')



print('Initilizing Simulation Subfunctions')

#Module Inits
AverageCoolingSort.init(fakeredis,redis,testing)
AverageHackerSort.init(fakeredis,redis,testing)
WilsonHackerSort.init(fakeredis,redis,testing, 1.96)
WilsonCoolingSort.init(fakeredis,redis,testing, 1.96)

moduleArray = [AverageHackerSort, AverageCoolingSort, WilsonCoolingSort,WilsonHackerSort]

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
#print("Intrinsic Value","Determined Intrinsic Value")
#length = int(endTime/postTimeInterval) + 1
#for i in range(length):
#    print(postList[i], AverageSort.redis.zscore("rating",i), WilsonSort.redis.zscore("rating",i))

#postList
rankDifference(postList, moduleArray)
print(sorted(range(len(postList)), key=lambda i: postList[i])[-10:])
#print(AverageSort.topN(10))
#print(WilsonCoolingSort.topN(10))
#print(WilsonHackerSort.topN(10))

#rankDifference(postList, moduleArray)

#print(WilsonSort.topN(100))

print(AverageCoolingSort.popN(100))
print(AverageHackerSort.popN(100))
print(WilsonCoolingSort.popN(100))
print(WilsonHackerSort.popN(100))

