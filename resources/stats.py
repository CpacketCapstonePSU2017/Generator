"""
    A simple function for Distributions
    The byte count is accessed from ._ByteCount for each new object created.
"""

import numpy as np


class Stats:

    def __init__(self, size, maximum=None, minimum=0, shape=None, functype=None):
        """
            Creates the specified distribution into an Array
            :param: Min: Should almost always be 0 as we don't use negative values
            :param: Max: Can change varying on function. Should usually be infinity.
            :param: Size: How many elements to generate
            :param: Shape: The shape of the distribution.
            :param: Type: The distribution function to use. For now 'None' will default to Poisson.
        """

        # copied for Generate function.
        self._Min = minimum
        self._Max = maximum
        self._Size = size
        self._Shape = shape
        self._Func_Type = functype
        # public
        self.Dist_Array = None

        # Default function type will be Poisson.
        if self._Func_Type is None or self._Func_Type == 'poisson':
            if self._Max is None:
                # default to hardcoded max
                self._Max = 1.25 * 10000000
            # TODO: Fiddle with this level of variance
            lam = self._Max - (self._Max / 4)
            self.Dist_Array = np.random.poisson(lam=lam, size=self._Size)
            for x in self.Dist_Array:
                if x > self._Max:
                    x *= 0
                    x += self._Max
        elif self._Func_Type == 'weibull':
            if self._Max is None:
                self._Max = 1.25 * 10000000
            self.Dist_Array = (1000000 * np.random.weibull(self._Shape, self._Size)).astype(int)
            self.Dist_Array[self.Dist_Array > self._Max] = self._Max
            for x in self.Dist_Array:
                if x > self._Max:
                    print("x is greater than max")
                    x *= 0
                    x += self._Max
        elif self._Func_Type == 'beta':
            # beta function implementation
            pass
        else:
            print("Function type not recognized!")

    # Used for getting a second Dist array later in development.
    # overwrites the current Dist_Array.
    def generate(self):
        # switch for function type
        # Default
        if self._Func_Type is None or self._Func_Type == 'poisson':
            if self._Max is None:
                # default hardcoded value
                self._Max = 1.25 * 10000000
            # TODO: Fiddle with this level of variance
            lam = self._Max - (self._Max / 4)
            # TODO: error check Max and Size
            self.Dist_Array = np.random.poisson(lam=lam, size=self._Size)
            for x in self.Dist_Array:
                if x > self._Max:
                    x *= 0
                    x += self._Max
        elif self._Func_Type == 'weibull':
            if self._Max is None:
                self._Max = 1.25 * 10000000
            self.Dist_Array = (10000000 * np.random.weibull(self._Shape, self._Size)).astype(int)
            for x in self.Dist_Array:
                if x > self._Max:
                    x *= 0
                    x += self._Max
        elif self._Func_Type == 'beta':
            pass
        else:
            print("Function type not recognized!")
            return -1

        return self.Dist_Array
