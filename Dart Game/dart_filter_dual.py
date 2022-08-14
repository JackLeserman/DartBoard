import numpy as np
import cv2
import math
import time
from transform_point import get_transformed_point
from multiprocessing import Process
import threading
from dart_to_point_left import get_dart_left
from dart_to_point_right import get_dart_right
from point_to_score import *
from threading import Thread
lp = (0,0)
rp = (0,0)

def play_darts():
    def func1():
        global lp
        left_point = get_dart_left()
        print(left_point)
        lp = left_point
        return left_point

    def func2():
        global rp
        right_point = get_dart_right()
        print(right_point)
        rp = right_point
        return right_point

    l_thread = Thread(target = func1)
    r_thread = Thread(target = func2)
    l_thread.start()
    r_thread.start()

    while l_thread.is_alive():
        time.sleep(0.1)
    while r_thread.is_alive():
        time.sleep(0.1)

    x_left = lp[0]
    y_left = lp[1]
    x_right = rp[0]
    y_right = rp[1]

    avg_point = (int(((x_left + x_right)/2)),int(((y_left+y_right)/2)))
    print("avg")
    print(avg_point)

    score = get_score(avg_point)
    pointys = score[1]

    print("")
    print("")
    print("score: " +  str(pointys))
    return score

play_darts()


