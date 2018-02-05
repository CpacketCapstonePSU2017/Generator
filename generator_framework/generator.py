import numpy as np
import sys
from os import path
from root import ROOT_DIR
sys.path.append(path.join(ROOT_DIR, 'CPacket-Common-Modules'))

class Poisson:

    def __init__(self, size, maximum, minimum=0, shape=None):
        if maximum is None:
            raise ValueError("maximum cannot not be None")
        self._Size = size
        self._Max = maximum
        self._Min = minimum
        self._Shape = shape

        self.Dist_Array = None

    def generate(self):
        lambda_value = self._Max - (self._Max / 4)

        self.Dist_Array = np.random.poisson(lam=lambda_value, size=self._Size)
        for x in self.Dist_Array:
            if x > self._Max:
                x = self._Max
        return self.Dist_Array




class Generator:

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
            print(x)


poisson_test = Poisson(100, 1.25 * 10000000)
generator_test = Generator(poisson_test)
generator_test.show_array()
