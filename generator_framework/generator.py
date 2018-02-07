'''
    Author:
'''

from generator_config import *
import numpy as np
import sys
from os import path
# FIX: Code does not run if these are uncommented
#from root import ROOT_DIR
#sys.path.append(path.join(ROOT_DIR, 'CPacket-Common-Modules'))


class Generator:
    def __init__(self):
        '''

        '''
        self._Config = GeneratorConfig()
        self._Days = self._Config.Days
        self._Function = self._Config.Func_Type
        self._Increments = 96 * self._Days
        self._High_Max = self._Config.High_Max
        self._High_Min = self._Config.High_Min
        self._Low_Max = self._Config.Low_Max
        self._Low_Min = self._Config.Low_Min
        self.Dist_Array = None
        self._Weeks = ((self._Days - (self._Days % 7)) / 7)

        # FIX: commenting to test run() function, else there are errors
        '''
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
                self.Dist_Array = np.concatenate([self.Dist_Array, array])
        '''

    def run(self):
        '''
            Runs generator. Not fully implemented. Right now just concatenates
            three arrays together.
        '''
        if self._Function == "poisson":
            # FIX: add code to loop correct amount of time based on self._Days
            # FIX: use Stats class instead of directly calling function
            morning = np.random.poisson(lam=10, size=self._Days)
            # FIX: use Stats class instead of directly calling function
            worktime = np.random.poisson(lam=100, size=self._Days)
            # FIX: use Stats class instead of directly calling function
            evening = np.random.poisson(lam=50, size=self._Days)
            # Last step is merge arrays
            array = np.concatenate((morning, worktime))
            self.Dist_Array = np.concatenate((array, evening))
        elif self._Function == "weilbul":
            print("Functionality not implemented yet!")
        elif self._Function == "beta":
            print("Functionality not implemented yet!")

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

# Test Code - Delete later
test_generator = Generator()
test_generator.run()

print(test_generator.Dist_Array)
