''''
    Author: Adrian Cardoza
'''


class GeneratorConfig:

    def __init__(self):
        '''

        '''
        self.time = 7
        self.high_day_max = 100
        self.high_day_min = 0
        self.low_day_max = 50
        self.low_day_min = 0
        self.business_hours = 6
        self.distribution_function = "poisson"

    def set_config(self, time=None, high_day_max=None, high_day_min=None, low_day_max=None, low_day_min=None,
                   business_hours=None, distribution_function=None):
        self.time = time
        self.high_day_max = high_day_max
        self.high_day_min = high_day_min
        self.low_day_max = low_day_max
        self.low_day_min = low_day_min
        self.business_hours = business_hours
        self.distribution_function = distribution_function

    def get_config(self):
        print("configuration: %d %d %d %d %d %d %s" % (self.time, self.high_day_max, self.high_day_min,
              self.low_day_max, self.low_day_min, self.business_hours, self.distribution_function))


#Test Code
test_generator_config = GeneratorConfig()
test_generator_config.get_config()
test_generator_config.set_config(14, 200, 0, 100, 0, 12, "beta")
test_generator_config.get_config()
