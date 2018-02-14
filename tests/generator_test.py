from generator_framework import generator
from generator_framework import generator_config
import random
from unittest import TestCase


class TestGenerator(TestCase):

    def setUp(self):
        self.gen = generator.Generator()
        self.config = generator_config.GeneratorConfig()

    def tearDown(self):
        self.gen = None
        self.config = None

    # Test that config class prints out properly (will always pass)
    # TODO implement some way to check that the printed values are correct
    def test_GetConfig(self):
        self.config.get_config()

    # Check that set config works properly
    # TODO Function type cannot be specified properly in a way the code will execute
        # Set config should be able to properly recognize a string of the function name and use the according class
    def test_SetConfig(self):
        self.config.set_config(14, 200, 0, 100, 0, 12, "weibull", 1)
        self.config.get_config()

    def test_arraySize(self):
        # Get expected array size
        size = self.config.Days * 24 * (60 / 15)
        # print("Expected array size: ", size)
        self.assertEquals(len(self.gen.Dist_Array[1]), size, "Incorrect Array Size")

    # TODO Create a way for values in the config to be changed and used on the fly
    # Check that the array has correct size with custom inputted days
    def test_customArraySize(self):
        self.fail("Can't enter custom days yet")
        # Set random number of days to be tested.
        self.config.Days = random.randint(7, 25)
        # Get expected array size
        size = self.config.Days * 24 * (60 / 15)
        print("Expected array size: ", size)
        self.gen = generator.Generator()
        print(len(self.gen.Dist_Array[1]))

    # Check that the generated data has cliffs (high days and low days)
    def test_arrayCliffs(self):
        pass

    # Check that generated data with a custom config will have proper cliffs
    def test_customArrayCliffs(self):
        pass
