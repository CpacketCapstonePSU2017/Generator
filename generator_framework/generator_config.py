"""
    This code is released under an MIT license
    Author: Adrian Cardoza
"""

import datetime
from resources.weibull import *
from resources.poisson import *


class GeneratorConfig:

    def __init__(self):
        self.Database = 'generated_data'
        self.Days = 7
        self.High_Max = 1.25 * 10000000
        self.High_Min = 0
        self.Low_Max = 1.25 * 1500000
        self.Low_Min = 0
        self.Business_Hours = 6
        self.Shape = .5
        self.Start_Date = datetime.date.today()
        self.Work_Hour_Start = 8
        self.Scale = 1000000
        self.Func_Type = Poisson(self)

    def set_config(self, database='generated_data', days=7, high_max=1.25 * 10000000, high_min=0,
                   low_max=1.25 * 1500000, low_min=0, business_hours=6, shape=.5, start_date=datetime.date.today(),
                   work_hour_start=8, scale=1000000, func_type='poisson'):
        self.Database = database
        self.Days = days
        self.High_Max = high_max
        self.High_Min = high_min
        self.Low_Max = low_max
        self.Low_Min = low_min
        self.Business_Hours = business_hours
        self.Shape = shape
        self.Start_Date = start_date
        self.Work_Hour_Start = work_hour_start
        self.Scale = scale
        if func_type.lower() == 'poisson':
            self.Func_Type = Poisson(self)
        elif func_type.lower() == 'weibull':
            self.Func_Type = Weibull(self)
        else:
            self.Func_Type = None

    def set_func_type(self, func_type):
        if func_type == 'poisson':
            self.Func_Type = Poisson(self)
        elif func_type == 'weibull':
            self.Func_Type = Weibull(self)
        else:
            self.Func_Type = None

    def get_config(self):
        config_data = [self.Database, self.Days, self.High_Max, self.High_Min, self.Low_Max, self.Low_Min,
                       self.Business_Hours, self.Shape, self.Start_Date, self.Work_Hour_Start, self.Scale,
                       self.Func_Type.Name]
        return config_data
