import unittest
from .Adder import Adder

class TestAdder(unittest.TestCase):

	def	test_add_positive(self):
		self.assertEqual(5, Adder.add(2, 3))