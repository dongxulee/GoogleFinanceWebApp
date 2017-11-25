import pandas as pd
import pickle
import os
import save_tickers
from googlefinance.client import get_price_data, get_prices_time_data

def get_data(reload_sp500 = False, frequency = '86400', period = '1M'):
	'''
		- store all the data in the csv file, under the stock_dfs folder
		- default time frame is 1M, it could also be 1Y, 1D, etc, you can refer to googlefinance for more info
		- default frequency is 86400 second, which is 1 day intervals
		- default input of reload_sp500 is False. If it is true, all tickers will be renewed.
		renew the database, delete all stock files, all stock data
	'''
	filelist = [f for f in os.listdir("./stock_dfs") if f.endswith(".csv")]
	for f in filelist:
		os.remove("./stock_dfs/{}".format(f))
	if not os.path.exists('stock_dfs'):
		os.makedirs('stock_dfs')

	if reload_sp500:
		tickers = save_tickers.save_sp500_tickers()
	else:
		with open("sp500tickers.pickle", "rb") as f:
			tickers = pickle.load(f)

	for ticker in tickers:
		print(ticker)
		param = {
			'q': ticker, # Stock symbol (ex: "AAPL")
			'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
			'x': "INDEXSP", # Stock exchange symbol on which stock is traded (ex: "NASD")
			'p': "1M" # Period (Ex: "1Y" = 1 year)
		}
		# just in case the connection breaks, we'd like to save our progress!
		if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
			# because now the wikipedia is using '.' instead of '-', sometimes just use . to replace -.
			try:
				# get price data (return pandas dataframe)
				df = get_price_data(param)
				df.to_csv('stock_dfs/{}.csv'.format(ticker))
			except Exception as e:
				print('ticker error: {}'.format(ticker))
		else:
			print('Already have {}'.format(ticker))