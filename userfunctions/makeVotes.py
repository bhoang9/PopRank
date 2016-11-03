import random

def voteTime(postList, voteTimeInterval, currentTime, moduleArray):
  for module in moduleArray:
    if (voteTimeCheck(voteTimeInterval, currentTime)):
      #Get the submission
      popularSubmissions = getPopularSubmissions(module)
      newSubmissions = getNewSubmissions(module)
      #Make the votes on those submissions
      popularVotes(module, postList, popularSubmissions, currentTime)
      newVotes(module, postList, newSubmissions, currentTime)

def voteTimeCheck(voteTimeInterval, currentTime):
  if (currentTime % voteTimeInterval == 0):
    return True
  else:
    return False

def getPopularSubmissions(module):
  return module.topN(100)

def getNewSubmissions(module):
  return module.newN(100)

def popularVotes(module, postList,submissions, currentTime):
  for submission in submissions:
    index = int(submission)
    intrinsicPostValue = postList[index]
    if (doesUserVoteUp(intrinsicPostValue)):
      submissionUpvote(module, index, currentTime)
    else:
      submissionDownvote(module, index, currentTime)

def newVotes(module, postList,submissions, currentTime):
  for submission in submissions:
    index = int(submission)
    intrinsicPostValue = postList[index]
    if (doesUserVoteUp(intrinsicPostValue)):
      submissionUpvote(module, index, currentTime)
    else:
      submissionDownvote(module, index, currentTime)

def doesUserVoteUp(intrinsicPostValue):
  if ( random.uniform(-1,1) < intrinsicPostValue ):
    votesUp = True
  else:
    votesUp = False  
  return votesUp

def submissionUpvote(module, index, currentTime):
  module.voteUp(index,currentTime)

def submissionDownvote(module, index, currentTime):
  module.voteDown(index, currentTime)
