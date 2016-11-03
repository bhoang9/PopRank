class WilsonSort:

  redis = None

  @staticmethod
  def init(fakeredis,redis,testing):
    if(testing):
      WilsonSort.redis = fakeredis.FakeStrictRedis()
    else:
      WilsonSort.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
    WilsonSort.redis.flushall()

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
    rating = #Function here
    WilsonSort.redis.zadd("rating", rating, index)
    
    
  @staticmethod
  def voteDown(index):
    score = WilsonSort.redis.hincrby(index, "score", -1)
    votes = WilsonSort.redis.hincrby(index, "votes", 1)
    rating = #Function here
    WilsonSort.redis.zadd("rating", rating, index)
    
  
  @staticmethod
  def topN(n):
    #returns array
    return WilsonSort.redis.zrange("rating", -n, -1)

  @staticmethod
  def newN(n):
    #returns array
    return WilsonSort.redis.zrange("time", -n, -1)
