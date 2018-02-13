"""
    A simple function for Distributions
    The byte count is accessed from ._ByteCount for each new object created.
"""

from generator_framework.generator_config import *
import numpy as np
import pandas as pd
from root import ROOT_DIR
import sys
from os import path
sys.path.append(path.join(ROOT_DIR, 'CPacket-Common-Modules'))


class Weibull:
    def __init__(self):
        self._Config = GeneratorConfig()
        self.work_hours = self._Config.Business_Hours * 4
        self.morning_hours = self._Config.Work_Hour_Start * 4
        self.evening_hours = 96 - self.morning_hours - self.work_hours
        self.Dist_Array = None
        self._Weeks = ((self._Config.Days - (self._Config.Days % 7)) / 7)
        self._Increments = 96 * self._Config.Days
        self.Function_Name = "weibull"

    def get_array(self, max, increments):
        array = (self._Config.Scale * np.random.weibull(self._Config.Shape, increments)).astype(int)
        array[array > max] = max
        return array

    def generate(self):
        count = self._Config.Start_Date.weekday()
        iter = 0
        iterArray = []
        while iter < self._Weeks:
            iterArray.append(iter)
            iter += 1
        for week in iterArray:
            array = np.array([])
            while count < 7:
                if count < 5:
                    #weekday - high traffic during work hours
                    array = np.concatenate([self.get_array(self._Config.Low_Max, self.morning_hours), self.get_array(self._Config.High_Max, self.work_hours), self.get_array(self._Config.Low_Max, self.evening_hours)])
                else:
                    #weekend - low traffic
                    array = self.get_array(self._Config.Low_Max, self._Increments)
                if self.Dist_Array is None:
                    self.Dist_Array = array
                else:
                    self.Dist_Array = np.concatenate([self.Dist_Array, array])
                count += 1
            count = 0
        result_datetimes = np.array(
            pd.date_range(self._Config.Start_Date, periods=self._Increments + 1, freq='15min'))[1:]
        print("Hey!")
        return np.array([result_datetimes, self.Dist_Array]).transpose()


'''
class Stats:

    def __init__(self, size, maximum=None, minimum=0, shape=None, functype=None):
        """
            Creates the specified distribution into an Array
            :param: Min: Should almost always be 0 as we don't use negative values
            :param: Max: Can change varying on function. Should usually be infinity.
            :param: Size: How many elements to generate
            :param: Shape: The shape of the distribution.
            :param: Type: The distribution function to use. For now 'None' will default to Poisson.
        """

        # copied for Generate function.
        self._Min = minimum
        self._Max = maximum
        self._Size = size
        self._Shape = shape
        self._Func_Type = functype
        # public
        self.Dist_Array = None

        # Default function type will be Poisson.
        if self._Func_Type is None or self._Func_Type == 'poisson':
            if self._Max is None:
                # default to hardcoded max
                self._Max = 1.25 * 10000000
            # TODO: Fiddle with this level of variance
            lam = self._Max - (self._Max / 4)
            self.Dist_Array = np.random.poisson(lam=lam, size=self._Size)
            for x in self.Dist_Array:
                if x > self._Max:
                    x *= 0
                    x += self._Max
        elif self._Func_Type == 'weibull':
            if self._Max is None:
                self._Max = 1.25 * 10000000
            self.Dist_Array = (1000000 * np.random.weibull(self._Shape, self._Size)).astype(int)
            self.Dist_Array[self.Dist_Array > self._Max] = self._Max
            for x in self.Dist_Array:
                if x > self._Max:
                    print("x is greater than max")
                    x *= 0
                    x += self._Max
        elif self._Func_Type == 'beta':
            # beta function implementation
            pass
        else:
            print("Function type not recognized!")

    # Used for getting a second Dist array later in development.
    # overwrites the current Dist_Array.
    def generate(self):
        # switch for function type
        # Default
        if self._Func_Type is None or self._Func_Type == 'poisson':
            if self._Max is None:
                # default hardcoded value
                self._Max = 1.25 * 10000000
            # TODO: Fiddle with this level of variance
            lam = self._Max - (self._Max / 4)
            # TODO: error check Max and Size
            self.Dist_Array = np.random.poisson(lam=lam, size=self._Size)
            for x in self.Dist_Array:
                if x > self._Max:
                    x *= 0
                    x += self._Max
        elif self._Func_Type == 'weibull':
            if self._Max is None:
                self._Max = 1.25 * 10000000
            self.Dist_Array = (10000000 * np.random.weibull(self._Shape, self._Size)).astype(int)
            for x in self.Dist_Array:
                if x > self._Max:
                    x *= 0
                    x += self._Max
        elif self._Func_Type == 'beta':
            pass
        else:
            print("Function type not recognized!")
            return -1

        return self.Dist_Array
'''