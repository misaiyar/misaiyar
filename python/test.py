
import redis
import sys
from redis import BlockingConnectionPool

connection_kwargs = {
    'host': '192.168.17.128',
    'port': 6379,
    'db': 11,
    'password': None
}
pool = BlockingConnectionPool(500,
     5,
     socket_timeout=30,
     socket_connect_timeout=5,
     **connection_kwargs)
redis = redis.StrictRedis(connection_pool=pool)
method = sys.argv[1]
lists = sys.argv[2:]
func = getattr(redis,method)
print str( func(*lists) )

class Task:
    def echo(self,a,b,c):
        log_msg = 'a=%s, b=%s, c=%s' % (a, b, c)
        print log_msg

    def info(self):
        log_msg = 'Info'
        print log_msg


method = 'echo'
task = Task()
func = getattr(task,method);
lists=["sda","sadas","asda"]
func(*lists)
