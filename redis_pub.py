import redis
import cv2
import base64
from datetime import datetime
import time
import json

r = redis.Redis(host="172.18.0.3", port=6379)

capture = cv2.VideoCapture('')
# capture.set(cv2.CAP_PROP_FOURCC, 1196444237)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# capture.set(cv2.CAP_PROP_FPS , 10)

while True:
    d = datetime.fromtimestamp(time.time())
    # print(d)
    # print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    ret, frame = capture.read()
    r.publish(channel="redis_test",message=frame.tobytes())