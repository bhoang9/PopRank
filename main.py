Import fakeredis
from module.AverageSort import AverageSort


print('Initializing Configurations')

endTime = 10

#Module Inits
AverageSort.init(fakeredis)


#Create Module Array
moduleArray = [AverageSort]

print('Configurations Initiliazed')


print('Initilizing Simulation Subfunctions')



print('Simulation Subfunctions Initialized')


print('Starting Simulation')

currentTime = 0

AverageSort.addPost(1,1)  

AverageSort.voteDown(1)

while currentTime < endTime :



  #Votes
  voteTime(currentTime, moduleArray)



  print(AverageSort.redis.zscore("average", 1))

  currentTime += 1

























