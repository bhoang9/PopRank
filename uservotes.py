from random import randint


interval = ;

def voteTimeCheck( currentTime ):

  if ( currentTime % interval == 0 ):
    return True
  else:
    return False




def voteTime( currentTime, getNew):

  if (voteTimeCheck()):
    popularSubmissions = getPopularSubmissions()
    popularVotes(popularSubmissions)

    if (getNew):
      newSubmissions = getNewSubmissions()
      newVotes(newSubmissions)

    generalVoters()




def doesUserVoteUp(intrinsicPostValue):
  
  votesUp = False  

  if ( randint(0,99) < intrinsicPostValue ):
    votesUp = True

  return votesUp




  
def popularVotes( submissions ):




def newVotes( submissions ):





