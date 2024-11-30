
import unittest
from functions import sum_funct, sub_funct

class TestFunctions(unittest.TestCase):
  def test_sum_funct(self):
    self.assertEqual(sum_funct(5,2), 7)
  
  def test_sub_funct(self):
    self.assertEqual(sub_funct(3,2), 1)

if __name__ == "__main__":
  unittest.main()
