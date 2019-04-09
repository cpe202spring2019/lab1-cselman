import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        """Testing the output of the __repr__ function in the Location class"""
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc1 = Location("Paris", 18.2, -11.2)
        self.assertEqual(repr(loc1), "Location('Paris', 18.2, -11.2)")
        self.assertNotEqual(repr(loc1), "Location('Paris', 18.0, -11.2)")
    # Add more tests!

    def test_eq(self):
        """Testing the output of the __eq__ function in the Location class.
        All values and names must be the same for the Location objects to be equal."""
        loc1 = Location("SLO", 10.0, -5.0)
        loc2 = Location("SLO", 10.0, -5.0)
        loc3 = Location("Paris", 4.0, -15.0)
        self.assertNotEqual(loc1, loc3)
        self.assertEqual(loc1, loc2)
        self.assertNotEqual(loc2, loc3)

if __name__ == "__main__":
        unittest.main()