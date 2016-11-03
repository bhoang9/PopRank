import math

def coolingFunction(rating, time):

  r = -.002
  hot = (rating) * math.exp(r * time)

  return hot
