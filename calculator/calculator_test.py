from unittest import TestCase, main
import calculator

class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)
    def test_minus(self):
        self.assertEqual(calculator('3-1'), 2)
    def test_multi(self):
        self.assertEqual(calculator('7*2'), 14)
    def test_divide(self):
        self.assertEqual(calculator('10/5'), 2.0)
    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('')
        self.assertEqual('', e.exception.args[0])
if __name__ == '__main__':
    main()