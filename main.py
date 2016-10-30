import redis
import fakeredis
import userfunctions
from module.AverageSort import AverageSort

print('Initializing Configurations')

endTime = 100

#Module Inits

testing = True;

postTimeInterval = 7

voteTimeInterval = 7

AverageSort.init(fakeredis,redis,testing)

postList = [.6,.5,.2]

#AverageSort.addPost(1,1)


#Create Module Array
moduleArray = [AverageSort]

print('Configurations Initiliazed')


print('Initilizing Simulation Subfunctions')



print('Simulation Subfunctions Initialized')


print('Starting Simulation')

currentTime = 0


while currentTime < endTime :
  #posting
  addPost.postTime(postTimeInterval, currentTime, endTime, moduleArray)

  #Votes
  #uservotes.voteTime(postList, voteTimeInterval, currentTime, moduleArray)

  currentTime += 1


print(AverageSort.redis.zscore("average",1))

print(AverageSort.redis.zcard("time"))























