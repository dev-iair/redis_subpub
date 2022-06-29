import redis
import cv2
import numpy as np
from datetime import datetime
import time

r = redis.Redis(host="172.18.0.3", port=6379)
s = r.pubsub()

s.subscribe("redis_test")

while cv2.waitKey(33) < 0 :
    res = s.get_message()
    if res is not None:
        if res['data'] != 1:
            d = datetime.fromtimestamp(time.time())
            print(d)
            buffer = np.frombuffer(res['data'], dtype=np.uint8)
            buffer.shape = (448,3584,3)
            cv2.imshow('hi',buffer)