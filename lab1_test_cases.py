import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Testing the max_list_iter function in lab1.py. Confirms the output to the
        function is correct."""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        tlist = [1, 2, 3, 4]
        self.assertEqual(max_list_iter(tlist), 4)
        tlist = [3, 2, 1, 0]
        self.assertEqual(max_list_iter(tlist), 3)
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_reverse_rec(self):
        """Tests the reverse_rec function in lab1.py. Confirms the output to the
        function is correct."""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([5, 4, 3, 2, 1]),[1, 2, 3, 4, 5])
        self.assertEqual(reverse_rec([]),[])
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        """Tests the bin_search function in lab1.py. Confirms the output to the
        function is correct."""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        list_val = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(bin_search(6, 0, 6, list_val), 5)
        self.assertEqual(bin_search(1, 0, 6, list_val), 0)
        list_val = [5, 10, 15, 20]
        self.assertEqual(bin_search(25, 0, 3, list_val), None)
        list_val = []
        with self.assertRaises(ValueError):
            bin_search(1, 0, 1, list_val)

if __name__ == "__main__":
        unittest.main()