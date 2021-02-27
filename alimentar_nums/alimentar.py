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


#Eliminamos los elementos residuales de la lista
while True:    
    i = r.lpop('queue_entrada')
    if i is None:
        print('setup:limpieza de queue')
        break


#Agregamos los nuevos elementos
i = 0
while i <= 100:
    r.rpush('queue_entrada', i)  #empuja un valor por la derecha right push
    i+=1
    #print('numero: ', i)    
    #time.sleep(3)