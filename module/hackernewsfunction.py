
def hackerNewsFunction(confidenceInterval, time):
  
  score = confidenceInterval/((time+2)**1.8)

  return score
