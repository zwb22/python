import redis

# 连接到本地redis服务
p_redis_cli = redis.Redis(host='localhost', port=6379, db=0)
# 设置指定key的value为字符串类型
p_redis_cli.set('zwb', '666')
# 获取数据
s_value = p_redis_cli.get('zwb')
print(f's_value {s_value}')
# 删除数据
p_redis_cli.delete('zwb')
