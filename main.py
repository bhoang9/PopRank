import redis
import fakeredis
from userfunctions import addPosts, makeVotes
from initfunctions.intrinsicArray import intrinsicArray
from module.AverageSort import AverageSort
from metrics.simpleDifference import simpleDifference
from metrics.residualSS import residualSS
from metrics.residualBest import residualBest
from metrics.rankDifference import rankDifference



print('Initializing Configurations')

#Testing Range
endTime = 220
postTimeInterval = 2
voteTimeInterval = 1

#Environment Configs
testing = True

print('Configurations Initiliazed')



print('Initilizing Simulation Subfunctions')

#Module Inits
AverageSort.init(fakeredis,redis,testing)
moduleArray = [AverageSort]

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
#  print(postList[i], AverageSort.redis.zscore("rating",i))

#simpleDifference(postList, moduleArray)
#residualSS(postList, moduleArray)
#residualBest(postList,moduleArray)
#rankDifference(postList,moduleArray)



