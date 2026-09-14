import io
import unittest
from unittest.mock import patch

import main


class BMITestCase(unittest.TestCase):
    def test_calculate_bmi_accepts_decimal_weight(self):
        self.assertAlmostEqual(main.calculate_bmi(1.7, 72.5), 25.08650519031142)

    def test_calculate_bmi_rejects_zero_height(self):
        with self.assertRaisesRegex(ValueError, "Height must be greater than 0."):
            main.calculate_bmi(0, 72.5)

    def test_main_formats_bmi_to_two_decimals(self):
        with patch("builtins.input", side_effect=["Alice", "1.7", "72.5"]), patch(
            "sys.stdout", new_callable=io.StringIO
        ) as stdout:
            main.main()

        self.assertEqual(stdout.getvalue(), "Alice Your BMI is 25.09\n")

    def test_main_prints_error_for_zero_height(self):
        with patch("builtins.input", side_effect=["Alice", "0", "72.5"]), patch(
            "sys.stdout", new_callable=io.StringIO
        ) as stdout:
            main.main()

        self.assertEqual(stdout.getvalue(), "Height must be greater than 0.\n")

if __name__ == "__main__":
    unittest.main()
