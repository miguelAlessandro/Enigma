import unittest
from library.enigma import Enigma

class MyTestCase(unittest.TestCase):
    def test_enigma_1(self):
        machine = Enigma(3, [1, 2, 3],
                         ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"],
                         ['AB'], ['A', 'B', 'C'])
        self.assertEqual(machine.press('A'), 'C')
        self.assertEqual(machine.press('A'), 'C')
        self.assertEqual(machine.press('A'), 'C')

    def test_enigma_2(self):
        machine = Enigma(3, [1, 2, 3],
                         ["CBADEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"],
                         ['AB'], ['A', 'B', 'C'])
        self.assertEqual(machine.press('A'), 'C')
        self.assertEqual(machine.press('A'), 'C')
        self.assertNotEqual(machine.press('A'), 'C')

    def test_enigma_3(self):
        with self.assertRaises(AssertionError):
            machine = Enigma(2, [1, 2, 3],
                            ["CBADEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"],
                            ['AB'], ['A', 'B', 'C'])


if __name__ == '__main__':
    unittest.main()
