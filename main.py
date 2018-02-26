"""
A sample script for running the generator.
"""

from root import ROOT_DIR
from generator_framework import generator
from generator_framework import generator_config

"""
We can create an instance of the generator config.
This class comes with default values that can be edited.
"""
config = generator_config.GeneratorConfig()

"""
We can also change values of the config on the fly.
TODO: Add description of all values in config.
"""
config.Days = 14

"""
Then generator will be run when it is initiated, creating an array of the generated data.
By default the generator will create its own config instance thus using the hardcoded defaults.
"""
gen = generator.Generator()
# Array of timestamps
timestamps = gen.Dist_Array[0]
# Array of data points
data = gen.Dist_Array[1]
# As a data frame
# DF = gen.nparray_to_dataframe()
# print(DF)

"""
You can also input a config instance as a input for the generator to use.
This allows for config variables to be changed on the fly and the generator to be re-run.
"""
gen = generator.Generator(config)
