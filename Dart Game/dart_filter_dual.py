import numpy as np
import cv2
import math
from transform_point import get_transformed_point
from multiprocessing import Process
import dart_filter_generic

def filter(camID):
        dart_filter_generic.filter(camID)
        print("done" + camID)


if __name__ == '__main__':
        #f(0)
        '''
        t0 = threading.Thread(target=f, args= (0,))
        t0.start()
        t1 = threading.Thread(target=f, args= (1,))
        t1.start()
        '''

        left = 1
        right = 2
        p0 = Process(target=filter, args=(left,))
        p0.start()
        p1 = Process(target=filter, args=(right,))
        p1.start()
