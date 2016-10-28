from random import randint

voteTimeInterval = 1;


def voteTime(currentTime, moduleArray):
  for module in moduleArray:
    if (voteTimeCheck(currentTime)):
      #Get the submission
      popularSubmissions = getPopularSubmissions(module)
      newSubmissions = getNewSubmissions(module)
      #Make the votes on those submissions
      popularVotes(popularSubmissions)
      newVotes(newSubmissions)


def voteTimeCheck(currentTime):
  if (currentTime % voteTimeInterval == 0):
    return True
  else:
    return False


def getPopularSubmissions(module):
  return module.topN(100)


def getNewSubmissions(module):
  return module.newN(100)


def popularVotes( submissions ):
  for submission in submissions:
    print(submissions)
    print(submission)
    postNumber = submission.index
    intrinsicPostValue = postList.postNumber
    if (doesUserVoteUp(intrinsicPostValue)):
      submissionUpvote(submission)
    else:
      submissionDownvote(submission)


def newVotes( submissions ):
  for submission in submissions:
    postNumber = submission.index
    intrinsicPostValue = postList.postNumber
    if (doesUserVoteUp(intrinsicPostValue)):
      submissionUpvote(submission)
    else:
      submissionDownvote(submission)


def doesUserVoteUp(intrinsicPostValue):
  if ( randint(0,99) < intrinsicPostValue ):
    votesUp = True
  else:
    votesUp = False  
  return votesUp
