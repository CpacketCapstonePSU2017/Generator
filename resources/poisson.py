import pandas as pd
import numpy as np
from root import ROOT_DIR
import sys
from os import path
sys.path.append(path.join(ROOT_DIR, 'CPacket-Common-Modules'))

class Poisson:
    def __init__(self, generator_config):
        self._Config = generator_config
        self.work_hours = self._Config.Business_Hours * 4
        self.morning_hours = self._Config.Work_Hour_Start * 4
        self.evening_hours = 96 - self.morning_hours - self.work_hours
        self.Dist_Array = None
        self.Increments_Per_Day = 96
        self._Increments = 96 * self._Config.Days
        self._Weeks = ((self._Config.Days - (self._Config.Days % 7)) / 7)
        self.Name = "poisson"

    def get_array(self, max, increments):
        lam = max - (max / 3)
        array = np.random.poisson(lam=lam, size=increments)
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
                    array = self.get_array(self._Config.Low_Max, self.Increments_Per_Day)
                if self.Dist_Array is None:
                    self.Dist_Array = array
                else:
                    self.Dist_Array = np.concatenate([self.Dist_Array, array])
                count += 1
            count = 0
        start_date = str(self._Config.Start_Date) + "T00:00:00.00"
        result_datetimes = np.array(
            pd.date_range(start_date, periods=self._Increments + 1, freq='15min'))[1:]
        return np.array([result_datetimes, self.Dist_Array]).transpose()