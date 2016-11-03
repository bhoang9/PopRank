from wilsonfunction import wilsonFunction
from coolingFunction import coolingFunction
from hackernewsfunction import hackerNewsFunction

class WilsonCoolingSort:

  redis = None
  zscore = None

  @staticmethod
  def init(fakeredis,redis,testing,zscore):
    if(testing):
      WilsonCoolingSort.redis = fakeredis.FakeStrictRedis(db=1)
    else:
      WilsonCoolingSort.redis = redis.StrictRedis(host='localhost', port=6379, db=1)
    WilsonCoolingSort.redis.flushall()
    WilsonCoolingSort.zscore = zscore

  @staticmethod
  def addPost(index, count):
    WilsonCoolingSort.redis.zadd("time",count,index)
    WilsonCoolingSort.redis.hset(index, "score", 1)
    WilsonCoolingSort.redis.hset(index, "votes", 1)
    WilsonCoolingSort.redis.zadd("rating", 1, index)
    WilsonCoolingSort.redis.zadd("hot", 0, index)


  @staticmethod
  def getRedisListSize():
    return WilsonCoolingSort.redis.zcard("time")


  @staticmethod
  def voteUp(index,currentTime):
    score = WilsonCoolingSort.redis.hincrby(index, "score", 1)
    votes = WilsonCoolingSort.redis.hincrby(index, "votes", 1)
    upvotes = (score + votes)/2 
    rating = 2*(wilsonFunction(upvotes, votes, WilsonCoolingSort.zscore)) - 1
    time = currentTime - WilsonCoolingSort.redis.zscore("time",index)
    hot = coolingFunction((rating+1), time)
    #hot = hackerNewsFunction((rating+1), time)
    WilsonCoolingSort.redis.zadd("hot", hot, index)
    WilsonCoolingSort.redis.zadd("rating", rating, index)
    

  @staticmethod
  def voteDown(index,currentTime):
    score = WilsonCoolingSort.redis.hincrby(index, "score", -1)
    votes = WilsonCoolingSort.redis.hincrby(index, "votes", 1)
    upvotes = (score + votes)/2 
    rating = 2*(wilsonFunction(upvotes, votes, WilsonCoolingSort.zscore)) - 1
    time = currentTime - WilsonCoolingSort.redis.zscore("time",index)
    hot = coolingFunction((rating+1), time)
    #hot = hackerNewsFunction((rating+1), time)
    WilsonCoolingSort.redis.zadd("hot", hot, index)
    WilsonCoolingSort.redis.zadd("rating", rating, index)
    
  @staticmethod
  def popN(n):
    #returns array
    return WilsonCoolingSort.redis.zrange("hot", -n, -1)
  
  @staticmethod
  def topN(n):
    #returns array
    return WilsonCoolingSort.redis.zrange("rating", -n, -1)

  @staticmethod
  def newN(n):
    #returns array
    return WilsonCoolingSort.redis.zrange("time", -n, -1)
