from generator_framework import generator
from generator_framework import generator_config
import random
import datetime
from unittest import TestCase


class TestGenerator(TestCase):

    def setUp(self):
        self.gen = generator.Generator()
        self.config = generator_config.GeneratorConfig()

    def tearDown(self):
        self.gen = None
        self.config = None

    # Test that config class prints out properly (will always pass)
    def test_GetConfig(self):
        # build a list with class variable manually
        manual_config_list = [self.config.Database, self.config.Days, self.config.High_Max, self.config.High_Min,
                              self.config.Low_Max, self.config.Low_Min, self.config.Business_Hours, self.config.Shape,
                              self.config.Start_Date, self.config.Work_Hour_Start, self.config.Scale,
                              self.config.Func_Type.Name]
        # build a list using the get_config()
        get_config_list = self.config.get_config()
        # compare the list and return result
        count = 0
        result = 0
        for i in manual_config_list:
            if i != get_config_list[count]:
                result = -1
                break
            else:
                count += 1
        self.assertEqual(result, 0, "Compared lists are not equal ")

    # Check that set config works properly
    def test_SetConfig(self):
        data = ['weibull_data', 7, 100, 0, 50, 0, 8, 1, datetime.date.today(), 8, 1, 'weibull']
        self.config.set_config(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7],
                               data[8], data[9], data[10], data[11])
        get_data = self.config.get_config()
        count = 0
        result = 0
        for i in data:
            if i != get_data[count]:
                result = -1
                break
            else:
                count += 1
        self.assertEqual(result, 0, "Compared lists are not equal")

    def test_arraySize(self):
        # Get expected array size
        size = self.config.Days * 24 * (60 / 15)
        # print("Expected array size: ", size)
        timestamps = self.gen.Dist_Array[0]
        data = self.gen.Dist_Array[1]
        self.assertEquals(len(timestamps), len(data), "Timestamp and Data arrays have different sizes")
        self.assertEquals(len(self.gen.Dist_Array[0]), size, "Incorrect Timestamp Array Size")
        self.assertEquals(len(self.gen.Dist_Array[1]), size, "Incorrect Data Array Size")

    # Check that the array has correct size with custom inputted days
    def test_customArraySize(self):
        # Set random number of days to be tested.
        self.config.set_config(days=random.randint(7, 25))
        # Get expected array size
        size = self.config.Days * 24 * (60 / 15)
        # print("Expected array size: ", size)
        self.gen = generator.Generator(self.config)
        # print(self.gen.Dist_Array)
        timestamps = self.gen.Dist_Array[0]
        data = self.gen.Dist_Array[1]
        self.assertEquals(len(timestamps), len(data), "Timestamp and Data arrays have different sizes")
        self.assertEquals(len(self.gen.Dist_Array[0]), size, "Incorrect Timestamp Array Size")
        self.assertEquals(len(self.gen.Dist_Array[1]), size, "Incorrect Data Array Size")

    # Check that the generated data has cliffs (high days and low days)
    def test_arrayCliffs(self):
        pass

    # Check that generated data with a custom config will have proper cliffs
    def test_customArrayCliffs(self):
        pass
