''''
    Author: Adrian Cardoza
'''

import datetime
from resources.weibull import *
from resources.poisson import *


class GeneratorConfig:

    def __init__(self):
        '''

        '''
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

    def set_config(self, database='generated_data', days=7, high_max=1.25 * 10000000, high_min=0, low_max=1.25 * 1500000, low_min=0,
                   business_hours=6, shape=.5, start_date=datetime.date.today(), work_hour_start=8, scale=1000000,
                   func_type='poisson'):
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
        if func_type == 'poisson':
            self.Func_Type = Poisson(self)
        elif func_type == 'weibull':
            self.Func_Type = Weibull(self)
        else:
            self.Func_Type = None

    def set_database(self, database):
        self.Database = database

    def get_database(self):
        return self.Database

    def set_days(self, days):
        self.Days = days

    def get_days(self):
        return self.Days

    def set_high_max(self, high_max):
        self.High_Max = high_max

    def get_high_max(self):
        return self.High_Max

    def set_high_min(self, high_min):
        self.High_Min = high_min

    def get_high_min(self):
        return self.High_Min

    def set_low_max(self, low_max):
        self.Low_Max = low_max

    def get_low_max(self):
        return self.Low_Max

    def set_low_min(self, low_min):
        self.Low_Min = low_min

    def get_low_min(self):
        return self.Low_Min

    def set_business_hours(self, business_hours):
        self.Business_Hours = business_hours

    def get_business_hours(self):
        return self.Business_Hours

    def set_shape(self, shape):
        self.Shape = shape

    def get_shape(self):
        return self.Shape

    def set_start_date(self, start_date):
        self.Start_Date = start_date

    def get_start_date(self):
        return self.Start_Date

    def set_work_hour_start(self, work_hour_start):
        self.Work_Hour_Start = work_hour_start

    def get_work_hour_start(self):
        return self.Work_Hour_Start

    def set_scale(self, scale):
        self.Scale = scale

    def get_scale(self):
        return self.Scale

    def set_func_type(self, func_type):
        if func_type == 'poisson':
            self.Func_Type = Poisson(self)
        elif func_type == 'weibull':
            self.Func_Type = Weibull(self)
        else:
            self.Func_Type = None

    def get_func_type(self):
        if self.Func_Type:
            return type(self.Func_Type).__name__
        else:
            return ''

    def get_config(self):
        config_data = [self.Database, self.Days, self.High_Max, self.High_Min, self.Low_Max, self.Low_Min,
                       self.Business_Hours, self.Shape, self.Start_Date, self.Work_Hour_Start, self.Scale,
                       self.Func_Type.Name]
        return config_data
