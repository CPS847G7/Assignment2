import unittest
from add import add

class TestAdder(unittest.TestCase):

	def	test_add_positive_integer(self):
		self.assertEqual(5, add(2, 3))

	def test_add_negative_integer(self):
		self.assertEqual(-2, add(2, -4))

	def test_add_positive_float(self):
		self.assertEqual(2.5, add(1.0, 1.5))

	def test_add_negative_float(self):
		self.assertEqual(-2.5, add(1.0, -3.5))