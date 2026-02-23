import unittest
from data_processor import clean_currency, parse_timestamp, summarize_sales

class TestDataEngineeringIntern(unittest.TestCase):

    # ==========================================
    # TASK 1: Data Cleaning & Type Casting
    # ==========================================
    def test_clean_currency(self):
        """Test that currency strings are converted to floats correctly."""
        self.assertEqual(clean_currency("$1,200.50"), 1200.50)
        self.assertEqual(clean_currency("€ 50.00"), 50.0)
        self.assertEqual(clean_currency("100"), 100.0)
        
        # Edge case: Handle None or empty strings safely (return 0.0)
        self.assertEqual(clean_currency(None), 0.0)
        self.assertEqual(clean_currency(""), 0.0)

    # ==========================================
    # TASK 2: Date Parsing (Standardization)
    # ==========================================
    def test_parse_timestamp(self):
        """Test that various date formats are converted to ISO 8601 strings (YYYY-MM-DD)."""
        # Input format: MM/DD/YYYY -> Output: YYYY-MM-DD
        self.assertEqual(parse_timestamp("12/01/2025"), "2025-12-01")
        self.assertEqual(parse_timestamp("01/30/2023"), "2023-01-30")
        
        # Edge case: If the date is invalid or None, return None
        self.assertIsNone(parse_timestamp("invalid-date"))
        self.assertIsNone(parse_timestamp(None))

    # ==========================================
    # TASK 3: Aggregation (The "Group By" Logic)
    # ==========================================
    def test_summarize_sales(self):
        """Test aggregation of sales data by category."""
        raw_data = [
            {"id": 1, "category": "Electronics", "amount": 100.0},
            {"id": 2, "category": "Books", "amount": 20.0},
            {"id": 3, "category": "Electronics", "amount": 50.0},
            {"id": 4, "category": "Books", "amount": 10.0},
            {"id": 5, "category": "Clothing", "amount": 30.0},
        ]

        expected_output = {
            "Electronics": 150.0,
            "Books": 30.0,
            "Clothing": 30.0
        }

        self.assertEqual(summarize_sales(raw_data), expected_output)

        # Edge case: Empty input list
        self.assertEqual(summarize_sales([]), {})

if __name__ == '__main__':
    unittest.main()