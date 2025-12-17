"""
Unit tests for the pricing module.
Run with: python -m unittest discover tests
"""

import unittest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pricing import format_price, convert_currency


class TestFormatPrice(unittest.TestCase):
    """Tests for the format_price function."""
    
    def test_format_price_rounds_up(self):
        """19.99 should round UP to 20, not truncate to 19."""
        result = format_price(19.99)
        self.assertEqual(result, 20, 
            "format_price(19.99) should return 20, not 19! "
            "Hint: Use round() instead of int()")
    
    def test_format_price_rounds_down(self):
        """19.49 should round DOWN to 19."""
        result = format_price(19.49)
        self.assertEqual(result, 19,
            "format_price(19.49) should return 19")
    
    def test_format_price_exact(self):
        """25.00 should stay as 25."""
        result = format_price(25.00)
        self.assertEqual(result, 25,
            "format_price(25.00) should return 25")
    
    def test_format_price_half(self):
        """10.50 should round to 10 (Python rounds .5 to even)."""
        result = format_price(10.50)
        self.assertEqual(result, 10,
            "format_price(10.50) should return 10 (banker's rounding)")
    
    def test_format_price_large_number(self):
        """999.99 should round to 1000."""
        result = format_price(999.99)
        self.assertEqual(result, 1000,
            "format_price(999.99) should return 1000")


class TestConvertCurrency(unittest.TestCase):
    """Tests for the convert_currency function."""
    
    def test_convert_currency(self):
        """100 USD at 0.85 rate should equal 85.0 EUR."""
        result = convert_currency(100, 0.85)
        self.assertEqual(result, 85.0,
            "convert_currency(100, 0.85) should return 85.0! "
            "Hint: Return amount * exchange_rate")
    
    def test_convert_currency_reverse(self):
        """50 EUR at 1.18 rate should equal 59.0 USD."""
        result = convert_currency(50, 1.18)
        self.assertEqual(result, 59.0,
            "convert_currency(50, 1.18) should return 59.0")
    
    def test_convert_currency_same(self):
        """Converting with rate 1.0 should return the same amount."""
        result = convert_currency(75.50, 1.0)
        self.assertEqual(result, 75.50,
            "convert_currency(75.50, 1.0) should return 75.50")
    
    def test_convert_currency_zero(self):
        """Converting 0 should return 0."""
        result = convert_currency(0, 0.85)
        self.assertEqual(result, 0.0,
            "convert_currency(0, 0.85) should return 0.0")


if __name__ == '__main__':
    unittest.main()
