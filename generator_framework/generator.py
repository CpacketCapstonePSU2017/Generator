'''
    Author:
'''

from generator_config import *
import numpy as np
import pandas as pd
import datetime
from root import ROOT_DIR
import sys
sys.path.append('../resources')
from stats import *
from os import path, remove
from resources.config import RESOURCES_DIR
sys.path.append(path.join(ROOT_DIR, 'CPacket-Common-Modules'))
#from io_framework.csv_writer import CsvWriter


class Generator:
    def __init__(self):
        '''

        '''
        self._Config = GeneratorConfig()
        # TODO: This can be converted to only self._Config.**** No need to make copies
        self._Days = self._Config.Days
        self._Function = self._Config.Func_Type
        self._Shape = self._Config.Shape
        self._Increments = 96 * self._Days
        self.Work_Hours_Increments = self._Config.Business_Hours * 4
        #FIX: set a starting hour for work hours to ensure that the low-traffic morning hours are properly calculated
        self.Morning_Increments = 32
        self.Evening_Increments = 96 - self.Morning_Increments - self.Work_Hours_Increments
        self._High_Max = self._Config.High_Max
        self._High_Min = self._Config.High_Min
        self._Low_Max = self._Config.Low_Max
        self._Low_Min = self._Config.Low_Min
        self.Dist_Array = None
        self._Weeks = ((self._Days - (self._Days % 7)) / 7)
        self.Start_Date = self._Config.Start_Date
        self._Columns = 'avg_hrcrx_max_byt'
        self._data_writer = CsvWriter(host=db_config.host, port=db_config.port, username=db_config.username,
                                      password=db_config.password, database=database)


    def run(self):
        '''
            Runs generator. Not fully implemented. Right now just concatenates
            three arrays together.
        '''
        print(self.Start_Date)
        count = self.Start_Date.weekday()
        iter = 0
        iterArray = []
        while iter < self._Weeks:
            iterArray.append(iter)
            iter += 1
        for week in iterArray:
            array = np.array([])
            while count < 7:
                if count < 5:
                    print("weekday - high traffic")
                #weekday - high traffic
                    morning = Stats(self.Morning_Increments, self._Low_Max, self._Low_Min, self._Shape, self._Function)
                    worktime = Stats(self.Work_Hours_Increments, self._High_Max, self._High_Min, self._Shape, self._Function)
                    evening = Stats(self.Evening_Increments, self._Low_Max, self._Low_Min, self._Shape, self._Function)
                    # Last step is merge arrays
                    array = np.concatenate([morning.Dist_Array, worktime.Dist_Array, evening.Dist_Array])
                else:
                    print("weekend - low traffic")
                    #weekend - low traffic
                    morning = Stats(32, self._Low_Max, self._Low_Min, self._Shape, self._Function)
                    worktime = Stats(32, self._Low_Max, self._Low_Min, self._Shape, self._Function)
                    evening = Stats(32, self._Low_Max, self._Low_Min, self._Shape, self._Function)

                    array = np.concatenate([morning.Dist_Array, worktime.Dist_Array, evening.Dist_Array])
                if self.Dist_Array is None:
                    self.Dist_Array = array
                else:
                    self.Dist_Array = np.concatenate([self.Dist_Array, array])
                count += 1
            count = 0
        result_datetimes = np.array(pd.date_range(self._Config.Start_Date, periods=self._Increments+1, freq='15min'))[1:]
        return np.array([result_datetimes, self.Dist_Array]).transpose()

    def nparray_to_dataframe(self, nparray_data):
        indexes = pd.DataFrame(nparray_data[:, 0])
        indexes[0] = pd.to_datetime(indexes[0], format='%Y-%m-%d %H:%M:%S')
        cols = [self._Columns]
        df = pd.DataFrame(data=nparray_data[0:, 1:],
                          index=indexes[0],
                          columns=cols)
        return df

    def write_data_to_csv(self, model_name, df):
        if not isinstance(df, pd.DataFrame):
            print("Error reading the data from database. Please test this query in Chronograf/Grafana.")
        df.to_csv(path.join(RESOURCES_DIR, model_name + "_generated.csv"))

    #this will work once the io_framework can succesfully import
    '''def write_data_to_database(self, model_name, df):
        df.to_csv(path.join(RESOURCES_DIR, model_name + "_generated.csv"))
        self._data_writer.csv_file_to_db(measurement_to_use=model_name + '_generated',
                                         new_csv_file_name=path.join(RESOURCES_DIR, model_name + "_generated.csv"))
        remove(path.join(RESOURCES_DIR, model_name + "_generated.csv"))'''


# Test Code - Delete later
test_generator = Generator()
test_generator._Config.get_config()
data = test_generator.run()
dataFrame = test_generator.nparray_to_dataframe(data)
test_generator.write_data_to_database('weibull', dataFrame)
#print(test_generator.Dist_Array)
print("array count: %d" % (len(test_generator.Dist_Array)))


