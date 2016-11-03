from wilsonfunction import wilsonFunction

class WilsonSort:

  redis = None
  zscore = None

  @staticmethod
  def init(fakeredis,redis,testing,zscore):
    if(testing):
      WilsonSort.redis = fakeredis.FakeStrictRedis(db=1)
    else:
      WilsonSort.redis = redis.StrictRedis(host='localhost', port=6379, db=1)
    WilsonSort.redis.flushall()
    WilsonSort.zscore = zscore

  @staticmethod
  def addPost(index, count):
    WilsonSort.redis.zadd("time",count,index)
    WilsonSort.redis.hset(index, "score", 1)
    WilsonSort.redis.hset(index, "votes", 1)
    WilsonSort.redis.zadd("rating", 1, index)

  @staticmethod
  def getRedisListSize():
    return WilsonSort.redis.zcard("time")


  @staticmethod
  def voteUp(index):
    score = WilsonSort.redis.hincrby(index, "score", 1)
    votes = WilsonSort.redis.hincrby(index, "votes", 1)
    upvotes = (score + votes)/2 
    rating = 2*(wilsonFunction(upvotes, votes, WilsonSort.zscore)) - 1 
    WilsonSort.redis.zadd("rating", rating, index)
    

  @staticmethod
  def voteDown(index):
    score = WilsonSort.redis.hincrby(index, "score", -1)
    votes = WilsonSort.redis.hincrby(index, "votes", 1)
    upvotes = (score + votes)/2 
    rating = 2*(wilsonFunction(upvotes, votes, WilsonSort.zscore)) - 1 
    WilsonSort.redis.zadd("rating", rating, index)
    
  
  @staticmethod
  def topN(n):
    #returns array
    return WilsonSort.redis.zrange("rating", -n, -1)

  @staticmethod
  def newN(n):
    #returns array
    return WilsonSort.redis.zrange("time", -n, -1)
