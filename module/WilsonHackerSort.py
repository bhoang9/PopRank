from wilsonfunction import wilsonFunction
from coolingFunction import coolingFunction
from hackernewsfunction import hackerNewsFunction

class WilsonHackerSort:

  redis = None
  zscore = None

  @staticmethod
  def init(fakeredis,redis,testing,zscore):
    if(testing):
      WilsonHackerSort.redis = fakeredis.FakeStrictRedis(db=2)
    else:
      WilsonHackerSort.redis = redis.StrictRedis(host='localhost', port=6379, db=2)
    WilsonHackerSort.redis.flushall()
    WilsonHackerSort.zscore = zscore

  @staticmethod
  def addPost(index, count):
    WilsonHackerSort.redis.zadd("time",count,index)
    WilsonHackerSort.redis.hset(index, "score", 1)
    WilsonHackerSort.redis.hset(index, "votes", 1)
    WilsonHackerSort.redis.zadd("rating", 1, index)
    WilsonHackerSort.redis.zadd("hot", 0, index)


  @staticmethod
  def getRedisListSize():
    return WilsonHackerSort.redis.zcard("time")


  @staticmethod
  def voteUp(index,currentTime):
    score = WilsonHackerSort.redis.hincrby(index, "score", 1)
    votes = WilsonHackerSort.redis.hincrby(index, "votes", 1)
    upvotes = (score + votes)/2 
    rating = 2*(wilsonFunction(upvotes, votes, WilsonHackerSort.zscore)) - 1
    time = currentTime - WilsonHackerSort.redis.zscore("time",index)
    #hot = coolingFunction((rating+1), time)
    hot = hackerNewsFunction((rating+1), time)
    WilsonHackerSort.redis.zadd("hot", hot, index)
    WilsonHackerSort.redis.zadd("rating", rating, index)
    

  @staticmethod
  def voteDown(index,currentTime):
    score = WilsonHackerSort.redis.hincrby(index, "score", -1)
    votes = WilsonHackerSort.redis.hincrby(index, "votes", 1)
    upvotes = (score + votes)/2 
    rating = 2*(wilsonFunction(upvotes, votes, WilsonHackerSort.zscore)) - 1
    time = currentTime - WilsonHackerSort.redis.zscore("time",index)
    #hot = coolingFunction((rating+1), time)
    hot = hackerNewsFunction((rating+1), time)
    WilsonHackerSort.redis.zadd("hot", hot, index)
    WilsonHackerSort.redis.zadd("rating", rating, index)
    
  @staticmethod
  def popN(n):
    #returns array
    return WilsonHackerSort.redis.zrange("hot", -n, -1)
  
  @staticmethod
  def topN(n):
    #returns array
    return WilsonHackerSort.redis.zrange("rating", -n, -1)

  @staticmethod
  def newN(n):
    #returns array
    return WilsonHackerSort.redis.zrange("time", -n, -1)
