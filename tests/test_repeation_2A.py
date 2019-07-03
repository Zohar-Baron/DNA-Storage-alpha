import unittest
from encoding.bin_coding import repeatition_code_2A

class Test_repeatition_2A(unittest.TestCase):

	def test_encode_8bits(self):
		encoded = repeatition_code_2A.encode('01010101')
		self.assertEqual(encoded,'000111000111000111000111')

	def test_encode_7bits(self):
		encoded = repeatition_code_2A.encode('0101010')
		self.assertEqual(encoded,'000111000111000111000')

	def test_decode_1(self):
		decoded = repeatition_code_2A.decode('111000000111111111000111000111000000000')
		self.assertEqual(decoded, '1001110101000')



if __name__ == '__main__':
    unittest.main()