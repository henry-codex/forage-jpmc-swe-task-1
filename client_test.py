import unittest
from client3 import getDataPoint


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # Calculate the expected price for the first quote
        expected_price_1 = (121.2 + 120.48) / 2
        # Calculate the expected price for the second quote
        expected_price_2 = (121.68 + 117.87) / 2

        # Verify the calculated prices against the expected prices
        self.assertEqual(getDataPoint(quotes[0])[3], expected_price_1)
        self.assertEqual(getDataPoint(quotes[1])[3], expected_price_2)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # Calculate the expected price for the first quote
        expected_price_1 = (119.2 + 120.48) / 2
        # Calculate the expected price for the second quote
        expected_price_2 = (121.68 + 117.87) / 2

        # Verify the calculated prices against the expected prices
        self.assertEqual(getDataPoint(quotes[0])[3], expected_price_1)
        self.assertEqual(getDataPoint(quotes[1])[3], expected_price_2)


if __name__ == '__main__':
    unittest.main()
