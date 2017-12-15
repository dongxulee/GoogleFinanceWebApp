import unittest
from retrieveData import *
import pandas as pd
import pickle
from database import *


class Test_Pickle_caching(unittest.TestCase):
	'''
		the catch method and all the tickers we get from the web scratch
	'''
	def setUp(self):
		with open("sp500tickers.pickle", "rb") as f:
			tickers = pickle.load(f)
		self.tickers = tickers
	def test_listOfTickers(self):
		tickers = self.tickers
		self.assertTrue(len(tickers) > 500)
		for ticker in tickers:
			self.assertIsInstance(ticker, str)

class Test_Caching(unittest.TestCase):
	'''
		testing the correct format of the cached excel file
	'''
	def setUp(self):
		self.data = pd.read_csv('stock_dfs/A.csv')
	def test_csv(self):
		pd = self.data
		self.assertTrue(pd.size != 0)
	def test_pd_value_datatype(self):
		pd = self.data
		self.assertIsInstance(pd['Open'][0], float)
		self.assertIsInstance(pd['High'][0], float)
		self.assertIsInstance(pd['Low'][0], float)
		self.assertIsInstance(pd['Close'][0], float)
	def test_pd_shape(self):
		pd = self.data
		self.assertTrue(pd.shape, (64, 6))


class Test_retrieveDataFunction(unittest.TestCase):
	'''
		testing database retrieve data process successful, return data type is
		Stock object and then conduct object testing.
	'''
	def setUp(self):
		self.tStock = retriveStockData('A')
	def test_retriveStockDataFunction(self):
		obj = self.tStock
		self.assertTrue(obj != 0)
	def test_obj_attribute(self):
		obj = self.tStock
		self.assertIsInstance(obj, Stock)
		self.assertIsInstance(obj.info['open'][0], float)
		self.assertIsInstance(obj.info['high'][0], float)
		self.assertIsInstance(obj.info['low'][0], float)
		self.assertIsInstance(obj.info['close'][0], float)
	def test_obj_repr_method(self):
		obj = self.tStock
		self.assertIsInstance(obj.__repr__(), str)
	def test_obj_contains_method(self):
		obj = self.tStock
		self.assertTrue(obj.__contains__('A'))

class Test_dataDase(unittest.TestCase):
	def setUp(self):
		conn, cur = get_connection_and_cursor()
		self.conn = conn
		self.cur = cur
	def test_stocklist_table(self):
		cur = self.cur
		cur.execute(""" select * from stocklist where name = '{}'""".format('A'))
		stockid = cur.fetchall()[0]['id']
		self.assertTrue(stockid == 14)
	def test_stockinfo_table(self):
		cur = self.cur
		cur.execute(""" select * from stockinfo where stockid = {}""".format(1))
		stockinfo = cur.fetchall()
		self.assertIsInstance(stockinfo, list)
		self.assertTrue(len(stockinfo[0]) == 7)
		self.assertTrue(len(stockinfo) == 64)




if __name__ == "__main__":
	unittest.main(verbosity=2)