import unittest
from oxrse_unit_conv.units import fortnight, second


class TestFortnight(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(fortnight.si_unit.matches(second))

    def test_to_si(self):
        self.assertEqual(fortnight.to_si(1), 1209600)
    
if __name__ == '__main__':
    unittest.main()