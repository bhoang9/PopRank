import math

def wilsonFunction(upVotes, votes, z):

  phat = (1.0*upVotes)/votes
  divisor = 1+(z*z)/votes
  firstTerm = phat
  secondTerm = (z*z)/(2*votes)
  thirdTerm = z*math.sqrt( ( (phat*(1-phat))+((z*z)/(4*votes)) ) /votes)
  confidenceInterval = (firstTerm + secondTerm - thirdTerm)/(divisor)
  #print(divisor,firstTerm,secondTerm,thirdTerm)

  return confidenceInterval
