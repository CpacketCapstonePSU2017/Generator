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
        self.Database = 'poisson_data'
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

    def set_config(self, days=None, high_day_max=None, high_day_min=None, low_day_max=None, low_day_min=None,
                   business_hours=None, funct_type=None, shape=None, start_date=None):
        self.Days = days
        self.High_Max = high_day_max
        self.High_Min = high_day_min
        self.Low_Max = low_day_max
        self.Low_Min = low_day_min
        self.Business_Hours = business_hours
        self.Func_Type = funct_type
        self.Shape = shape
        self.Start_Date = start_date

    def get_config(self):
        print("configuration: %d %d %d %d %d %d %s %d %s" % (self.Days, self.High_Max, self.High_Min,
              self.Low_Max, self.Low_Min, self.Business_Hours, self.Func_Type, self.Shape, self.Start_Date))


#Test Code
#test_generator_config = GeneratorConfig()
#test_generator_config.get_config()
#test_generator_config.set_config(14, 200, 0, 100, 0, 12, "weibull", 1)
#test_generator_config.get_config()
