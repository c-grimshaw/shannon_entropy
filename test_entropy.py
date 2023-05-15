import unittest

from entropy import shannon_entropy


class ShannonEntropyTestCase(unittest.TestCase):
    def test_shannon_entropy_with_valid_input(self):
        word = "ojriubswjbza15pub2abivpe5.net"
        n = 2
        expected_entropy = 4.735926350629031

        calculated_entropy = shannon_entropy(word, n)
        self.assertAlmostEqual(calculated_entropy, expected_entropy)

    def test_shannon_entropy_with_different_input(self):
        word = "rmc.ca"
        n = 1
        expected_entropy = 2.2516291673878226

        calculated_entropy = shannon_entropy(word, n)
        self.assertAlmostEqual(calculated_entropy, expected_entropy)


if __name__ == "__main__":
    unittest.main()
