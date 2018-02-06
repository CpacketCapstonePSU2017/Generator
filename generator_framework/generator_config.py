''''
    Author: Adrian Cardoza
'''


class GeneratorConfig:

    def __init__(self):
        '''

        '''
        self._Days = 7
        self._High_Max = 100
        self._High_Min = 0
        self._Low_Max = 50
        self._Low_Min = 0
        self._Business_Hours = 6
        self._Func_Type = "poisson"

    def set_config(self, days=None, high_day_max=None, high_day_min=None, low_day_max=None, low_day_min=None,
                   business_hours=None, funct_type=None):
        self._Days = days
        self._High_Max = high_day_max
        self._High_Min = high_day_min
        self._Low_Max = low_day_max
        self._Low_Min = low_day_min
        self._Business_Hours = business_hours
        self._Func_Type = funct_type

    def get_config(self):
        print("configuration: %d %d %d %d %d %d %s" % (self._Days, self._High_Max, self._High_Min,
              self._Low_Max, self._Low_Min, self._Business_Hours, self._Func_Type))
