from get_market_data import get_data
'''
		- store all the data in the csv file, under the stock_dfs folder
		- default time frame is 1M, it could also be 1Y, 1D, etc, you can refer to googlefinance for more info
		- default frequency is 86400 second, which is 1 day intervals
		- default input of reload_sp500 is False. If it is true, all tickers will be renewed.
		renew the database, delete all stock files, all stock data
'''
get_data(reload_sp500 = False, frequency = '86400', period = '1M')