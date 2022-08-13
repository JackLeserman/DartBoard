import numpy as np
import cv2
import math
from transform_point import get_transformed_point
from multiprocessing import Process
import threading
from dart_to_point_left import get_dart_left
from dart_to_point_right import get_dart_right

from threading import Thread

def func1():
    left_point = get_dart_left()
    print(left_point)
    return left_point

def func2():
    right_point = get_dart_right()
    print(right_point)
    return right_point

lp = Thread(target = func1).start()
rp = Thread(target = func2).start()