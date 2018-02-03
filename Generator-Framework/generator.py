import numpy as np
import sys
from os import path
from root import ROOT_DIR
sys.path.append(path.join(ROOT_DIR, 'CPacket-Common-Modules'))

class Generator:
    def __init__(self, days, functype, high_max, high_min, low_max, low_min):
        self._Days = days
        self._Function = functype
        self._Increments = 96 * days
        self._High_Max = high_max
        self._High_Min = high_min
        self._Low_Max = low_max
        self._High_Min = low_min

        remainder = days % 7
        days_to_convert = days - remainder
        self._Weeks = days_to_convert / 7
        self.Dist_Array = None
        for week in self._Weeks:
            array = []
            count = 0
            while count < 7:
                if count < 5:
                    #generate high traffic morning
                    #generate high traffic work time
                    #generate high traffic evening
                    array = np.concatenate([morning, worktime, evening])
                else:
                    #generate low traffic morning
                    #generate low traffic work time
                    #generate low traffic evening
                    array = np.concatenate([morning, worktime, evening])
                self.Dist_Array = np.concat([self.Dist_Array, array])


'''class Generator:

# The way this is set up, every distribution function to be passed in here needs a method called "generate" to do its work.

    def __init__(self, functype):
        """
                    Creates the specified distribution into an Array
                    :param: Min: Should almost always be 0 as we don't use negative values
                    :param: Max: Can change varying on function. Should usually be infinity.
                    :param: Size: How many elements to generate
                    :param: Shape: The shape of the distribution.
                    :param: Type: The distribution function to use. For now 'None' will default to Poisson.
        """
        if functype is None:
            raise ValueError("functype cannot be None")
        self._Function = functype

        self.Dist_Array = self._Function.generate()

    def show_array(self):
        for x in self.Dist_Array:
            print(x)'''