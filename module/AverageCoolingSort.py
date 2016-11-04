from wilsonfunction import wilsonFunction
from coolingFunction import coolingFunction
from hackernewsfunction import hackerNewsFunction

class AverageCoolingSort:

  redis = None

  @staticmethod
  def init(fakeredis,redis,testing):
    if(testing):
      AverageCoolingSort.redis = fakeredis.FakeStrictRedis(db = 0)
    else:
      AverageCoolingSort.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
    AverageCoolingSort.redis.flushall()

  @staticmethod
  def addPost(index, count):
    AverageCoolingSort.redis.zadd("time",count,index)
    AverageCoolingSort.redis.hset(index, "score", 1)
    AverageCoolingSort.redis.hset(index, "votes", 1)
    AverageCoolingSort.redis.zadd("rating", 1, index)
    AverageCoolingSort.redis.zadd("hot", 0, index)

  @staticmethod
  def getRedisListSize():
    return AverageCoolingSort.redis.zcard("time")

  @staticmethod
  def voteUp(index, currentTime):
    score = AverageCoolingSort.redis.hincrby(index, "score", 1)
    votes = AverageCoolingSort.redis.hincrby(index, "votes", 1)
    rating = score/float(votes)
    time = currentTime - AverageCoolingSort.redis.zscore("time",index)
    hot = coolingFunction((rating+1),time)
    AverageCoolingSort.redis.zadd("hot", hot, index)
    AverageCoolingSort.redis.zadd("rating", rating, index)
    
    
  @staticmethod
  def voteDown(index, currentTime):
    score = AverageCoolingSort.redis.hincrby(index, "score", -1)
    votes = AverageCoolingSort.redis.hincrby(index, "votes", 1)
    rating = score/float(votes)
    time = currentTime - AverageCoolingSort.redis.zscore("time",index)
    hot = coolingFunction((rating+1),time)
    AverageCoolingSort.redis.zadd("hot", hot, index)
    AverageCoolingSort.redis.zadd("rating", rating, index)
  
  @staticmethod
  def popN(n):
    #returns array
    return AverageCoolingSort.redis.zrange("hot", -n, -1)

  @staticmethod
  def topN(n):
    #returns array
    return AverageCoolingSort.redis.zrange("rating", -n, -1)

  @staticmethod
  def newN(n):
    #returns array
    return AverageCoolingSort.redis.zrange("time", -n, -1)
