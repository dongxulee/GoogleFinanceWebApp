import os
import psycopg2
import psycopg2.extras
from psycopg2 import sql
from config import *
from csv import DictReader
import pickle
from get_market_data import get_data

# Write code / functions to set up database connection and cursor here.
def get_connection_and_cursor():
	try:
		if db_password != "":
			db_connection = psycopg2.connect("dbname='{0}' user='{1}' password='{2}'".format(db_name, db_user, db_password))
			print("Success connecting to database")
		else:
			db_connection = psycopg2.connect("dbname='{0}' user='{1}'".format(db_name, db_user))
	except:
		print("Unable to connect to the database. Check server and credentials.")
		sys.exit(1) # Stop running program if there's no db connection.

	db_cursor = db_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

	return db_connection, db_cursor


# Write code / functions to create tables with the columns you want and all database setup here.
def setup_database():
	conn, cur = get_connection_and_cursor()

	cur.execute("DROP TABLE IF EXISTS StockInfo")
	cur.execute("DROP TABLE IF EXISTS StockList")

	# cur.execute("DROP TABLE IF EXISTS States")
	cur.execute("""CREATE TABLE IF NOT EXISTS StockList (
			id SERIAL PRIMARY KEY,
			name VARCHAR(40)
		)""")

	# cur.execute("DROP TABLE IF EXISTS Sites")
	cur.execute("""CREATE TABLE IF NOT EXISTS StockInfo (
			stockid INTEGER REFERENCES StockList(id),
			daytime DATE,
			open FLOAT,
			high FLOAT,
			low FLOAT,
			close FLOAT,
			volume FLOAT
		)""")

	conn.commit()
	print('Setup database complete')


# Write code / functions to deal with CSV files and insert data into the database here.
def insert(conn, cur, table, data_dict):
	column_names = data_dict.keys()
	query = sql.SQL('INSERT INTO {0}({1}) VALUES({2}) ON CONFLICT DO NOTHING').format(
		sql.SQL(table),
		sql.SQL(', ').join(map(sql.Identifier, column_names)),
		sql.SQL(', ').join(map(sql.Placeholder, column_names))
	)
	query_string = query.as_string(conn)
	cur.execute(query_string, data_dict)

def csv_insert(tickers, conn, cur):
	for i in range(len(tickers)):
		ticker = tickers[i]
		stockId = i + 1
		stockReader = DictReader(open('stock_dfs/' + ticker + '.csv', 'r'))
		insert(conn, cur, 'StockList' ,{"name": ticker})
		for info in stockReader:
			diction = {}
			diction['stockid'] = stockId
			diction['daytime'] = info['']
			diction['open'] = info['Open']
			diction['high'] = info['High']
			diction['low'] = info['Low']
			diction['close'] = info['Close']
			diction['volume'] = info['Volume']
			insert(conn, cur, 'StockInfo', diction)
	conn.commit()


def dataBaseConstuct(cachData = False):
	'''
		this function is use to construct the sql database base on the csv files
		. If cachData is ture, so we request the data through the api and the
		csv files in the folder stock_dfs will be renewed completely.
	'''
	if (cachData == True):
		get_data(reload_sp500 = False, frequency = '86400', period = '3M')

	with open("sp500tickers.pickle", "rb") as f:
		tickers = pickle.load(f)

	setup_database()
	conn, cur = get_connection_and_cursor()
	csv_insert(tickers, conn, cur)
















