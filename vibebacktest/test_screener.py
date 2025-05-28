import unittest
from unittest.mock import patch
from vibebacktest.screener import Screener

class TestScreenerIntegration(unittest.TestCase):
    @patch("screener.openbb.stocks.screener")
    def test_screen_stocks(self, mock_screener):
        """Integration test for the Screener class with mocked OpenBB API."""
        # Mock data returned by OpenBB API
        mock_screener.return_value = [
            {"symbol": "AAPL", "price": 150, "pe_ratio": 25},
            {"symbol": "MSFT", "price": 300, "pe_ratio": 30},
        ]
        
        # Path to the example strategy file
        strategy_file = "vibebacktest/strategy_example.yaml"
        
        # Initialize the Screener
        screener = Screener(strategy_file)
        
        # Call the screen_stocks method
        stocks = screener.screen_stocks()
        
        # Validate the output
        self.assertIsInstance(stocks, list)
        self.assertGreater(len(stocks), 0)
        print("Screened stocks:", stocks)

    @patch("vibebacktest.screener.openbb.stocks.screener")
    def test_screen_stocks_exception(self, mock_screener):
        """Test exception handling in the screen_stocks method."""
        # Simulate an exception in the OpenBB API
        mock_screener.side_effect = Exception("API error")
        
        # Path to the example strategy file
        strategy_file = "vibebacktest/strategy_example.yaml"
        
        # Initialize the Screener
        screener = Screener(strategy_file)
        
        # Call the screen_stocks method and validate the output
        stocks = screener.screen_stocks()
        self.assertEqual(stocks, [])
        print("Handled exception correctly.")

if __name__ == "__main__":
    unittest.main()