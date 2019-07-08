import unittest
from encoding.bin2dna.two_bits import two_bits_3

class Test_3(unittest.TestCase):
    def test_bin2dna_1(self):
        translated = two_bits_3.bin2dna('01100111100010101011')
        self.assertEqual(translated,'TATCAGAAAC')

    def test_dna2bin_1(self):
        translated = two_bits_3.dna2bin('TATCAGAAAC')
        self.assertEqual(translated, '01100111100010101011')

if __name__ == '__main__':
    unittest.main()