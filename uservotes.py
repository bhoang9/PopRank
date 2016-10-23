#Mostly pseudocode atm

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

    generalSubmissions = getGeneralSubmissions()
    generalVotes(generalSubmissions)




def doesUserVoteUp(intrinsicPostValue):
  
  votesUp = False  

  if ( randint(0,99) < intrinsicPostValue ):
    votesUp = True

  return votesUp



  
def popularVotes( submissions ):

  for submission in submissions:

    postNumber = submission.index
    intrinsicPostValue = postList.postNumber

    if (doesUserVoteUp(intrinsicPostValue)):
      submissionUpvote(submission)
    else
      submissionDownvote(submission)


def newVotes( submissions ):


  for submission in submissions:

    postNumber = submission.index
    intrinsicPostValue = postList.postNumber

    if (doesUserVoteUp(intrinsicPostValue)):
      submissionUpvote(submission)
    else
      submissionDownvote(submission)



def generalVotes( submissions ):

  for submission in submissions:

    postNumber = submission.index
    intrinsicPostValue = postList.postNumber

    if (doesUserVoteUp(intrinsicPostValue)):
      submissionUpvote(submission)
    else
      submissionDownvote(submission)


