class AverageSort:

  redis = None

  @staticmethod
  def init(fakeredis):
    AverageSort.redis = fakeredis.FakeStrictRedis()    

  @staticmethod
  def addPost(index, count):
    AverageSort.redis.zadd("time",count,index)
    AverageSort.redis.hset(index, "score", 1)
    AverageSort.redis.hset(index, "votes", 1)
    AverageSort.redis.zadd("average", 1, index)


  @staticmethod
  def voteUp(index):
    score = AverageSort.redis.hincrby(index, "score", 1)
    votes = AverageSort.redis.hincrby(index, "votes", 1)
    average = score/float(votes)
    AverageSort.redis.zadd("average", average, index)
    
    
  @staticmethod
  def voteDown(index):
    score = AverageSort.redis.hincrby(index, "score", -1)
    votes = AverageSort.redis.hincrby(index, "votes", 1)
    average = score/float(votes)
    AverageSort.redis.zadd("average", average, index)
    
  
  @staticmethod
  def topN(n):
    #returns array
    return = AverageSort.redis.zrange("average", 0, n)

  @staticmethod
  def newN(n):
    #returns array
    return = AverageSort.redis.zrange("time", 0, n)
