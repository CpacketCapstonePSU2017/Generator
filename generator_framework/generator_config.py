''''
    Author: Adrian Cardoza
'''

import datetime


class GeneratorConfig:

    def __init__(self):
        '''

        '''
        self.Days = 7
        self.High_Max = 100
        self.High_Min = 0
        self.Low_Max = 50
        self.Low_Min = 0
        self.Business_Hours = 6
        self.Func_Type = "poisson"
        self.Start_Date = datetime.date.today()

    def set_config(self, days=None, high_day_max=None, high_day_min=None, low_day_max=None, low_day_min=None,
                   business_hours=None, funct_type=None, start_date=None):
        self.Days = days
        self.High_Max = high_day_max
        self.High_Min = high_day_min
        self.Low_Max = low_day_max
        self.Low_Min = low_day_min
        self.Business_Hours = business_hours
        self.Func_Type = funct_type
        self.Start_Date = start_date

    def get_config(self):
        print("configuration: %d %d %d %d %d %d %s %s" % (self.Days, self.High_Max, self.High_Min,
              self.Low_Max, self.Low_Min, self.Business_Hours, self.Func_Type, self.Start_Date))
