class AverageSort:

  redis = None

  @staticmethod
  def init(fakeredis,redis,testing):
    if(testing):
      AverageSort.redis = fakeredis.FakeStrictRedis()
    else:
      AverageSort.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
    AverageSort.redis.flushall()

  @staticmethod
  def addPost(index, count):
    AverageSort.redis.zadd("time",count,index)
    AverageSort.redis.hset(index, "score", 1)
    AverageSort.redis.hset(index, "votes", 1)
    AverageSort.redis.zadd("rating", 1, index)

  @staticmethod
  def getRedisListSize():
    return AverageSort.redis.zcard("time")


  @staticmethod
  def voteUp(index):
    score = AverageSort.redis.hincrby(index, "score", 1)
    votes = AverageSort.redis.hincrby(index, "votes", 1)
    rating = score/float(votes)
    AverageSort.redis.zadd("rating", rating, index)
    
    
  @staticmethod
  def voteDown(index):
    score = AverageSort.redis.hincrby(index, "score", -1)
    votes = AverageSort.redis.hincrby(index, "votes", 1)
    rating = score/float(votes)
    AverageSort.redis.zadd("rating", rating, index)
    
  
  @staticmethod
  def topN(n):
    #returns array
    return AverageSort.redis.zrange("rating", -n, -1)

  @staticmethod
  def newN(n):
    #returns array
    return AverageSort.redis.zrange("time", -n, -1)
