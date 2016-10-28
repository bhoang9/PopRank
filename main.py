import fakeredis
from module.AverageSort import AverageSort
import uservotes

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
  uservotes.voteTime(currentTime, moduleArray)

  currentTime += 1

























