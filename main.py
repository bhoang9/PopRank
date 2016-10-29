import redis
import fakeredis
import uservotes
from module.AverageSort import AverageSort

print('Initializing Configurations')

endTime = 1000

#Module Inits

testing = False;

voteTimeInterval = 1

AverageSort.init(fakeredis,redis,testing)

postList = [.6,-.5,.2]

AverageSort.addPost(1,1)


#Create Module Array
moduleArray = [AverageSort]

print('Configurations Initiliazed')


print('Initilizing Simulation Subfunctions')



print('Simulation Subfunctions Initialized')


print('Starting Simulation')

currentTime = 0


while currentTime < endTime :

  #Votes
  uservotes.voteTime(postList, voteTimeInterval, currentTime, moduleArray)

  currentTime += 1


print(AverageSort.redis.zscore("average",1))






















