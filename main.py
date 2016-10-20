import fakeredis

print "Test"

r = fakeredis.FakeStrictRedis()

r.set('foo','bar')

print(r.get('foo'))

