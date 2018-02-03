'''
    Author: Adrian Cardoza
'''


import numpy as np
import sys
from os import path
from root import ROOT_DIR
sys.path.append(path.join(ROOT_DIR, 'CPacket-Common-Modules'))


class SeasonalTrafficGenerator(object):
    def __init__(self, size, maximum=0, minimum=0, shape=None, distribution_name=None):
        '''

        '''
        self.size = size
        self.maximum = maximum
        self.minimum = minimum
        self.shape = shape
        self.distribution_name = distribution_name
        self.distribution_array = None

    def generate_traffic(self):
        if self.distribution_name == "poisson":
            # Code to generate specified array
            # Replace this with code/class that handles distribution functions?
            lambda_value = self.maximum - (self.maximum / 4)
            self.distribution_array = np.random.poisson(lam=lambda_value, size=self.size)
            return self.distribution_array
        elif self.distribution_name == "beta":
            # Code to generate specified array
            # Replace this with code/class that handles distribution functions?
            print("Functionality not implemented yet!")
        elif self.distribution_name == "weilbull":
            # Code to generate specified array
            # Replace this with code/class that handles distribution functions?
            print("Functionality not implemented yet!")
        else:
            # Error bad function
            print("Error - bad distribution function")

    def generate_low_traffic(self):
        if self.distribution_name == "poisson":
            # Code to generate specified array
            # Replace this with code/class that handles distribution functions?
            lambda_value = self.maximum - (self.maximum / 4)
            self.distribution_array = np.random.poisson(lam=lambda_value, size=self.size)
            return self.distribution_array
        elif self.distribution_name == "beta":
            # Code to generate specified array
            # Replace this with code/class that handles distribution functions?
            print("Functionality not implemented yet!")
        elif self.distribution_name == "weilbull":
            # Code to generate specified array
            # Replace this with code/class that handles distribution functions?
            print("Functionality not implemented yet!")
        else:
            # Error bad function
            print("Error - bad distribution function")

    def generate_high_traffic(self):
        if self.distribution_name == "poisson":
            # Code to generate specified array
            # Replace this with code/class that handles distribution functions?
            lambda_value = self.maximum - (self.maximum / 4)
            self.distribution_array = np.random.poisson(lam=lambda_value, size=self.size)
            return self.distribution_array
        elif self.distribution_name == "beta":
            # Code to generate specified array
            # Replace this with code/class that handles distribution functions?
            print("Functionality not implemented yet!")
        elif self.distribution_name == "weilbull":
            # Code to generate specified array
            # Replace this with code/class that handles distribution functions?
            print("Functionality not implemented yet!")
        else:
            # Error bad function
            print("Error - bad distribution function")

    def show_array(self):
        print(self.distribution_array)


# Test code Poisson
test_seasonal_generator = SeasonalTrafficGenerator(10, 100, 0, None, "poisson")

print("Test: Normal")
test_seasonal_generator.generate_traffic()
test_seasonal_generator.show_array()

print("Test: Low")
test_seasonal_generator.generate_low_traffic()
test_seasonal_generator.show_array()

print("Test: High")
test_seasonal_generator.generate_high_traffic()
test_seasonal_generator.show_array()

# Test code Beta
test_seasonal_generator = SeasonalTrafficGenerator(10, 100, 0, None, "beta")

print("Test: Normal")
test_seasonal_generator.generate_traffic()
test_seasonal_generator.show_array()

print("Test: Low")
test_seasonal_generator.generate_low_traffic()
test_seasonal_generator.show_array()

print("Test: High")
test_seasonal_generator.generate_high_traffic()
test_seasonal_generator.show_array()
