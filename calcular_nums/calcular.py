# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:57:41 2020

@author: jcarl
"""


import redis
import os
import time


r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=6379, db=0)

redis_ready = False

while not redis_ready:
    try:
        redis_ready = r.ping()
    except:
        print("waiting for redis")
        time.sleep(3)
        
print("setup:redis alive")
print("setup:espera 3 segundos")
time.sleep(3)

i, x = 0, 0

while i <= 100:    
    i = r.lpop('queue_entrada')
    if i is None:
        break
    i = int(i)
    x = i*i
    r.rpush('queue_trabajo', x)
    print('recuperando', i, ' ... cuadrado: ', x)    
    time.sleep(0.25)