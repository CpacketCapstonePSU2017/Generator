from unittest import TestCase
from generator_framework.generator import Generator, Poisson

# Just for making Travis trigger tests
class TestSample(TestCase):

    poisson_test = Poisson(100, 1.25 * 10000000)
    generator_test = Generator(poisson_test)

    def test_nonempty_generator(self):
        self.assertIsNotNone(self.poisson_test)
        self.assertIsNotNone(self.generator_test)

    def test_empty_generator(self):
        with self.assertRaises(ValueError):
            new_generator_test = Generator(None)

    def test_parameters(self):
        dist_array = self.poisson_test.generate()
        self.assertTrue(dist_array.size == 100)
        self.assertTrue(dist_array.max() <= 1.25 * 10000000)
        self.assertTrue(dist_array.min() >= 0)
