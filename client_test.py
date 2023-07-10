import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        expected_price = (quote['top_bid']['price'] +
                          quote['top_ask']['price']) / 2
        self.assertEqual(price, expected_price)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       stock, bid_price, ask_price, price = getDataPoint(quote)
       expected_price = (quote['top_bid']['price'] +
                         quote['top_ask']['price']) / 2
       self.assertGreater(bid_price, ask_price)
       self.assertEqual(price, expected_price)

  """ ------------ Add more unit tests ------------ """

  def test_getRatio(self):
      price_a = 10.0
      price_b = 5.0
      expected_ratio = 2.0

      result_ratio = getRatio(price_a, price_b)

      self.assertEqual(result_ratio, expected_ratio)

  def test_getRatio_divideByZero(self):
      price_a = 10.0
      price_b = 0.0

      result_ratio = getRatio(price_a, price_b)

      self.assertIsNone(result_ratio)

if __name__ == '__main__':
    unittest.main()
