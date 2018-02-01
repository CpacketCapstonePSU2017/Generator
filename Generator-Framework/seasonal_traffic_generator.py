'''

'''


import sys
from os import path
from root import ROOT_DIR
sys.path.append(path.join(ROOT_DIR, 'CPacket-Common-Modules'))
from .dist_functions.stats.py import *
from 


class SeasonalTrafficGenerator(object):
    def __init__(self, size, maximum=None, minimum=0, shape=None, function_type=None):
        '''

        '''
        self.size = size
        self.maximum = maximum
        self.minimum = minimum
        self.shape = shape
        self.function_type = function_type

    def generate_traffic(self, speed):
        if speed == 0:
            # generate low traffic
            print("Fase speed set\n")
        elif speed == 1:
            # generate low traffic
            print("Low speed set\n")
        else:
            # error bad speed
            print("Error - bad traffic speed\n")

