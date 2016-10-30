import random

def voteTime(postList, voteTimeInterval, currentTime, moduleArray):
  for module in moduleArray:
    if (voteTimeCheck(voteTimeInterval, currentTime)):
      #Get the submission
      popularSubmissions = getPopularSubmissions(module)
      newSubmissions = getNewSubmissions(module)
      #Make the votes on those submissions
      popularVotes(module, postList, popularSubmissions)
      newVotes(module, postList, newSubmissions)

def voteTimeCheck(voteTimeInterval, currentTime):
  if (currentTime % voteTimeInterval == 0):
    return True
  else:
    return False

def getPopularSubmissions(module):
  return module.topN(100)

def getNewSubmissions(module):
  return module.newN(100)

def popularVotes(module, postList,submissions):
  for submission in submissions:
    index = int(submission)
    intrinsicPostValue = postList[index]
    if (doesUserVoteUp(intrinsicPostValue)):
      submissionUpvote(module, index)
    else:
      submissionDownvote(module, index)

def newVotes(module, postList,submissions):
  for submission in submissions:
    index = int(submission)
    intrinsicPostValue = postList[index]
    if (doesUserVoteUp(intrinsicPostValue)):
      submissionUpvote(module, index)
    else:
      submissionDownvote(module, index)

def doesUserVoteUp(intrinsicPostValue):
  if ( random.uniform(-1,1) < intrinsicPostValue ):
    votesUp = True
  else:
    votesUp = False  
  return votesUp

def submissionUpvote(module, index):
  module.voteUp(index)

def submissionDownvote(module, index):
  module.voteDown(index)
