from wilsonfunction import wilsonFunction
from coolingFunction import coolingFunction
from hackernewsfunction import hackerNewsFunction

class AverageHackerSort:

  redis = None

  @staticmethod
  def init(fakeredis,redis,testing):
    if(testing):
      AverageHackerSort.redis = fakeredis.FakeStrictRedis(db = 3)
    else:
      AverageHackerSort.redis = redis.StrictRedis(host='localhost', port=6379, db=3)
    AverageHackerSort.redis.flushall()

  @staticmethod
  def addPost(index, count):
    AverageHackerSort.redis.zadd("time",count,index)
    AverageHackerSort.redis.hset(index, "score", 1)
    AverageHackerSort.redis.hset(index, "votes", 1)
    AverageHackerSort.redis.zadd("rating", 1, index)
    AverageHackerSort.redis.zadd("hot", 0, index)

  @staticmethod
  def getRedisListSize():
    return AverageHackerSort.redis.zcard("time")


  @staticmethod
  def voteUp(index, currentTime):
    score = AverageHackerSort.redis.hincrby(index, "score", 1)
    votes = AverageHackerSort.redis.hincrby(index, "votes", 1)
    rating = score/float(votes)
    time = currentTime - AverageHackerSort.redis.zscore("time",index)
    hot = hackerNewsFunction((rating+1), time)
    AverageHackerSort.redis.zadd("hot", hot, index)
    AverageHackerSort.redis.zadd("rating", rating, index)
    
    
  @staticmethod
  def voteDown(index, currentTime):
    score = AverageHackerSort.redis.hincrby(index, "score", -1)
    votes = AverageHackerSort.redis.hincrby(index, "votes", 1)
    rating = score/float(votes)
    time = currentTime - AverageHackerSort.redis.zscore("time",index)
    hot = hackerNewsFunction((rating+1), time)
    AverageHackerSort.redis.zadd("hot", hot, index)
    AverageHackerSort.redis.zadd("rating", rating, index)
    
  
  @staticmethod
  def popN(n):
    #returns array
    return AverageHackerSort.redis.zrange("hot", -n, -1)

  @staticmethod
  def topN(n):
    #returns array
    return AverageHackerSort.redis.zrange("rating", -n, -1)

  @staticmethod
  def newN(n):
    #returns array
    return AverageHackerSort.redis.zrange("time", -n, -1)
