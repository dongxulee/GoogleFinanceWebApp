import psycopg2
import psycopg2.extras
import pandas as pd
from config import *
from pylab import *

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

class Stock:
	'''
	    pass in a list of dictionary, construct the stock object base on the dictionary
	'''
	def __init__(self, stockinfo, ticker):
	    self.name = ticker
	    self.info = pd.DataFrame(stockinfo)

	def __repr__(self):
	    return 'stock price information include open high low and volume for stock: {}'.format(self.name)

	def __contains__(self, letter):
	    '''
	        check if a letter is in the class name
	    '''
	    return (letter in self.name)

def retriveStockData(ticker):
	'''
	    input is the name of the ticker and return a dictionary
	'''
	conn, cur = get_connection_and_cursor()
	cur.execute(""" select * from stocklist where name = '{}'""".format(ticker))
	stockid = cur.fetchall()[0]['id']
	cur.execute(""" select * from stockinfo where stockid = {}""".format(stockid))
	stockinfo = cur.fetchall()
	return Stock(stockinfo, ticker)






